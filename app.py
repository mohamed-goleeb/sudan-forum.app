import streamlit as st

# 1. إعدادات الصفحة الأساسية والهوية البصرية الكونية
st.set_page_config(
    page_title="برنامج الأمانة الثقافية - الجالية السودانية بجدة",
    page_icon="🇸🇩",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. حقن CSS مطور لحل مشكلة السايدبار والخط القاطع وتحسين العرض على الجوال
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght=400;600;700;800&display=swap');
    
    /* تثبيت الخط والاتجاه الأساسي للمحتوى داخل الصفحة من اليمين لليسار */
    html, body, [data-testid="stAppViewContainer"], .main {
        font-family: 'Cairo', sans-serif !important;
        background-color: #F4F6F9 !important;
        color: #1A365D !important;
    }
    
    /* جعل حاوية المحتوى الرئيسي تدعم القراءة من اليمين لليسار */
    [data-testid="stMain"] [data-testid="stVerticalBlock"] {
        direction: rtl !important;
        text-align: right !important;
    }
    
    /* تنسيق السايدبار في الجهة اليسرى بشكل مستقر يمنع ظهور الخطوط المزعجة */
    [data-testid="stSidebar"] {
        background-color: #0F1E36 !important;
        background-image: linear-gradient(180deg, #0F1E36 0%, #1A365D 100%) !important;
        border-right: 3px solid #C5A059 !important;
        border-left: none !important;
    }
    
    /* ضبط اتجاه عناصر السايدبار لتكون واضحة */
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] {
        direction: rtl !important;
        text-align: right !important;
    }
    
    [data-testid="stSidebar"] * {
        color: #FFFFFF !important;
        font-family: 'Cairo', sans-serif !important;
    }
    
    /* تصميم الهيدر العلوي ليكون متوافقاً مع الجوال والأجهزة الذكية */
    .cosmic-header {
        background: linear-gradient(135deg, #1A365D 0%, #0F1E36 100%);
        padding: 20px 25px;
        border-radius: 12px;
        color: white !important;
        box-shadow: 0 10px 30px rgba(26, 54, 93, 0.15);
        margin-bottom: 20px;
        border-right: 6px solid #C5A059;
        text-align: right !important;
        direction: rtl !important;
    }
    .cosmic-header h1 {
        color: #FFFDF5 !important;
        font-weight: 800 !important;
        font-size: 24px !important; /* حجم متناسق مع الجوال */
        margin: 0 0 8px 0 !important;
        border: none !important;
        padding: 0 !important;
        line-height: 1.4 !important;
    }
    
    /* علم السودان الجمالي */
    .sudan-flag-line {
        height: 5px;
        width: 100%;
        background: linear-gradient(to left, #D21034 33.3%, #FFFFFF 33.3%, #FFFFFF 66.6%, #007229 66.6%);
        border-radius: 10px;
        margin-top: 12px;
    }

    /* كروت العرض التفاعلية الفاخرة - مرنة تماماً للجوال */
    .luxury-card {
        background-color: #FFFFFF !important;
        border: 1px solid #E2E8F0 !important;
        border-right: 6px solid #1A365D !important;
        padding: 18px !important;
        border-radius: 10px !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.04) !important;
        margin-bottom: 20px !important;
        color: #1A365D !important;
        text-align: right !important;
        direction: rtl !important;
    }
    .luxury-card h3, .luxury-card h4 {
        color: #1A365D !important;
        font-weight: 700 !important;
        margin-top: 0 !important;
        margin-bottom: 12px !important;
        font-size: 18px !important;
    }
    .luxury-card p {
        color: #334155 !important;
        font-size: 14px !important;
        line-height: 1.7 !important;
        margin-bottom: 10px !important;
    }
    .luxury-card ul {
        padding-right: 18px !important;
        margin: 0 !important;
        list-style-type: square !important;
    }
    .luxury-card li {
        color: #334155 !important;
        font-size: 14px !important;
        line-height: 1.7 !important;
        margin-bottom: 8px !important;
    }
    
    .gold-luxury-card {
        background-color: #FFFDF5 !important;
        border: 1px solid #FEF3C7 !important;
        border-right: 6px solid #C5A059 !important;
        padding: 18px !important;
        border-radius: 10px !important;
        box-shadow: 0 4px 15px rgba(197, 160, 89, 0.06) !important;
        margin-bottom: 20px !important;
        text-align: right !important;
        direction: rtl !important;
    }

    /* ==========================================
       إصلاح التبويبات (Tabs) لتكون منسابة ومثالية لشاشات الجوال
       ========================================== */
    div[data-testid="stTabs"] {
        direction: rtl !important;
    }
    div[data-testid="stTabs"] [data-baseweb="tab-list"] {
        display: flex !important;
        flex-direction: row !important;
        justify-content: flex-start !important;
        gap: 6px !important;
        border-bottom: 2px solid #E2E8F0 !important;
        padding-bottom: 4px !important;
        overflow-x: auto !important; /* السماح بالتمرير الأفقي على الجوال بدون تخريب التصميم */
        white-space: nowrap !important;
    }
    div[data-testid="stTabs"] button[data-baseweb="tab"] {
        font-family: 'Cairo', sans-serif !important;
        font-size: 14px !important;
        font-weight: 700 !important;
        color: #64748B !important;
        padding: 10px 16px !important;
        background-color: #E2E8F0 !important;
        border-radius: 6px 6px 0 0 !important;
        border: none !important;
        transition: all 0.3s ease !important;
        flex-shrink: 0 !important; /* منع انكماش العناوين الثقافية */
    }
    div[data-testid="stTabs"] button[data-baseweb="tab"][aria-selected="true"] {
        color: #FFFFFF !important;
        background-color: #1A365D !important;
        border-bottom: 3px solid #C5A059 !important;
    }
    
    /* إزالة القوائم العشوائية والرموز الغريبة داخل تابات المعارض */
    div[data-testid="stTabs"] [data-testid="stMarkdownContainer"] ul {
        list-style-type: none !important;
        padding: 0 !important;
        margin: 0 !important;
    }

    /* تجميل أزرار الراديو في السايدبار (الجهة اليسرى) */
    div[data-testid="stRadio"] label {
        background-color: rgba(255, 255, 255, 0.04) !important;
        padding: 10px 15px !important;
        border-radius: 6px !important;
        margin-bottom: 6px !important;
        transition: all 0.3s ease !important;
        border-right: 3px solid transparent !important;
        text-align: right !important;
    }
    div[data-testid="stRadio"] label:hover {
        background-color: rgba(197, 160, 89, 0.15) !important;
        border-right: 3px solid #C5A059 !important;
        cursor: pointer;
    }
    div[data-testid="stWidgetLabel"] p {
        font-size: 15px !important;
        font-weight: bold !important;
        color: #C5A059 !important;
        text-align: right !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. الهيدر الموحد الفاخر
st.markdown("""
    <div class='cosmic-header'>
        <h1>لجنة تسيير الجالية السودانية بجدة</h1>
        <p style='margin: 0; font-size: 15px; color: #CBD5E1; font-weight: bold;'>برنامج الأمانة الثقافية — الرؤية الإستراتيجية والمناشط للمرحلة القادمة</p>
        <div class='sudan-flag-line'></div>
    </div>
    """, unsafe_allow_html=True)

# 4. بناء السايدبار في الجهة اليسرى (مستقر وآمن تماماً للموبايل)
with st.sidebar:
    st.markdown("<div style='text-align: right; padding: 5px 10px;'><h2 style='color: #C5A059 !important; margin:0; font-size:20px;'>📌 الفهرس الرقمي</h2></div>", unsafe_allow_html=True)
    st.markdown("---")
    
    menu_selection = st.radio(
        "انتقل بين بنود البرنامج:",
        [
            "1. المقدمة والمنهجية الإستراتيجية",
            "2. دراسة الفئات المستهدفة",
            "3. المسارات الإستراتيجية",
            "4. المشروعات والفعاليات التنفيذية",
            "5. منصة 'مَجَرَّة' للكفاءات",
            "6. آليات التفعيل والحوكمة",
            "7. الخاتمة والتوصيات"
        ]
    )
    
    st.markdown("---")
    st.markdown("<h4 style='color: #C5A059 !important; text-align:right;'>📊 مؤشر تتبع الخطة</h4>", unsafe_allow_html=True)
    
    if menu_selection == "1. المقدمة والمنهجية الإستراتيجية":
        st.metric("الغايات الأساسية", "4 غايات")
    elif menu_selection == "2. دراسة الفئات المستهدفة":
        st.metric("الفئات الحيوية المحددة", "4 فئات")
    elif menu_selection == "3. المسارات الإستراتيجية":
        st.metric("المسارات والمحاور", "3 مسارات واضحة")
    elif menu_selection == "4. المشروعات والفعاليات التنفيذية":
        st.metric("المشروعات المقترحة", "3 حزم كبرى")
    elif menu_selection == "5. منصة 'مَجَرَّة' للكفاءات":
        st.metric("زمن التتقديم الصارم", "20 دقيقة")
    else:
        st.metric("معايير الحوكمة والشفافية", "100%")

    st.markdown("---")
    st.caption("أمانة الثقافة بلجنة تسيير الجالية السودانية بجدة • مايو 2026م")

# 5. عرض المحتوى بدقة وانسيابية كاملة تمنع أي خطوط مشوهة

if menu_selection == "1. المقدمة والمنهجية الإستراتيجية":
    st.markdown("<h2>1. المقدمة التعريفية والمنهجية الإستراتيجية</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class='luxury-card' style='border-right-color: #C5A059;'>
        <p style='font-size: 15px; font-weight: bold; color: #1A365D;'>السادة رئيس وأعضاء لجنة تسيير الجالية السودانية بجدة : الموقرين</p>
        <p>يتقدم المكتب الثقافي بلجنة التسيير بخطة عمل رسمية للفترة القادمة ، تتضمن أنشطة معرفية فنية وتراثية وتهدف إلى إبراز طاقات المجتمع وتطوير مهاراته من خلال تنفيذ برنامج ثقافي احترافي ناجح يُلبي تطلعات المرحلة الانتقالية.</p>
        <p>إن المنهجية الإستراتيجية لهذا البرنامج تقوم على تحديد الأهداف والجمهور المستهدف أولاً، ومن ثمَّ تصميم المناشط والفعاليات وفقاً للغايات الأساسية للجنة التسيير والتي تنحصر في التالي :</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<h3>🎯 الغايات الأساسية للبرنامج:</h3>", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("""
        <div class='luxury-card'>
            <ul>
                <li><b>تعزيز المعرفة ونشرها</b> بين أبناء الجالية السودانية بجدة.</li>
                <li><b>إبراز التراث الثقافي السوداني الأصيل</b> وربط الجيل الناشئ بوطنه.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class='luxury-card'>
            <ul>
                <li><b>صقل المواهب الوطنية</b> ودعم رواد الأعمال والمبتكرين في شتى المجالات.</li>
                <li><b>تجميع الكيانات والروابط</b> تحت مظلة مؤسسية متناغمة تمهيداً لقيام الجالية.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

elif menu_selection == "2. دراسة الفئات المستهدفة":
    st.markdown("<h2>2. دراسة الفئات المستهدفة وتحليل البيئة</h2>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:15px;'>تلتزم الأمانة الثقافية بدراسة طبيعة واحتياجات الجمهور المستهدف وتصميم برامج متخصصة تلائم كافة المكونات مع التركيز على الفئات الحيوية التالية:</p>", unsafe_allow_html=True)
    
    # تحويل التقسيم ليتوافق مع شاشات الجوال الطولية بسلاسة
    st.markdown("""
    <div class='luxury-card'><h4>1. الشباب والخريجين</h4><p>لتمكينهم وتوجيه طاقاتهم المعرفية والمهنية لصناعة المستقبل.</p></div>
    <div class='luxury-card'><h4>2. الأطفال والناشئة</h4><p>عبر مناشط مخصصة لبناء الهوية الوطنية وحمايتها وغرس القيم.</p></div>
    <div class='luxury-card'><h4>3. الأسر والنساء</h4><p>فعاليات تدمج بين التكافل الاجتماعي والتطوير الاقتصادي للأسر المنتجة.</p></div>
    <div class='luxury-card'><h4>4. الكيانات والروابط</h4><p>الروابط الثقافية والأدبية كشركاء أساسيين في بناء النسيج الموحد.</p></div>
    """, unsafe_allow_html=True)

elif menu_selection == "3. المسارات الإستراتيجية":
    st.markdown("<h2>3. المسارات الإستراتيجية للبرنامج الثقافي</h2>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:15px;'>لضمان جودة المخرجات وسلاسة الأداء تم تقسيم البرنامج الثقافي إلى ثلاثة مسارات ومحاور واضحة ومحددة :</p>", unsafe_allow_html=True)
    
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

elif menu_selection == "4. المشروعات والفعاليات التنفيذية":
    st.markdown("<h2>4. المشروعات والفعاليات التنفيذية المقترحة</h2>", unsafe_allow_html=True)
    
    tab_a, tab_b, tab_c = st.tabs([
        "أ. الصالون الأدبي وملتقيات الإبداع", 
        "ب. ملتقى التراث والفنون الأدائية", 
        "ج. مشروع المجمع الثقافي"
    ])
    
    with tab_a:
        st.markdown("""
        <div class='luxury-card'>
            <h4>🏢 حزمة الصالون الأدبي وملتقيات الإبداع</h4>
            <p><b>• المسابقات الأدبية:</b> إطلاق مسابقات رسمية في مجالات كتابة وتأليف المقالات، والقصص القصيرة، والرواية، والشعر، لتشجيع الإبداع وحصر الطاقات الأدبية في المهجر.</p>
            <p><b>• المناشط الفنية والتشكيلية:</b> تنظيم معارض ومعاهد متخصصة لتعليم وصقل المعارف الفنية في مجالات الرسم، التصوير الفوتوغرافي، الفنون البصرية، والخط العربي مع إقامة معارض دورية لعرض أعمال المبدعين.</p>
            <p><b>• معارض المهرجانات والكتاب:</b> تنظيم صالونات دورية للقراءة وزيارة وتنظيم معارض مصغرة للكتاب، لتشجيع القراءة ونشر الوعي الثقافي بين الأسر والشباب.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with tab_b:
        st.markdown("""
        <div class='luxury-card'>
            <h4>🎪 حزمة ملتقى التراث والفنون الأدائية (مهرجان الهوية)</h4>
            <p><b>• المهرجانات التراثية الحية:</b> إقامة ملتقيات تراثية مغلقة تشمل عروضاً للفرق الموسيقية التراثية والرقص الشعبي الممثل لكافة أقاليم السودان، لتقديم لوحة وطنية متكاملة تبرز التنوع كعنصر وحدة.</p>
            <p><b>• أسواق الحرف اليدوية والطهي:</b> تنظيم أسواق ومعارض مصاحبة للحرف اليدوية السودانية، المشغولات الجلدية والخزف، يصاحبها استعراض حي للمأكولات التقليدية لربط الوجدان والأسرة بالثقافة المحلية.</p>
            <p><b>• ورش العمل التعليمية للتقاليد:</b> تنظيم ورش سريعة وموجهة للأطفال تسلط الضوء على عادات وتقاليد المجتمع السوداني في المناسبات والأعياد لترسيخ قيم التكافل الأصيلة.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with tab_c:
        st.markdown("""
        <div class='luxury-card'>
            <h4>🏰 مشروع "المجمع الثقافي / النادي السوداني"</h4>
            <p><b>• فعاليات الأطفال والناشئة:</b> تخصيص أيام ترفيهية ومعرفية دورية وممنهجة للأطفال، تشمل مسرح الطفل والألعاب التعليمية والمسابقات الثقافية لتعزيز الانتماء للوطن بأساليب محببة وجاذبة وعصرية.</p>
            <p><b>• المحاضرات وجلسات النقاش:</b> عقد محاضرات دورية مستمرة تستضيف قادة الرأي والفكر لمناقشة آليات تطوير العمل العام، وتوفيق أوضاع الكيانات، وتوطيد العلاقات الاجتماعية الإيجابية بين أفراد الجالية.</p>
        </div>
        """, unsafe_allow_html=True)

elif menu_selection == "5. منصة 'مَجَرَّة' للكفاءات":
    st.markdown("<h2>5. المشروع النوعي المبتكر: منصة \"مَجَرَّة\" للكفاءات</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='gold-luxury-card'>
        <p style='font-size: 15px; font-style: italic; text-align: center; margin: 0; color: #C5A059; font-weight: bold;'>
        "مواكبة لأحدث النظم العالمية في نقل المعرفة، تم ابتكار منصة 'مَجَرَّة' لتكون الحاضنة المعرفية والتنموية الكبرى لأبناء الوطن في المهجر."
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='luxury-card'>
        <h4>⚙️ الآلية وضوابط التقديم الصارمة:</h4>
        <ul>
            <li><b>آلية التنفيذ والتقديم:</b> يُجهز مسرح القاعة بأحدث التقنيات البصرية والصوتية المناسبة للعروض التقديمية الاحترافية والملهمة.</li>
            <li><b>المتحدثون:</b> يتم استضافة 6 شخصيات من أرفع الكفاءات السودانية بالمنطقة الغربية.</li>
            <li><b>ضوابط المنصة:</b> يُمنح كل متحدث <b>20 دقيقة محددة وصارمة</b>، يستعرض فيها "خلاصة تجربته المهنية والعلمية".</li>
        </ul>
    </div>
    <div class='luxury-card'>
        <h4>🚀 المعرض المهني المصاحب (دعم رواد الأعمال):</h4>
        <p>على هامش المنصة يُقام معرض متكامل لرواد الأعمال الشباب وأصحاب المشاريع الناشئة والابتكارات والمهن الحرة بهدف إتاحة فرص التشبيك والتواصل.</p>
    </div>
    """, unsafe_allow_html=True)

elif menu_selection == "6. آليات التفعيل والحوكمة":
    st.markdown("<h2>6. آليات التفعيل ( الحوكمة والمتابعة )</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='luxury-card'>
        <h4>🎟️ 1. بطاقة العضوية الثقافية (المتابعة وقياس الأثر)</h4>
        <p>إصدار بطاقات حضور رمزية تسلسلية للمشاركين تسهم في قياس مدى التزام وتفاعل العضوية، وتمنح ميزات تفضيلية وحصرية.</p>
    </div>
    <div class='luxury-card'>
        <h4>📥 2. صندوق "صوت المواطن" للشفافية</h4>
        <p>صندوق مقترحات رسمي وموثق يتيح لأبناء الجالية تقديم أفكارهم ورؤاهم المكتوبة مباشرة إلى لجنة التسيير.</p>
    </div>
    <div class='luxury-card'>
        <h4>⚖️ 3. الحوكمة والتنفيذ المؤسسي</h4>
        <p>تخضع كافة الفعاليات والمشروعات لإشراف مباشر من الأمانة الثقافية بلجنة التسيير، وبالتنسيق الكامل والمنظم مع رئيس لجنة التسيير والقنصلية العامة لجمهورية السودان بجدة.</p>
    </div>
    """, unsafe_allow_html=True)

else:
    st.markdown("<h2>7. الخاتمة والتوصيات</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='luxury-card' style='border-right-color: #C5A059;'>
        <p>إن هذا البرنامج الثقافي المتكامل بمساراته الواضحة وأهدافه المحددة ومستهدفاته المدروسة، يمثل الركيزة الأساسية واللبنة الأولى لصياغة مستقبل جالية نموذجية ومتلاحمة ورائدة تعكس الوجه المشرق للسودان وأبنائه في المملكة العربية السعودية.</p>
        <p>تتقدم الأمانة الثقافية بلجنة تسيير الجالية السودانية بجدة بهذا المقترح الإستراتيجي لسعادتكم للمناقشة والإجازة وبدء التنفيذ الميداني.</p>
        <p style='text-align: center; font-weight: bold; font-size: 15px; margin-top: 20px; color: #1A365D;'>سائلين الله التوفيق والسداد لما فيه خير العباد والبلاد.</p>
        <p style='text-align: center; font-weight: bold; color: #C5A059; margin-top: 10px;'>،، وتفضلوا بقبول وافر الشكر والتقدير ،،</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style='text-align: center; margin-top: 30px; font-weight: bold; color: #1A365D;'>
        <p style='margin:0; font-size: 15px;'>أمانة الثقافة بلجنة تسيير الجالية السودانية بجدة</p>
        <p style='color: #C5A059; margin: 8px 0; font-size: 16px;'>بابكر عبدالله &nbsp;&nbsp;|&nbsp;&nbsp; وليد البليل</p>
    </div>
    """, unsafe_allow_html=True)
