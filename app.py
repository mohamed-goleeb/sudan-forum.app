import streamlit as st

# 1. إعدادات الصفحة الأساسية والهوية البصرية الرسمية
st.set_page_config(
    page_title="الخطة الثقافية الشاملة",
    page_icon="🇸🇩",
    layout="wide"
)

# 2. حقن CSS العام لتهيئة المتصفح على الخط والمحاذاة الصحيحة
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap');
    
    html, body, [data-testid="stAppViewContainer"], .main, .block-container {
        font-family: 'Cairo', sans-serif !important;
        background-color: #F4F6F9 !important;
        color: #1A365D !important;
        direction: rtl !important;
        text-align: right !important;
    }
    
    h1, h2, h3, h4, h5, h6, p, span, li, ul, div {
        text-align: right !important;
        direction: rtl !important;
    }
    
    /* تنسيقات الهيدر والكروت والكداول الثابتة */
    .main-header {
        background: linear-gradient(135deg, #1A365D 0%, #0F1E36 100%);
        padding: 35px;
        border-radius: 12px;
        margin-bottom: 30px;
        border-right: 6px solid #C5A059;
    }
    .main-header p, .main-header h1 {
        color: #C5A059 !important; /* نصوص الهيدر باللون الذهبي بالكامل */
        font-size: 28px !important;
        font-weight: 800 !important;
        margin: 15px 0 !important;
        line-height: 1.6 !important;
        text-align: right !important;
    }
    
    .luxury-card {
        background-color: #FFFFFF !important;
        border: 1px solid #E2E8F0 !important;
        border-right: 6px solid #1A365D !important;
        padding: 25px !important;
        border-radius: 10px !important;
        margin-bottom: 25px !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.02) !important;
    }
    
    .gold-card {
        background-color: #FFFDF5 !important;
        border: 1px solid #FEF3C7 !important;
        border-right: 6px solid #C5A059 !important;
        padding: 25px !important;
        border-radius: 10px !important;
        margin-bottom: 25px !important;
    }
    
    .section-title {
        color: #1A365D !important;
        font-weight: 800 !important;
        border-bottom: 3px solid #C5A059 !important;
        padding-bottom: 8px !important;
        margin-top: 45px !important;
        margin-bottom: 25px !important;
        font-size: 24px !important;
    }
    
    .custom-table {
        width: 100%;
        border-collapse: collapse;
        margin: 20px 0;
        font-size: 15px;
        text-align: right;
        direction: rtl;
    }
    .custom-table th {
        background-color: #1A365D;
        color: white;
        padding: 12px;
        border: 1px solid #E2E8F0;
        font-weight: 700;
    }
    .custom-table td {
        padding: 12px;
        border: 1px solid #E2E8F0;
        background-color: #FFFFFF;
        color: #334155;
    }
    .custom-table tr:nth-child(even) td {
        background-color: #F8FAFC;
    }
    
    .signature-section {
        text-align: center !important;
        margin-top: 50px;
        margin-bottom: 30px;
        width: 100%;
    }
    .signature-table {
        width: 60%;
        margin: 0 auto !important;
        border: none !important;
    }
    .signature-table td {
        border: none !important;
        background: transparent !important;
        text-align: center !important;
        padding: 10px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. ديباجة الرسالة والمستهدفات العامة
st.markdown("""
<div class='main-header'>
    <p>بسم الله الرحمن الرحيم</p>
    <p>المملكة العربية السعودية - جدة</p>
    <p>لجنة تسيير الجالية السودانية بجدة</p>
    <h1>الأمانة الثقافية</h1>
    <p>التاريخ : مايو 2026م</p>
</div>

<div class='luxury-card' style='border-right-color: #C5A059;'>
    <p style='font-weight: bold; font-size: 18px;'>سعادة رئيس وأعضاء لجنة تسيير الجالية السودانية بجدة</p>
    <p style='font-weight: bold; font-size: 16px;'>السلام عليكم ورحمة الله وبركاته</p>
    <p style='font-weight: bold;'>الموقرين</p>
    <p>إيماناً بالدور الطليعي المحوري الذي تلعبه الثقافة في تعزيز التماسك المجتمعي وبناء جسور التواصل المعرفي بين أبناء الوطن في المهجر وتماشياً مع الرؤية التطويرية للأمانة الثقافية يسرنا أن نضع بين أيديكم الخطة الثقافية الشاملة</p>
    <p>إن القيمة التنظيمية العليا لهذه الخطة تكمن في كونها إطاراً مرجعياً مستداماً وبنية تحتية مؤسسية حيث تم تصميمها وهندستها لتكون دليلاً حاكماً وأصلاً من أصول العمل العام التي تنتقل تلقائياً لشرعنة واستدامة الحراك الثقافي لأي مجالس إدارية أو جاليات منتخبة قادمة، صوناً للمكتسبات المعرفية وضماناً لتراكم الخبرات وتواصل الأجيال دون انقطاع .</p>
    <p style='text-align: center !important; font-weight: 800; font-size: 18px; color: #C5A059; margin-top: 15px;'>تحت شعار</p>
    <p style='text-align: center !important; font-weight: 800; font-size: 22px; color: #1A365D; margin: 0;'>الثقافة تجمعنا</p>
</div>
""", unsafe_allow_html=True)

# 4. جدول الفهرس
st.markdown("<h2 class='section-title'>الفهرس</h2>", unsafe_allow_html=True)
st.markdown("""
<table class='custom-table'>
    <thead>
        <tr>
            <th>رقم القسم / الفصل</th>
            <th>عنوان المكون الهيكلي</th>
            <th>المحتوى</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>تمهيد الخطاب</td><td>ديباجة الرسالة والمستهدفات العامة</td><td>إعلان المرجعية المؤسسية المستدامة</td></tr>
        <tr><td>1</td><td>الملخص التنفيذي</td><td>مبررات الخطة الاستدامة ومؤشرات النجاح</td></tr>
        <tr><td>2</td><td>الخلفية الخاصة بالخطة</td><td>دور الثقافة في التماسك المجتمعي بالمهجر</td></tr>
        <tr><td>3</td><td>تحليل الواقع الثقافي</td><td>دراسة الوضع الراهن والفرص بالمنطقة الغربية</td></tr>
        <tr><td>4</td><td>تحليل ( SWOT)الرباعي</td><td>نقاط القوة والضعف والفرص والمهددات</td></tr>
        <tr><td>الفصل 5</td><td>الرؤية، الرسالة، والقيم</td><td>الإطار المرجعي الحاكم والهوية البصرية الموحدة</td></tr>
        <tr><td>6</td><td>الركائز التوجيهية الست ومساراتها التنفيذية</td><td>الأعمدة الستة مقرونة بآليات التطبيق الميداني والمنصات حية</td></tr>
        <tr><td>7</td><td>التحول الرقمي والأرشفة الثقافية</td><td>المكتبة الرقمية السودانية والأرشيف التقني</td></tr>
        <tr><td>8</td><td>الشراكات والتعاونيات والرعايات</td><td>التوأمة مع الروابط المحلية وجذب الداعمين</td></tr>
        <tr><td>9</td><td>الإعلام الثقافي وإدارة المحتوى</td><td>خطة التسويق الثقافي وصناعة المحتوى الرقمي</td></tr>
        <tr><td>10</td><td>الخطة التشغيلية السنوية</td><td>الجداول الزمنية وتوزيع المهام على مدار العام</td></tr>
        <tr><td>11</td><td>الميزانية التقديرية والحوكمة المالية</td><td>التدفقات المالية وضوابط الشفافية</td></tr>
        <tr><td>ملاحق الحوكمة</td><td>ديمومة المرجعية وآليات التفعيل</td><td>بطاقة العضوية، صوت المواطن، وبروتوكول التسليم</td></tr>
    </tbody>
</table>
""", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center !important; font-weight: 800; color: #1A365D; margin-top: 40px;'>الهيكل التفصيلي للخطة الشاملة :</h2>", unsafe_allow_html=True)

# -------------------------------------------------------------
# الفصول من 1 إلى 5
# -------------------------------------------------------------
st.markdown("<h2 class='section-title'>الفصل 1: الملخص التنفيذي</h2>", unsafe_allow_html=True)
st.markdown("<div class='luxury-card'><p>• يقدم عرضاً شاملاً ومكثفاً للخطة الثقافية، مبرراتها وأثرها التنموي المتوقع يركز الفصل على هندسة إطار مؤسسي عملي ومرن وقابل للتنفيذ الميداني الفوري مع التركيز على استخراج مخرجات ونتائج نوعية وكمية قابلة للقياس والتقييم.</p><p>• يستند هذا الإطار على مبادئ التنوع والشمولية والاستدامة مبيناً الأدوار التنفيذية آليات المتابعة والشراكات المستهدفة ومؤشرات النجاح الرئيسية لضمان تحقيق الأثر بعيد المدى .</p></div>", unsafe_allow_html=True)

st.markdown("<h2 class='section-title'>الفصل 2 الخلفية الخاصة بالخطة</h2>", unsafe_allow_html=True)
st.markdown("<div class='luxury-card'><p>تأصيل دور الثقافة كركيزة أساسية لا غنى عنها في تعزيز التماسك والتعايش المجتمعي بين مكونات الجالية في المهجر مع التركيز على صياغة بنية تحتية إدارية وثقافية تدعم هذا التوجه إجرائياً وعملياً</p></div>", unsafe_allow_html=True)

st.markdown("<h2 class='section-title'>الفصل 3 تحليل الواقع الثقافي</h2>", unsafe_allow_html=True)
st.markdown("<div class='luxury-card'><p>• دراسة وصفية وميدانية دقيقة للوضع الراهن للحراك الثقافي في المنطقة الغربية واستكشاف مكامن الفرص غير المستغلة والوقوف على التحديات الراهنة التي تواجه العمل العام وتذليلها .</p></div>", unsafe_allow_html=True)

st.markdown("<h2 class='section-title'>الفصل 4 تحليل (SWOT) الرباعي</h2>", unsafe_allow_html=True)
st.markdown("<div class='luxury-card'><p>• قراءة علمية تحليلية لواقع العمل الثقافي تحدد بشكل صارم : نقاط القوة لتنميتها، نقاط الضعف لمعالجتها وحوكمتها، الفرص المتاحة لانتهازها، والمهددات الخارجية للتحوط منها وتجنبها .</p></div>", unsafe_allow_html=True)

st.markdown("<h2 class='section-title'>الفصل 5 الرؤية والرسالة والقيم</h2>", unsafe_allow_html=True)
st.markdown("<div class='luxury-card'><p>• صياغة الإطار الفلسفي والمرجعي الحاكم للعمل الثقافي بالأمانة الثقافية بما يضمن التزام كافة اللجان والروابط بهوية بصرية موحدة تعبر عن الوجدان الثقافي السوداني الأصيل .</p></div>", unsafe_allow_html=True)

# -------------------------------------------------------------
# الفصل 6 (حل جذري ونهائي لمنع ظهور الكود تماماً وعرض المحتوى نظيفاً)
# -------------------------------------------------------------
st.markdown("<h2 class='section-title'>الفصل 6: الركائز التوجيهية الست ومساراتها التنفيذية</h2>", unsafe_allow_html=True)

html_content_f6 = """
<div style="font-family: 'Cairo', sans-serif; direction: rtl; text-align: right; background-color: #FFFFFF; border: 1px solid #E2E8F0; border-right: 6px solid #1A365D; padding: 25px; border-radius: 10px; color: #1A365D; line-height: 1.8;">
    <p>التفاصيل : يمثل هذا الفصل العصب العملي للخطة حيث يحدد الأعمدة الستة التي يستند عليها البناء الهيكلي الهوية المعرفة، الإبداع الشباب الشراكات، والتحول الرقمي ويترجمها مباشرة إلى محاور ومسارات تطبيقية على أرض الواقع كالتالي:</p>
    
    <p style="margin-top: 20px; font-weight: bold; color: #1A365D; font-size: 17px;">أولاً : محور الهوية والتراث (المسار التنفيذي للمعارض الفنية والتراثية)</p>
    <p>• <b>المهرجانات التراثية:</b> إقامة ملتقيات تراثية في مساحات وقاعات مغلقة تشمل عروضاً للفرق الموسيقية التراثية والرقص الشعبي الممثل لكافة أقاليم السودان لتقديم لوحة وطنية متكاملة تبرز التنوع كعنصر وحدة.</p>
    <p>• <b>أسواق الحرف اليدوية والطهي:</b> تنظيم أسواق ومعارض مصاحبة للحرف اليدوية السودانية والمشغولات الجلدية والخزف، يصاحبها استعراض حي للمأكولات التقليدية لربط الوجدان والأسرة بالثقافة المحلية .</p>
    <p>• <b>ورش العمل التعليمية للتقاليد:</b> تنظيم ورش سريعة وموجهة للأطفال تسلط الضوء على عادات وتقاليد المجتمع السوداني في المناسبات والأعياد لترسيخ قيم التكافل الأصيلة.</p>
    
    <hr style="border: 0; border-top: 1px solid #E2E8F0; margin: 20px 0;">
    
    <p style="font-weight: bold; color: #1A365D; font-size: 17px;">ثانياً: محور المعرفة والتعليم</p>
    <p>• <b>ورش صقل المعارف:</b> بناء القدرات الحقيقية ونقل الخبرات المهنية والعملية لتأهيل الكوادر والشباب والخريجين وتوجيه طاقاتهم المعرفية.</p>
    <p>• <b>جلسات النقاش المستمرة:</b> عقد محاضرات دورية مستمرة تستضيف قادة الرأي والفكر لمناقشة آليات تطوير العمل العام وتوفيق أوضاع الكيانات وتوطيد العلاقات الاجتماعية الإيجابية.</p>
    
    <hr style="border: 0; border-top: 1px solid #E2E8F0; margin: 20px 0;">
    
    <p style="font-weight: bold; color: #1A365D; font-size: 17px;">ثالثاً: محور الإبداع والفنون (المسار التنفيذي للندوات واللقاءات الحوارية)</p>
    <p>• <b>المسابقات الأدبية:</b> إطلاق مسابقات رسمية في مجالات كتابة وتأليف المقالات والقصص القصيرة والرواية والشعر لتشجيع الإبداع وحصر الطاقات الأدبية في المهجر.</p>
    <p>• <b>المناشط الفنية والتشكيلية:</b> تنظيم معارض ومعاهد متخصصة لتعليم وصقل المعارف الفنية في مجالات الرسم والتصوير الفوتوغرافي والفنون البصرية والخط العربي مع إقامة معارض دورية لعرض أعمال المبدعين السودانيين بجدة.</p>
    <p>• <b>صالون القراءة والكتاب:</b> تنظيم صالونات دورية للقراءة وزيارة وتنظيم معارض مصغرة للكتاب، لتشجيع القراءة ونشر الوعي الثقافي بين الأسر والشباب.</p>
    
    <hr style="border: 0; border-top: 1px solid #E2E8F0; margin: 20px 0;">
    
    <p style="font-weight: bold; color: #1A365D; font-size: 17px;">رابعاً: محور الشمولية الثقافية وتكامل الروابط:</p>
    <p>• ضمان التمثيل العادل والمتوازن لكافة مكونات النسيج الاجتماعي والثقافي السوداني بكافة أقاليمه وجغرافيته المتنوعة، لتعزيز فكرة الوحدة من خلال التنوع وتفعيل دور الروابط كشركاء أساسيين.</p>
    
    <hr style="border: 0; border-top: 1px solid #E2E8F0; margin: 20px 0;">
    
    <p style="font-weight: bold; color: #1A365D; font-size: 17px;">خامساً: محور الحراك الثقافي المجتمعي:</p>
    <p>• تخصيص أيام ترفيهية ومعرفية دورية وممنهجة ومبادرات متنقلة للأطفال والناشئة في مختلف النطاقات الجغرافية وتشمل مسرح الطفل، الألعاب التعليمية والمسابقات الثقافية لتعزيز الانتماء للوطن بحماية الهوية وغرس القيم بأساليب محببة وجاذبة.</p>
</div>

<br>

<div style="font-family: 'Cairo', sans-serif; direction: rtl; text-align: right; background-color: #FFFDF5; border: 1px solid #FEF3C7; border-right: 6px solid #C5A059; padding: 25px; border-radius: 10px; color: #1A365D; line-height: 1.8;">
    <p style="color: #1A365D; font-size: 18px; font-weight: bold;">سادساً: منصة "مَجَرَّة" للكفاءات (المشروع المعرفي الأساسي للشباب) :</p>
    <p>• حاضنة معرفية وتنموية رائدة ومبتكرة، تم تصميمها خصيصاً لتكون الفضاء الذي يلتقي فيه العلماء، الخبراء والرواد وعموم أصحاب الكفاءات العالية من أبناء الوطن في المهجر بالمنطقة الغربية.</p>
    <p>• يُجهز مسرح القاعة بأحدث التقنيات البصرية والصوتية المناسبة للعروض التقديمية الاحترافية والملهمة.</p>
    <p>• <b>المتحدثون والعلماء:</b> يتم استضافة 6 شخصيات من أرفع الكفاءات السودانية بالمنطقة الغربية في مجالات (الأكاديمية - الهندسة - التقنية - الطب - الإدارة - وريادة الأعمال).</p>
    <p>• <b>ضوابط المنصة الزمنية:</b> يُمنح كل متحدث 20 دقيقة محددة وصارمة يستعرض فيها "خلاصة تجربته المهنية والعلمية" ويقدم حلولاً وتوصيات عملية للشباب والخريجين بعيداً عن السرد الإنشائي التقليدي.</p>
    <p>• <b>المعرض المهني المصاحب:</b> على هامش المنصة يُقام معرض متكامل لرواد الأعمال الشباب وأصحاب المشاريع والابتكارات والمهن الحرة لتبادل بطاقات العمل والتطوير المعرفي لترسيخ دور الجالية كحاضنة اقتصادية ومعرفية.</p>
</div>
"""

# عرض محتويات الفصل 6 بداخل الـ Component لضمان جودة الأداء وعدم التشويه
st.components.v1.html(html_content_f6, height=920, scrolling=True)

# -------------------------------------------------------------
# باقي فصول الخطة والملاحق
# -------------------------------------------------------------
st.markdown("<h2 class='section-title'>الفصل 7: التحول الرقمي والأرشفة الثقافية</h2>", unsafe_allow_html=True)
st.markdown("<div class='luxury-card'><p>• بناء وتصميم \"المكتبة الرقمية السودانية والأرشيف الرقمي الثقافي\" لحفظ الأعمال الأدبية والندوات والتاريخ السوداني رقمياً وفق أحدث النظم التقنية.</p></div>", unsafe_allow_html=True)

st.markdown("<h2 class='section-title'>الفصل 8: الشراكات والتعاونيات والرعايات</h2>", unsafe_allow_html=True)
st.markdown("<div class='luxury-card'><p>• بناء وتطوير برامج توأمة وشراكات تعاونية مع المؤسسات والروابط الثقافية المحلية، وجذب الرعاة والداعمين لدعم استدامة الأنشطة مالياً ومؤسسياً.</p></div>", unsafe_allow_html=True)

st.markdown("<h2 class='section-title'>الفصل 9: الإعلام الثقافي وإدارة المحتوى</h2>", unsafe_allow_html=True)
st.markdown("<div class='luxury-card'><p>• تصميم خطة تسويق ثقافي متكاملة، وإدارة صناعة المحتوى على المنصات الرقمية لتعكس الأنشطة باحترافية، وتبرز الوجه المشرق للمجتمع السوداني بجدة.</p></div>", unsafe_allow_html=True)

st.markdown("<h2 class='section-title'>الفصل 10: الخطة التشغيلية السنوية</h2>", unsafe_allow_html=True)
st.markdown("<div class='luxury-card'><p>تحويل الرؤى النظرية إلى جداول زمنية محددة التواريخ، وتوزيع المهام التنفيذية والبرامج على مدار العام لتأمين سلاسة الأداء وسهولة الرقابة.</p></div>", unsafe_allow_html=True)

st.markdown("<h2 class='section-title'>الفصل 11: الميزانية التقديرية والحوكمة المالية</h2>", unsafe_allow_html=True)
st.markdown("<div class='luxury-card'><p>تفصيل التدفقات المالية والميزانيات التقديرية المطلوبة لكل حزمة مشروعات، مقرونة بضوابط الحوكمة والشفافية المالية المعتمدة لدى لجنة التسيير.</p></div>", unsafe_allow_html=True)

st.markdown("<h2 class='section-title'>ملاحق الحوكمة والضبط الإداري (بروتوكول الاستدامة والمرجعية)</h2>", unsafe_allow_html=True)
st.markdown("""
<div class='luxury-card'>
    <p>لضمان جودة الأداء وتحقيق المخرجات المستهدفة، ولتأمين ديمومة هذه الوثيقة كارث مؤسسي للجاليات القادمة، تخضع الخطة لمنظومة الحوكمة التالية:</p>
    <p><b>1. بروتوكول التسليم والديمومة المؤسسية (الاستمرارية) :</b> تعتمد هذه الخطة كأصل وثائقي أساسي للأمانة الثقافية في "لجنة تسيير الجالية السودانية بجدة مايو 2026 " وتلتزم الأمانة الحالية بتسليم كافة ملفاتها التقنية والبيانات المستخرجة من المنصات الرقمية (مثل منصة مجرة والمكتبة الرقمية) إلى رئيس لجنة التسيير، لتبدأ الإدارات المتعاقبة من حيث انتهت هذه الخطة دون الحاجة لتأسيس حراك ثقافي من الصفر.</p>
    <p><b>2. بطاقة العضوية الثقافية (المتابعة وقياس الأثر) :</b> إصدار بطاقات حضور رمزية تسلسلية للمشاركين تسهم في قياس مدى التزام وتفاعل العضوية وتمنح ميزات تفضيلية للملتزمين بالمسارات التدريبية في الفعاليات الختامية.</p>
    <p><b>3. صندوق "صوت المواطن" للشفافية :</b> تفعيل صندوق مقترحات رسمي وموثق يتنقل بين كافة المشروعات والفعاليات الحضرية، ويتيح لأبناء الجالية تقديم أفكارهم ورؤاهم المكتوبة مباشرة إلى لجنة التسيير، إيماناً بمبدأ الشفافية والمشاركة الجماعية في صنع القرار.</p>
    <p><b>4. الحوكمة والتنفيذ المؤسسي :</b> تخضع كافة الفعاليات والمشروعات لإشراف مباشر من الأمانة الثقافية بلجنة التسيير، وبالتنسيق الكامل والمنظم مع رئيس وأعضاء لجنة التسيير والقنصلية العامة لجمهورية السودان بجدة لضمان الالتزام المطلق بالضوابط والأنظمة المتبعة في الدولة المضيفة.</p>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------------------
# الخاتمة والتوصيات والتواقيع الاحترافية
# -------------------------------------------------------------
st.markdown("<h2 class='section-title'>الخاتمة والتوصيات:</h2>", unsafe_allow_html=True)
st.markdown("""
<div class='luxury-card' style='border-right-color: #C5A059;'>
    <p>إن هذه الخطة الثقافية الشاملة بمساراتها الواضحة ومستهدفاتها المدروسة وآليات تنفيذها الملموسة وبروتوكول استدامتها الإدارية، تمثل الركيزة الأساسية واللبنة الأولى لصياغة مستقبل جالية نموذجية متلاحمة، ورائدة.</p>
    <p>نضع هذا المشروع الهيكلي والمرجعي أمام سعادتكم للتفضل بالاطلاع والمناقشة، توطئة لإجازته واعتماده لبدء التنفيذ الميداني الفوري وحفظه كارث تنظيمي دائم.</p>
    <p style='text-align: center !important; font-weight: bold;'>سائلين الله العلي القدير أن يوفقنا جميعاً لما فيه خير العباد والبلاد</p>
    <p style='text-align: center !important; font-weight: bold; color: #C5A059;'>،، وتفضلوا بقبول وافر الشكر والتقدير والامتنان ،،</p>
</div>

<!-- قسم التواقيع ممركز ومكبر تماماً باللون الذهبي -->
<div class='signature-section'>
    <p style='font-size: 24px !important; font-weight: bold !important; color: #1A365D !important; text-align: center !important;'>أمانة الثقافة بلجنة تسيير الجالية السودانية بجدة</p>
    <br>
    <table class='signature-table'>
        <tr>
            <td style='font-size: 28px !important; font-weight: 800 !important; color: #C5A059 !important; width: 50%; text-align: center;'>وليد البليل</td>
            <td style='font-size: 28px !important; font-weight: 800 !important; color: #C5A059 !important; width: 50%; text-align: center;'>بابكر عبد الله</td>
        </tr>
    </table>
</div>

<br><hr><p style='text-align: center !important; color: #64748B; font-size: 13px;'>أمانة الثقافة بلجنة تسيير الجالية السودانية بجدة • مايو 2026م</p>
""", unsafe_allow_html=True)
