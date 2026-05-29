import streamlit as st

# 1. إعدادات الصفحة الأساسية والهوية البصرية المستقرة
st.set_page_config(
    page_title="برنامج الأمانة الثقافية - ملتقى السودان بجدة",
    page_icon="🇸🇩",
    layout="wide"
)

# 2. حقن CSS شامل لفرض الاتجاه والمحاذاة نحو اليمين بالكامل لكل النصوص والعناوين
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght=400;600;700;800&display=swap');
    
    [data-testid="collapsedControl"] {
        display: none !important;
    }
    
    html, body, [data-testid="stAppViewContainer"], .main, .block-container {
        font-family: 'Cairo', sans-serif !important;
        background-color: #F4F6F9 !important;
        color: #1A365D !important;
        direction: rtl !important;
        text-align: right !important;
    }
    
    h1, h2, h3, h4, h5, h6, p, span, li, ul {
        text-align: right !important;
        direction: rtl !important;
    }
    
    .cosmic-header {
        background: linear-gradient(135deg, #1A365D 0%, #0F1E36 100%);
        padding: 25px 30px;
        border-radius: 12px;
        color: white !important;
        box-shadow: 0 10px 30px rgba(26, 54, 93, 0.15);
        margin-bottom: 30px;
        border-right: 6px solid #C5A059;
        text-align: right !important;
        direction: rtl !important;
    }
    .cosmic-header h1 {
        color: #FFFDF5 !important;
        font-weight: 800 !important;
        font-size: 26px !important;
        margin: 0 0 8px 0 !important;
        line-height: 1.4 !important;
    }
    
    .sudan-flag-line {
        height: 5px;
        width: 100%;
        background: linear-gradient(to left, #D21034 33.3%, #FFFFFF 33.3%, #FFFFFF 66.6%, #007229 66.6%);
        border-radius: 10px;
        margin-top: 15px;
    }

    .luxury-card {
        background-color: #FFFFFF !important;
        border: 1px solid #E2E8F0 !important;
        border-right: 6px solid #1A365D !important;
        padding: 22px 25px !important;
        border-radius: 10px !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.04) !important;
        margin-bottom: 25px !important;
        color: #1A365D !important;
        text-align: right !important;
        direction: rtl !important;
    }
    .luxury-card h3, .luxury-card h4 {
        color: #1A365D !important;
        font-weight: 700 !important;
        margin-top: 0 !important;
        margin-bottom: 12px !important;
        font-size: 19px !important;
    }
    .luxury-card p {
        color: #334155 !important;
        font-size: 15.5px !important;
        line-height: 1.8 !important;
        margin-bottom: 10px !important;
    }
    .luxury-card ul {
        padding-right: 20px !important;
        padding-left: 0 !important;
        margin: 0 !important;
        list-style-type: square !important;
    }
    .luxury-card li {
        color: #334155 !important;
        font-size: 15px !important;
        line-height: 1.8 !important;
        margin-bottom: 8px !important;
    }
    
    .gold-luxury-card {
        background-color: #FFFDF5 !important;
        border: 1px solid #FEF3C7 !important;
        border-right: 6px solid #C5A059 !important;
        padding: 20px !important;
        border-radius: 10px !important;
        box-shadow: 0 4px 15px rgba(197, 160, 89, 0.06) !important;
        margin-bottom: 25px !important;
        text-align: right !important;
        direction: rtl !important;
    }
    
    .section-title {
        color: #1A365D !important;
        font-weight: 800 !important;
        border-bottom: 2px solid #C5A059 !important;
        padding-bottom: 8px !important;
        margin-top: 40px !important;
        margin-bottom: 20px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. الهيدر الموحد الفاخر للهوية الرسمية (ملتقى السودان)
st.markdown("""
    <div class='cosmic-header'>
        <h1>لجنة تسيير الجالية السودانية بجدة (ملتقى السودان)</h1>
        <p style='margin: 0; font-size: 16px; color: #CBD5E1; font-weight: bold;'>برنامج الأمانة الثقافية — الرؤية الإستراتيجية والمناشط للمرحلة القادمة</p>
        <div class='sudan-flag-line'></div>
    </div>
    """, unsafe_allow_html=True)

# --- 1. المقدمة والمنهجية الإستراتيجية ---
st.markdown("<h2 class='section-title'>1. المقدمة التعريفية والمنهجية الإستراتيجية</h2>", unsafe_allow_html=True)
st.markdown("""
<div class='luxury-card' style='border-right-color: #C5A059;'>
    <p style='font-size: 16.5px; font-weight: bold; color: #1A365D;'>السادة رئيس وأعضاء لجنة تسيير الجالية السودانية بجدة : الموقرين</p>
    <p>يتقدم المكتب الثقافي بلجنة التسيير بخطة عمل رسمية للفترة القادمة ، تتضمن أنشطة معرفية فنية وتراثية وتهدف إلى إبراز طاقات المجتمع وتطوير مهاراته من خلال تنفيذ برنامج ثقافي احترافي ناجح يُلبي تطلعات المرحلة الانتقالية.</p>
    <p>إن المنهجية الإستراتيجية لهذا البرنامج تقوم على تحديد الأهداف والجمهور المستهدف أولاً، ومن ثمَّ تصميم المناشط والفعاليات وفقاً للغايات الأساسية للجنة التسيير والتي تنحصر في التالي :</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<h3 style='color: #1A365D; font-weight: 700; margin-bottom: 15px;'>🎯 الغايات الأساسية للبرنامج:</h3>", unsafe_allow_html=True)
st.markdown("""
<div class='luxury-card'>
    <ul>
        <li><b>تعزيز المعرفة ونشرها</b> بين أبناء الجالية السودانية بجدة.</li>
        <li><b>إبراز التراث الثقافي السوداني الأصيل</b> وربط الجيل الناشئ بوطنه.</li>
        <li><b>صقل المواهب الوطنية</b> ودعم رواد الأعمال والمبتكرين في شتى المجالات.</li>
        <li><b>تجميع الكيانات والروابط</b> تحت مظلة مؤسسية متناغمة تمهيداً لقيام الجالية.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# --- 2. دراسة الفئات المستهدفة وتحليل الواقع ---
st.markdown("<h2 class='section-title'>2. دراسة الفئات المستهدفة وتحليل الواقع</h2>", unsafe_allow_html=True)
st.markdown("""
<div class='luxury-card'>
    <h4>1. الشباب والخريجين</h4>
    <p>لتمكينهم وتوجيه طاقاتهم المعرفية والمهنية لصناعة المستقبل المشرق.</p>
</div>
<div class='luxury-card'>
    <h4>2. الأطفال والناشئة</h4>
    <p>عبر مناشط مخصصة لبناء الهوية الوطنية وحمايتها وغرس القيم السودانية الأصيلة.</p>
</div>
<div class='luxury-card'>
    <h4>3. الأسر والنساء</h4>
    <p>فعاليات تدمج بين التكافل الاجتماعي والتطوير الاقتصادي للأسر المنتجة.</p>
</div>
<div class='luxury-card'>
    <h4>4. الكيانات والروابط الثقافية</h4>
    <p>الروابط الثقافية والأدبية كشركاء أساسيين في بناء النسيج الاجتماعي الموحد.</p>
</div>
""", unsafe_allow_html=True)

# --- 3. المسارات الإستراتيجية للبرنامج ---
st.markdown("<h2 class='section-title'>3. المسارات الإستراتيجية للبرنامج الثقافي</h2>", unsafe_allow_html=True)
st.markdown("""
<div class='luxury-card'>
    <h4>📚 أولاً: مسار الندوات واللقاءات الحوارية والثقافية</h4>
    <p>يهدف لترسيخ الوعي وتوفير منصات رصينة للنقاش الفكري البنّاء والتبادل المعرفي بين قادة الفكر والجالية.</p>
</div>
<div class='luxury-card'>
    <h4>⚙️ ثانياً: مسار الورش التدريبية التفاعلية</h4>
    <p>يركز بالكامل على بناء القدرات الحقيقية، وصقل المعارف، ونقل الخبرات المهنية والعملية لتأهيل الكوادر والشباب.</p>
</div>
<div class='luxury-card'>
    <h4>🖼️ ثالثاً: مسار المعارض الفنية والتراثية</h4>
    <p>يعمل على توثيق الهوية السودانية وإبراز التنوع والإبداع البصري والموسيقي، وفقاً لأنظمة ولوائح الدولة المضيفة.</p>
</div>
""", unsafe_allow_html=True)

# --- 4. المشروعات والفعاليات التنفيذية المقترحة ---
st.markdown("<h2 class='section-title'>4. المشروعات والفعاليات التنفيذية المقترحة</h2>", unsafe_allow_html=True)
st.markdown("""
<div class='luxury-card'>
    <h3 style='color: #C5A059;'>أ. حزمة الصالون الأدبي وملتقيات الإبداع</h3>
    <p><b>• المسابقات الأدبية:</b> إطلاق مسابقات رسمية في مجالات كتابة وتأليف المقالات، والقصص القصيرة، والرواية، والشعر، لتشجيع الإبداع وحصر الطاقات الأدبية في المهجر.</p>
    <p><b>• المناشط الفنية والتشكيلية:</b> تنظيم معارض ومعاهد متخصصة لتعليم وصقل المعارف الفنية في مجالات الرسم، التصوير الفوتوغرافي، الفنون البصرية، والخط العربي بجدة مع إقامة معارض دورية لعرض أعمال المبدعين.</p>
    <p><b>• معارض المهرجانات والكتاب:</b> تنظيم صالونات دورية للقراءة وزيارة وتنظيم معارض مصغرة للكتاب، لتشجيع القراءة ونشر الوعي الثقافي بين الأسر والشباب.</p>
</div>

<div class='luxury-card'>
    <h3 style='color: #C5A059;'>ب. حزمة ملتقى التراث والفنون الأدائية (مهرجان الهوية)</h3>
    <p><b>• المهرجانات التراثية الحية:</b> إقامة ملتقيات تراثية مغلقة تشمل عروضاً للفرق الموسيقية التراثية والرقص الشعبي الممثل لكافة أقاليم السودان، لتقديم لوحة وطنية متكاملة تبرز التنوع كعنصر وحدة.</p>
    <p><b>• أسواق الحرف اليدوية والطهي:</b> تنظيم أسواق ومعارض مصاحبة للحرف اليدوية السودانية، المشغولات الجلدية والخزف، يصاحبها استعراض حي للمأكولات التقليدية لربط الوجدان والأسرة بالثقافة المحلية.</p>
    <p><b>• ورش العمل التعليمية للتقاليد:</b> تنظيم ورش سريعة وموجهة للأطفال تسلط الضوء على عادات وتقاليد المجتمع السوداني في المناسبات والأعياد لترسيخ قيم التكافل الأصيلة.</p>
</div>

<div class='luxury-card'>
    <h3 style='color: #C5A059;'>ج. مشروع "المجمع الثقافي / النادي السوداني"</h3>
    <p><b>• فعاليات الأطفال والناشئة:</b> تخصيص أيام ترفيهية ومعرفية دورية وممنهجة للأطفال، تشمل مسرح الطفل والألعاب التعليمية والمسابقات الثقافية لتعزيز الانتماء للوطن بأساليب محببة وجاذبة وعصرية.</p>
    <p><b>• المحاضرات وجلسات النقاش:</b> عقد محاضرات دورية مستمرة تستضيف قادة الرأي والفكر لمناقشة آليات تطوير العمل العام، وتوفيق أوضاع الكيانات، وتوطيد العلاقات الاجتماعية الإيجابية بين أفراد الجالية.</p>
</div>
""", unsafe_allow_html=True)

# --- 5. منصة "مَجَرَّة" للكفاءات (المشروع الأساسي) ---
st.markdown("<h2 class='section-title'>5. المشروع النوعي المبتكر: منصة \"مَجَرَّة\" للكفاءات</h2>", unsafe_allow_html=True)
st.markdown("""
<div class='gold-luxury-card'>
    <p style='font-size: 16px; font-style: italic; text-align: center; margin: 0; color: #C5A059; font-weight: bold;'>
    "مواكبة لأحدث النظم العالمية في نقل المعرفة، تم ابتكار منصة 'مَجَرَّة' لتكون الحاضنة المعرفية والتنموية الكبرى لأبناء الوطن في المهجر."
    </p>
</div>

<div class='luxury-card'>
    <h4>⚙️ الآلية وضوابط التقديم الصارمة:</h4>
    <p>• <b>آلية التنفيذ والتقديم:</b> يُجهز مسرح القاعة بأحدث التقنيات البصرية والصوتية المناسبة للعروض التقديمية الاحترافية والملهمة.</p>
    <p>• <b>المتحدثون والعلماء:</b> يتم استضافة 6 شخصيات من أرفع الكفاءات السودانية بالمنطقة الغربية (في مجالات: الأكاديمية - الهندسة – التقنية – الطب – الإدارة - وريادة الأعمال).</p>
    <p>• <b>ضوابط المنصة الزمنية:</b> يُمنح كل متحدث <b>20 دقيقة محددة وصارمة</b>، يستعرض فيها "خلاصة تجربته المهنية والعلمية" ويقدم حلولاً وتوصيات عملية للشباب والخريجين بعيداً عن السرد الإنشائي التقليدي.</p>
</div>

<div class='luxury-card'>
    <h4>🚀 المعرض المهني المصاحب (دعم رواد الأعمال):</h4>
    <p>على هامش المنصة يُقام معرض متكامل لرواد الأعمال الشباب وأصحاب المشاريع الناشئة والابتكارات والمهن الحرة بهدف إتاحة فرص التشبيك والتواصل، وترسيخ دور الجالية كحاضنة اقتصادية ومعرفية ملموسة.</p>
</div>
""", unsafe_allow_html=True)

# --- 6. آليات التفعيل والحوكمة المستدامة ---
st.markdown("<h2 class='section-title'>6. آليات التفعيل ( الحوكمة والضبط الإداري المرجعي )</h2>", unsafe_allow_html=True)
st.markdown("""
<div class='luxury-card'>
    <h4>🎟️ 1. بروتوكول التسليم والديمومة المؤسسية (الاستمرارية)</h4>
    <p>تُعتمد هذه الخطة كأصل وثائقي أساسي للأمانة الثقافية في "لجنة تيسير الجالية السودانية بجدة مايو 2026"، وتلتزم الأمانة الحالية بتسليم كافة ملفاتها التقنية والبيانات المستخرجة من المنصات الرقمية إلى رئيس لجنة التسيير، لتبدأ الإدارات المتعاقبة من حيث انتهت هذه الخطة دون الحاجة لتأسيس حراك من الصفر.</p>
</div>

<div class='luxury-card'>
    <h4>📥 2. صندوق "صوت المواطن" للشفافية</h4>
    <p>تفعيل صندوق مقترحات رسمي وموثق يتنقل بين كافة المشروعات والفعاليات الحضرية، ويتيح لأبناء الجالية تقديم أفكارهم ورؤاهم المكتوبة مباشرة إلى لجنة التسيير، إيماناً بمبدأ الشفافية والمشاركة الجماعية في صنع القرار.</p>
</div>

<div class='luxury-card'>
    <h4>🎫 3. بطاقة العضوية الثقافية (المتابعة وقياس الأثر)</h4>
    <p>إصدار بطاقات حضور رمزية تسلسلية للمشاركين تسهم في قياس مدى التزام وتفاعل العضوية، وتمنح ميزات تفضيلية وحصرية للملتزمين بالمسارات التدريبية في الفعاليات الختامية.</p>
</div>

<div class='luxury-card'>
    <h4>⚖️ 4. الحوكمة والتنفيذ المؤسسي</h4>
    <p>تخضع كافة الفعاليات والمشروعات لإشراف مباشر من الأمانة الثقافية بلجنة التسيير، وبالتنسيق الكامل والمنظم مع رئيس وأعضاء لجنة التسيير والقنصلية العامة لجمهورية السودان بجدة لضمان الالتزام المطلق بالضوابط والأنظمة المتبعة في الدولة المضيفة.</p>
</div>
""", unsafe_allow_html=True)

# --- 7. الخاتمة والتوصيات المعتمدة ---
st.markdown("<h2 class='section-title'>7. الخاتمة والتوصيات المعتمدة</h2>", unsafe_allow_html=True)
st.markdown("""
<div class='luxury-card' style='border-right-color: #C5A059;'>
    <p>إن هذا البرنامج الثقافي المتكامل بمساراتها الواضحة وأهدافه المحددة ومستهدفاته المدروسة، يمثل الركيزة الأساسية واللبنة الأولى لصياغة مستقبل جالية نموذجية ومتلاحمة ورائدة تعكس الوجه المشرق للسودان وأبنائه في المملكة العربية السعودية.</p>
    <p>تتقدم الأمانة الثقافية بلجنة تسيير الجالية السودانية بجدة بهذا المقترح الإستراتيجي لسعادتكم للمناقشة والإجازة وبدء التنفيذ الميداني وحفظه كإرث تنظيمي دائم.</p>
    <p style='text-align: center; font-weight: bold; font-size: 16px; margin-top: 25px; color: #1A365D;'>سائلين الله التوفيق والسداد لما فيه خير العباد والبلاد.</p>
    <p style='text-align: center; font-weight: bold; color: #C5A059; margin-top: 10px;'>،، وتفضلوا بقبول وافر الشكر والتقدير والإمتنان ،،</p>
</div>

<div style='text-align: center; margin-top: 35px; font-weight: bold; color: #1A365D;'>
    <p style='margin:0; font-size: 16px;'>أمانة الثقافة بلجنة تسيير الجالية السودانية بجدة</p>
    <p style='color: #C5A059; margin: 8px 0; font-size: 18px;'>بابكر عبدالله &nbsp;&nbsp;|&nbsp;&nbsp; وليد البليل</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br><hr><p style='text-align: center; color: #64748B; font-size: 13px;'>أمانة الثقافة بلجنة تسيير الجالية السودانية بجدة • مايو 2026م</p>", unsafe_allow_html=True)
