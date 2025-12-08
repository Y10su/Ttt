<!doctype html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>أروى — سلاف — مريم</title>
  <style>
    :root{--bg:#f6f8fb;--card:#ffffff;--accent:#0b79d0;--muted:#6b7280}
    *{box-sizing:border-box;font-family: 'Segoe UI', Tahoma, Arial, sans-serif}
    body{margin:0;background:var(--bg);color:#0b1220;}
    header{background:linear-gradient(90deg,#0b79d0, #0762a0);color:white;padding:36px 20px}
    .container{max-width:1000px;margin:20px auto;padding:0 16px}
    .brand{display:flex;align-items:center;gap:12px}
    .logo{width:64px;height:64px;border-radius:12px;background:white;color:var(--accent);display:flex;align-items:center;justify-content:center;font-weight:700}
    h1{margin:0;font-size:28px}
    p.lead{margin:8px 0 0;opacity:.95}

    nav{margin-top:18px;display:flex;gap:8px;flex-wrap:wrap}
    nav a{background:rgba(255,255,255,.12);padding:8px 12px;border-radius:10px;color:white;text-decoration:none;font-weight:600}

    .grid{display:grid;grid-template-columns:1fr 320px;gap:20px;margin-top:22px}
    .card{background:var(--card);padding:18px;border-radius:14px;box-shadow:0 6px 18px rgba(11,17,32,.06)}
    .section-title{display:flex;justify-content:space-between;align-items:center;margin-bottom:12px}
    h2{margin:0;font-size:18px}
    .muted{color:var(--muted);font-size:14px}

    .team-list{display:flex;flex-direction:column;gap:10px}
    .member{display:flex;gap:12px;align-items:center}
    .avatar{width:48px;height:48px;border-radius:10px;background:linear-gradient(180deg,#ffd670,#ffb86b);display:grid;place-items:center;font-weight:700}
    
    .contributors-list {margin-top: 15px;}
    .contributor {border: 1px solid #e5e7eb; border-radius: 10px; padding: 15px; margin-bottom: 15px;}
    .contributor h3 {margin-top: 0; color: #0b79d0;}
    .contributor ul {padding-right: 20px;}
    .contributor li {margin-bottom: 5px;}
    
    .ideas-grid {display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 15px;}
    .idea-card {background: #f0f7ff; padding: 12px; border-radius: 8px; border-right: 3px solid #0b79d0;}
    
    .questions-list {margin-top: 15px;}
    .question {background: #f9fafb; padding: 12px; border-radius: 8px; margin-bottom: 10px; border-right: 2px solid #e5e7eb;}
    .question strong {color: #0b79d0;}
    
    .image-container {width: 100%; margin: 20px 0;}
    .responsive-img {width: 100%; height: auto; border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);}
    .image-grid {display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin: 15px 0;}
    .image-caption {text-align: center; color: var(--muted); font-size: 14px; margin-top: 5px;}
    
    footer{margin:30px 0 60px;text-align:center;color:var(--muted)}

    @media (max-width:920px){
      .grid{grid-template-columns:1fr}
      .ideas-grid {grid-template-columns: 1fr;}
      .image-grid {grid-template-columns: 1fr;}
    }
  </style>
</head>
<body>
  <header>
    <div class="container">
      <div class="brand">
        <div class="logo">أ</div>
        <div>
          <h1>موقع: أروى — سلاف — مريم</h1>
          <p class="lead">صفحة تعريفية عن مشروع "مدن المستقبل"، تحتوي على الرؤية، أعضاء الفريق، وأهم الأفكار.</p>
        </div>
      </div>

      <nav>
        <a href="#about">عن المشروع</a>
        <a href="#contributors">المساهمون</a>
        <a href="#ideas">الأفكار الرئيسية</a>
        <a href="#questions">أسئلة شائعة</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <div class="image-container">
      <img src="https://images.unsplash.com/photo-1486406146926-c627a92ad1ab" 
           alt="مدينة ذكية مستقبلية" 
           class="responsive-img">
      <div class="image-caption">مدينة ذكية مستقبلية</div>
    </div>

    <div class="grid">
      <section class="card">
        <div class="section-title">
          <h2 id="about">عن مشروع "مدن المستقبل"</h2>
          <span class="muted">رؤية مبسطة</span>
        </div>
        <p>نقدم في هذا المشروع عرضًا مبسطًا عن مفهوم المدن الذكية: كيف تدمج التكنولوجيا والبيئة والإنسان بطريقة مستدامة لتسهيل حياة المواطنين وتحسين إدارة الموارد.</p>

        <h3>أهداف المشروع</h3>
        <ul>
          <li>استكشاف مفاهيم الاستدامة في التخطيط العمراني</li>
          <li>التعرف على دور الذكاء الاصطناعي وإنترنت الأشياء في تحسين الخدمات</li>
          <li>عرض أمثلة على مساهمين بارزين في مجال المدن الذكية</li>
          <li>تقديم رؤية مستقبلية للمدن الذكية في المملكة والعالم</li>
        </ul>
        
        <div style="margin: 20px 0;">
          <img src="https://images.unsplash.com/photo-1466611653911-95081537e5b7" 
               alt="الطاقة الشمسية في المدن الذكية" 
               style="width:100%; height:200px; object-fit:cover; border-radius:8px;">
          <div class="image-caption">الطاقة الشمسية في المدن الذكية</div>
        </div>
      </section>

      <section class="card">
        <div class="section-title">
          <h2 id="team">فريق المشروع</h2>
          <span class="muted">شعبة ٢</span>
        </div>
        <div class="team-list">
          <div class="member">
            <div class="avatar">أ</div>
            <div>
              <strong>أروى</strong>
              <p>تصميم وتنفيذ المشروع</p>
            </div>
          </div>
          <div class="member">
            <div class="avatar">س</div>
            <div>
              <strong>سلاف مرزوق</strong>
              <p>بحث وجمع المعلومات</p>
            </div>
          </div>
          <div class="member">
            <div class="avatar">م</div>
            <div>
              <strong>مريم أحمد</strong>
              <p>تحليل وتنسيق المحتوى</p>
            </div>
          </div>
        </div>
        
        <div style="margin-top:20px; text-align:center;">
          <img src="https://images.unsplash.com/photo-1552664730-d307ca884978" 
               alt="فريق العمل" 
               style="width:100%; height:150px; object-fit:cover; border-radius:8px;">
          <div class="image-caption">عمل جماعي لبناء المستقبل</div>
        </div>
      </section>
    </div>

    <div class="card" style="margin-top: 20px;">
      <div class="section-title">
        <h2 id="contributors">المساهمون في تطوير المدن الذكية</h2>
        <span class="muted">شخصيات مؤثرة</span>
      </div>
      
      <div class="contributors-list">
        <div class="contributor">
          <h3>محمد العسيري</h3>
          
          <div style="float:left; margin-left:15px; margin-bottom:15px;">
            <img src="https://images.unsplash.com/photo-1560250097-0b93528c311a" 
                 alt="رمزية لشخصية تقنية" 
                 style="width:120px; height:120px; border-radius:50%; object-fit:cover;">
          </div>
          
          <p>شخصية سعودية بارزة في مجال التحول الرقمي وتطوير المدن الذكية. ساهم في رفع كفاءة المدن السعودية باستخدام التقنيات الحديثة مثل الذكاء الاصطناعي وإنترنت الأشياء وتحليل البيانات الضخمة.</p>
          <p><strong>أبرز مساهماته:</strong></p>
          <ul>
            <li>تطوير مدينة الخبر وجعلها من المدن المتقدمة في مؤشر المدن الذكية العالمي</li>
            <li>الدعم للاستدامة الرقمية ودمج التكنولوجيا في خدمة الإنسان</li>
          </ul>
        </div>
        
        <div class="contributor">
          <h3>كلاوس مارتن شواب</h3>
          
          <div style="float:left; margin-left:15px; margin-bottom:15px;">
            <img src="https://images.unsplash.com/photo-1582750433449-648ed127bb54" 
                 alt="رمزية لشخصية قيادية" 
                 style="width:120px; height:120px; border-radius:50%; object-fit:cover;">
          </div>
          
          <p>مهندس ميكانيكي واقتصادي ألماني، مؤسس ورئيس المنتدى الاقتصادي العالمي سابقاً.</p>
          <p><strong>أبرز مساهماته:</strong></p>
          <ul>
            <li>التركيز على التعاون بين القطاع العام والخاص والمجتمع المدني</li>
            <li>الدعوة لتصميم مدن تقلل الانبعاثات الكربونية وتستخدم الطاقة المتجددة</li>
          </ul>
        </div>
      </div>
    </div>

    <div class="card" style="margin-top: 20px;">
      <div class="section-title">
        <h2 id="ideas">الأفكار الرئيسية</h2>
        <span class="muted">رؤى وتطورات</span>
      </div>
      
      <div class="image-grid">
        <div>
          <img src="https://images.unsplash.com/photo-1542601906990-b4d3fb778b09" 
               alt="مدينة خضراء" 
               style="width:100%; height:150px; object-fit:cover; border-radius:8px;">
          <div class="image-caption">المدن الخضراء المستدامة</div>
        </div>
        <div>
          <img src="https://images.unsplash.com/photo-1558494949-ef010cbdcc31" 
               alt="تقنيات ذكية" 
               style="width:100%; height:150px; object-fit:cover; border-radius:8px;">
          <div class="image-caption">إنترنت الأشياء والأجهزة الذكية</div>
        </div>
      </div>
      
      <h3>أفكار محمد العسيري:</h3>
      <div class="ideas-grid">
        <div class="idea-card">المدن الذكية تقوم على الاستدامة والمواطنة الرقمية</div>
        <div class="idea-card">ضرورة إشراك المجتمع في التحول الذكي</div>
        <div class="idea-card">استخدام التقنيات لخدمة الإنسان لا العكس</div>
        <div class="idea-card">تعزيز الابتكار في تصميم المدن المستقبلية</div>
      </div>
      
      <h3 style="margin-top: 20px;">أفكار كلاوس مارتن شواب:</h3>
      <div class="ideas-grid">
        <div class="idea-card">مدن مستدامة وصديقة للبيئة باستخدام الطاقة المتجددة</div>
        <div class="idea-card">المباني الخضراء مع عزل حراري وتقنيات لتقليل استهلاك الطاقة</div>
        <div class="idea-card">دعم الشركات الناشئة والمبتكرين لتطوير حلول ذكية</div>
        <div class="idea-card">تسهيل التجارة والخدمات الرقمية لزيادة الإنتاجية</div>
      </div>
    </div>

    <div class="card" style="margin-top: 20px;">
      <div class="section-title">
        <h2 id="questions">أسئلة شائعة</h2>
        <span class="muted">استفسارات مهمة</span>
      </div>
      
      <div style="margin-bottom:20px;">
        <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71" 
             alt="تحليل البيانات والذكاء الاصطناعي" 
             style="width:100%; height:200px; object-fit:cover; border-radius:8px;">
        <div class="image-caption">الذكاء الاصطناعي وتحليل البيانات في المدن الذكية</div>
      </div>
      
      <div class="questions-list">
        <div class="question">
          <strong>ما العلاقة بين المدن الذكية والذكاء الاصطناعي؟</strong>
          <p>علاقة وثيقة جداً، لأن الذكاء الاصطناعي يُعتبر أحد الأسس الرئيسية التي تقوم عليها فكرة المدن المستقبلية.</p>
        </div>
        
        <div class="question">
          <strong>كيف تسهم الأبحاث في المدن الأذكى بأمان أفضل؟</strong>
          <p>الأبحاث التي تطوّر بروتوكولات أمان أو خوارزميات تشفير قوية تُساهم في الحفاظ على سلامة البنية التحتية وتجنُّب الهجمات التي قد تؤثّر على الخدمات الحيوية.</p>
        </div>
        
        <div class="question">
          <strong>ما أبرز التقنيات المستخدمة في أبحاث المدن الذكية؟</strong>
          <p>الذكاء الاصطناعي يطبق في أنظمة المرور الذكي، الأمن، إدارة الطاقة، وخدمة المواطنين.</p>
        </div>
        
        <div class="question">
          <strong>ما التحديات المستقبلية التي تواجه المدن الذكية؟</strong>
          <p>ارتفاع التكلفة: بناء مدن ذكية يحتاج إلى استثمارات ضخمة في التكنولوجيا والبنية التحتية.</p>
        </div>
        
        <div class="question">
          <strong>ما أهمية مشاركة المواطنين في صنع القرار داخل المدينة الذكية؟</strong>
          <p>أهمية كبيرة، لأنها تجعل المدينة أكثر توافقًا مع احتياجات الناس وفاعلية في إدارة الموارد.</p>
        </div>
      </div>
    </div>
    
    <div class="card" style="margin-top: 20px; background: #f0f7ff;">
      <h3 style="color: #0b79d0; margin-top: 0;">رؤيتنا للمستقبل</h3>
      <p>نؤمن بأن المدن الذكية ليست فقط تقنيات، بل أسلوب حياة متكامل يجمع بين التكنولوجيا والإنسان والبيئة. يجب أن يكون هناك توازن بين التطور التقني والحفاظ على البيئة، حيث تكون المدن مترابطة رقمياً مع الحفاظ على المساحات الخضراء.</p>
      <p>ندعو إلى التعاون بين القطاعات الحكومية والخاصة لتطوير مدن مستدامة قادرة على التكيّف مع المستقبل.</p>
    </div>
  </main>

  <footer>
    <div class="container">
      <p>مشروع "مدن المستقبل" - شعبة ٢</p>
      <p>أروى - سلاف مرزوق - مريم أحمد</p>
      <p style="margin-top: 10px; font-size: 14px;">www.reallygreatsite.com | شكرًا لكم</p>
    </div>
  </footer>
</body>
</html>
