import os
import sys
import threading
import asyncio
import logging
from flask import Flask
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.errors import SessionPasswordNeededError, PhoneCodeInvalidError, PhoneNumberInvalidError
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# ================== إعداد التسجيل (Logging) ==================
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ================== المتغيرات البيئية ==================
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
PORT = int(os.environ.get("PORT", 8080))

# التحقق من وجود المتغيرات الأساسية
missing_vars = []
if not API_ID:
    missing_vars.append("API_ID")
if not API_HASH:
    missing_vars.append("API_HASH")
if not BOT_TOKEN:
    missing_vars.append("BOT_TOKEN")

if missing_vars:
    logger.error(f"❌ المتغيرات البيئية التالية غير موجودة: {', '.join(missing_vars)}")
    sys.exit(1)

# تحويل API_ID إلى رقم صحيح
try:
    API_ID = int(API_ID)
except ValueError:
    logger.error("❌ API_ID يجب أن يكون رقماً")
    sys.exit(1)

logger.info("✅ تم تحميل المتغيرات البيئية بنجاح")

# ================== تخزين بيانات المستخدمين المؤقتة ==================
users = {}

# ================== دوال البوت ==================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    await update.message.reply_text(
        "📱 أهلاً بك!\nأرسل رقم هاتفك مع رمز الدولة:\nمثال: +9665xxxxxxxx"
    )
    # إنشاء بيانات مؤقتة للمستخدم
    users[user_id] = {}
    logger.info(f"User {user_id} started the bot.")

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = update.message.text.strip()

    # التحقق من وجود المستخدم في القاموس (إذا لم يبدأ بـ /start)
    if user_id not in users:
        await update.message.reply_text("❌ لم تبدأ المحادثة بعد. أرسل /start")
        return

    user_data = users[user_id]

    # ---- 1️⃣ استقبال رقم الهاتف ----
    if "phone" not in user_data:
        user_data["phone"] = text
        try:
            # إنشاء عميل Telethon جديد
            client = TelegramClient(StringSession(), API_ID, API_HASH)
            await client.connect()
            # إرسال رمز التحقق
            await client.send_code_request(text)
            user_data["client"] = client
            await update.message.reply_text("📩 تم إرسال الرمز. أرسله الآن:")
            logger.info(f"User {user_id}: code request sent.")
        except PhoneNumberInvalidError:
            await update.message.reply_text("❌ رقم الهاتف غير صالح. تأكد من الصيغة: + الدولي ثم الرقم")
            users.pop(user_id, None)
        except Exception as e:
            logger.exception(f"User {user_id}: error in phone step")
            await update.message.reply_text(f"❌ حدث خطأ: {str(e)}")
            # تنظيف
            if "client" in user_data:
                await user_data["client"].disconnect()
            users.pop(user_id, None)
        return

    # ---- 2️⃣ استقبال رمز التحقق ----
    if "code" not in user_data and not user_data.get("need_password"):
        user_data["code"] = text
        client = user_data["client"]
        try:
            await client.sign_in(user_data["phone"], text)
        except SessionPasswordNeededError:
            # الحساب محمي بكلمة مرور
            user_data["need_password"] = True
            await update.message.reply_text("🔐 هذا الحساب مفعل بالتحقق بخطوتين.\nأرسل كلمة المرور:")
            return
        except PhoneCodeInvalidError:
            await update.message.reply_text("❌ رمز التحقق غير صحيح. حاول مجدداً:")
            # إعادة المحاولة: نسمح للمستخدم بإرسال رمز جديد (لا نمسح البيانات)
            return
        except Exception as e:
            logger.exception(f"User {user_id}: error in code step")
            await update.message.reply_text(f"❌ حدث خطأ: {str(e)}")
            await client.disconnect()
            users.pop(user_id, None)
            return

        # إذا وصلنا هنا، تم تسجيل الدخول بنجاح (بدون كلمة مرور)
        string_session = client.session.save()
        await update.message.reply_text(
            f"✅ **StringSession الخاصة بك:**\n\n`{string_session}`",
            parse_mode="Markdown"
        )
        await client.disconnect()
        users.pop(user_id, None)
        logger.info(f"User {user_id}: session generated successfully.")
        return

    # ---- 3️⃣ استقبال كلمة المرور (إذا مطلوبة) ----
    if user_data.get("need_password"):
        client = user_data["client"]
        try:
            await client.sign_in(password=text)
        except Exception as e:
            logger.exception(f"User {user_id}: error in password step")
            await update.message.reply_text(f"❌ كلمة المرور غير صحيحة: {str(e)}")
            # يمكن للمستخدم إعادة المحاولة، لا نمسح البيانات
            return

        # نجاح تسجيل الدخول بكلمة المرور
        string_session = client.session.save()
        await update.message.reply_text(
            f"✅ **StringSession الخاصة بك:**\n\n`{string_session}`",
            parse_mode="Markdown"
        )
        await client.disconnect()
        users.pop(user_id, None)
        logger.info(f"User {user_id}: session generated successfully (2FA).")
        return

    # إذا وصلنا هنا، المستخدم في حالة غير معروفة (نعيد تعيين)
    await update.message.reply_text("⚠️ حدث خطأ في المحادثة. أرسل /start من جديد.")
    if "client" in user_data:
        await user_data["client"].disconnect()
    users.pop(user_id, None)

async def run_bot():
    """تشغيل البوت مع Polling"""
    # بناء التطبيق
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))

    logger.info("🚀 البوت بدأ العمل...")
    # بدء Polling
    await app.run_polling()

def start_bot_thread():
    """تشغيل حلقة asyncio في خيط منفصل"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(run_bot())
    except Exception as e:
        logger.exception("Error in bot thread")
    finally:
        loop.close()

# ================== تطبيق Flask (لصحة Render) ==================
flask_app = Flask(__name__)

@flask_app.route('/')
def index():
    return "✅ Bot is running!"

@flask_app.route('/health')
def health():
    return "OK", 200

# ================== نقطة الدخول الرئيسية ==================
if __name__ == "__main__":
    # تشغيل البوت في خلفية
    bot_thread = threading.Thread(target=start_bot_thread, daemon=True)
    bot_thread.start()
    logger.info("📡 بدء خادم Flask...")
    # تشغيل Flask باستخدام Gunicorn (سيتم استدعاؤه من خلال Gunicorn خارجياً)
    # لكن إذا شغّلنا الملف مباشرة، نستخدم run() ولكننا سنعتمد على Gunicorn في الإنتاج.
    # هنا سنترك Flask يعمل على المنفذ المحدد، لكن مع تحذير بعدم استخدامه في الإنتاج.
    # في بيئة Render، سنستخدم Gunicorn كـ entrypoint.
    flask_app.run(host="0.0.0.0", port=PORT, debug=False)
