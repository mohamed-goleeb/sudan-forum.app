import streamlit as st

# 1. إعدادات الصفحة الأساسية والهوية البصرية الكونية
st.set_page_config(
    page_title="برنامج الأمانة الثقافية - الجالية السودانية بجدة",
    page_icon="🇸🇩",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. حقن CSS متقدم لإجبار الألوان الرسمية وإصلاح الـ Dark Mode وتفعيل الأنميشن الخارق للخريطة
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;800&display=swap');
    
    /* تثبيت الخط والاتجاه والخلفية بشكل صارم لضمان ثبات الواجهة */
    html, body, [data-testid="stAppViewContainer"], .main {
        font-family: 'Cairo', sans-serif !important;
        direction: rtl !important;
        text-align: right !important;
        background-color: #F4F6F9 !important;
        color: #1A365D !important;
    }
    
    /* تعديل السايدبار ليكون فخماً ومظلمًا مع خطوط ذهبية */
    [data-testid="stSidebar"] {
        background-color: #0F1E36 !important;
        background-image: linear-gradient(180deg, #0F1E36 0%, #1A365D 100%) !important;
        border-left: 3px solid #C5A059 !important;
    }
    
    [data-testid="stSidebar"] * {
        color: #FFFFFF !important;
        font-family: 'Cairo', sans-serif !important;
    }
    
    /* تصميم الهيدر الكوني العلوي */
    .cosmic-header {
        background: linear-gradient(135deg, #1A365D 0%, #0F1E36 100%);
        padding: 35px;
        border-radius: 16px;
        color: white !important;
        box-shadow: 0 10px 30px rgba(26, 54, 93, 0.15);
        margin-bottom: 30px;
        border-right: 8px solid #C5A059;
        position: relative;
        overflow: hidden;
    }
    .cosmic-header h1 {
        color: #FFFDF5 !important;
        font-weight: 800 !important;
        font-size: 30px !important;
        margin: 0 0 10px 0 !important;
        border: none !important;
        padding: 0 !important;
    }
    
    /* علم السودان الجمالي */
    .sudan-flag-line {
        height: 5px;
        width: 100%;
        background: linear-gradient(to left, #D21034 33.3%, #FFFFFF 33.3%, #FFFFFF 66.6%, #007229 66.6%);
        border-radius: 10px;
        margin-top: 15px;
    }

    /* كروت العرض التفاعلية الفاخرة المضيئة */
    .luxury-card {
        background-color: #FFFFFF !important;
        border: 1px solid #E2E8F0 !important;
        border-right: 6px solid #1A365D !important;
        padding: 25px !important;
        border-radius: 12px !important;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05) !important;
        margin-bottom: 25px !important;
        color: #1A365D !important;
    }
    .luxury-card h3, .luxury-card h4 {
        color: #1A365D !important;
        font-weight: 700 !important;
        margin-top: 0 !important;
    }
    .luxury-card p, .luxury-card li {
        color: #334155 !important;
        font-size: 15px !important;
        line-height: 1.8 !important;
    }
    
    .gold-luxury-card {
        background-color: #FFFDF5 !important;
        border: 1px solid #FEF3C7 !important;
        border-right: 6px solid #C5A059 !important;
        padding: 25px !important;
        border-radius: 12px !important;
        box-shadow: 0 4px 20px rgba(197, 160, 89, 0.08) !important;
        margin-bottom: 25px !important;
    }

    /* تجميل أزرار الراديو في السايدبار */
    div[data-testid="stRadio"] label {
        background-color: rgba(255, 255, 255, 0.05) !important;
        padding: 12px 20px !important;
        border-radius: 8px !important;
        margin-bottom: 8px !important;
        transition: all 0.3s ease !important;
        border-right: 3px solid transparent !important;
    }
    div[data-testid="stRadio"] label:hover {
        background-color: rgba(197, 160, 89, 0.15) !important;
        border-right: 3px solid #C5A059 !important;
        cursor: pointer;
    }
    div[data-testid="stWidgetLabel"] p {
        font-size: 16px !important;
        font-weight: bold !important;
        color: #C5A059 !important;
    }

    /* ==========================================
       أنميشن ومؤثرات الخريطة الحركية الفخمة (Dynamic Map Engine)
       ========================================== */
    .map-container {
        position: relative;
        width: 100%;
        height: 520px;
        background-color: #0E1726;
        background-image: 
            radial-gradient(rgba(197, 160, 89, 0.15) 1px, transparent 0),
            radial-gradient(rgba(26, 54, 93, 0.3) 2px, transparent 0);
        background-size: 20px 20px, 40px 40px;
        border-radius: 16px;
        overflow: hidden;
        border: 2px solid #C5A059;
        box-shadow: inset 0 0 50px rgba(0,0,0,0.6);
    }

    /* معالم بحر جدة التخطيطي الفخم */
    .jeddah-sea {
        position: absolute;
        left: 0; top: 0; bottom: 0; width: 25%;
        background: linear-gradient(90deg, #0A111E 0%, #101B2B 100%);
        border-right: 2px dashed rgba(197, 160, 89, 0.3);
    }
    .sea-text {
        position: absolute;
        left: 40px; top: 50%;
        transform: translateY(-50%) rotate(-90deg);
        color: rgba(255,255,255,0.15);
        font-weight: bold; font-size: 20px; letter-spacing: 4px;
    }

    /* الشوارع الرئيسية المتحركة بنظام النيون الجاري */
    .main-street {
        position: absolute;
        background: rgba(255,255,255,0.05);
    }
    /* طريق الملك عبد العزيز */
    .king-aziz-st { left: 32%; top: 0; bottom: 0; width: 6px; }
    /* طريق المدينة المنورة */
    .madinah-st { left: 55%; top: 0; bottom: 0; width: 6px; }
    /* طريق الحرمين السريع */
    .haramain-st { left: 82%; top: 0; bottom: 0; width: 8px; background: rgba(255,255,255,0.08); }
    /* شارع فلسطين العرضي */
    .palestine-st { top: 45%; left: 25%; right: 0; height: 6px; }
    /* طريق مكة القديم العرضي */
    .makkah-st { top: 75%; left: 25%; right: 0; height: 6px; }

    /* أنميشن تدفق نبضات النيون داخل الشوارع */
    .main-street::after {
        content: '';
        position: absolute;
        background: linear-gradient(90deg, transparent, #C5A059, #FFFFFF, #C5A059, transparent);
        border-radius: 10px;
    }
    /* تدفق طولي */
    .king-aziz-st::after, .madinah-st::after, .haramain-st::after {
        top: -100px; left: 0; width: 100%; height: 100px;
        background: linear-gradient(180deg, transparent, #C5A059, #FFFFFF, #C5A059, transparent);
        animation: flowVertical 6s linear infinite;
    }
    .madinah-st::after { animation-delay: 2s; animation-duration: 5s; }
    .haramain-st::after { animation-delay: 1s; animation-duration: 4s; background: linear-gradient(180deg, transparent, #007229, #FFFFFF, #007229, transparent); }
    /* تدفق عرضي */
    .palestine-st::after, .makkah-st::after {
        left: -100px; top: 0; height: 100%; width: 100px;
        animation: flowHorizontal 7s linear infinite;
    }
    .makkah-st::after { animation-delay: 3.5s; animation-duration: 5.5s; }

    @keyframes flowVertical {
        0% { top: -100px; }
        100% { top: 100%; }
    }
    @keyframes flowHorizontal {
        0% { left: -100px; }
        100% { left: 100%; }
    }

    /* نقاط الفعاليات الإشعاعية النابضة باستمرار (Pulsing Targets) */
    .map-node {
        position: absolute;
        width: 18px; height: 18px;
        background-color: #D21034;
        border-radius: 50%;
        border: 3px solid #FFFFFF;
        box-shadow: 0 0 15px #D21034;
        cursor: pointer;
        z-index: 10;
    }
    .map-node::before {
        content: '';
        position: absolute;
        top: -16px; left: -16px; right: -16px; bottom: -16px;
        border: 3px solid rgba(210, 16, 52, 0.6);
        border-radius: 50%;
        animation: pulseRing 2s cubic-bezier(0.215, 0.610, 0.355, 1) infinite;
    }
    .map-node::after {
        content: '';
        position: absolute;
        top: -32px; left: -32px; right: -32px; bottom: -32px;
        border: 1px solid rgba(197, 160, 89, 0.4);
        border-radius: 50%;
        animation: pulseRing 3s cubic-bezier(0.215, 0.610, 0.355, 1) infinite;
        animation-delay: 0.5s;
    }

    @keyframes pulseRing {
        0% { transform: scale(0.3); opacity: 0; }
        50% { opacity: 1; }
        100% { transform: scale(1); opacity: 0; }
    }

    /* تسميات كروت المواقع المنبثقة الفاخرة المربوطة بالخريطة */
    .node-label {
        position: absolute;
        background: rgba(15, 30, 54, 0.95);
        border: 1px solid #C5A059;
        padding: 10px 14px;
        border-radius: 8px;
        color: #FFFDF5 !important;
        font-size: 13px;
        font-weight: bold;
        box-shadow: 0 5px 15px rgba(0,0,0,0.5);
        width: 240px;
        pointer-events: none;
    }
    .node-label span {
        color: #C5A059;
        font-size: 11px;
        display: block;
        margin-top: 4px;
        font-weight: normal;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. الهيدر الموحد المحدث بنص المستند الصارم
st.markdown("""
    <div class='cosmic-header'>
        <h1>لجنة تسيير الجالية السودانية بجدة</h1>
        <p style='margin: 0; font-size: 18px; color: #CBD5E1; font-weight: bold;'>برنامج الأمانة الثقافية — الرؤية الإستراتيجية والمناشط للمرحلة القادمة</p>
        <div class='sudan-flag-line'></div>
    </div>
    """, unsafe_allow_html=True)

# 4. بناء السايدبار الذكي المطور كـ (Control Panel) ملاحي
with st.sidebar:
    st.markdown("<div style='text-align: center; padding: 10px;'><h2 style='color: #C5A059 !important; margin:0;'>🇸🇩 الفهرس الرقمي</h2></div>", unsafe_allow_html=True)
    st.markdown("---")
    
    menu_selection = st.radio(
        "📌 انتقل بين بنود البرنامج:",
        [
            "1. المقدمة والمنهجية الإستراتيجية",
            "2. دراسة الفئات المستهدفة",
            "🗺️ خريطة الفعاليات الحركية (جدة)",
            "3. المسارات الإستراتيجية",
            "4. المشروعات والفعاليات التنفيذية",
            "5. منصة 'مَجَرَّة' للكفاءات",
            "6. آليات التفعيل والحوكمة",
            "7. الخاتمة والتوصيات"
        ]
    )
    
    st.markdown("---")
    st.markdown("<h4 style='color: #C5A059 !important;'>📊 مؤشر تتبع الخطة</h4>", unsafe_allow_html=True)
    
    if menu_selection == "1. المقدمة والمنهجية الإستراتيجية":
        st.metric("الغايات الأساسية", "4 غايات")
    elif menu_selection == "2. دراسة الفئات المستهدفة":
        st.metric("الفئات الحيوية المحددة", "4 فئات")
    elif menu_selection == "🗺️ خريطة الفعاليات الحركية (جدة)":
        st.metric("الحركة الديناميكية", "نشط ومتحرك ⚡")
    elif menu_selection == "3. المسارات الإستراتيجية":
        st.metric("المسارات والمحاور", "3 مسارات واضحة")
    elif menu_selection == "4. المشروعات والفعاليات التنفيذية":
        st.metric("المشروعات المقترحة", "3 حزم كبرى")
    elif menu_selection == "5. منصة 'مَجَرَّة' للكفاءات":
        st.metric("زمن التقديم الصارم", "20 دقيقة")
    else:
        st.metric("معايير الحوكمة والشفافية", "100%")

    st.markdown("---")
    st.caption("أمانة الثقافة بلجنة تسيير الجالية السودانية بجدة • مايو 2026م")

# 5. معالجة وتوزيع المحتوى المعتمد

if menu_selection == "1. المقدمة والمنهجية الإستراتيجية":
    st.markdown("<h2>1. المقدمة التعريفية والمنهجية الإستراتيجية</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class='luxury-card' style='border-right-color: #C5A059;'>
        <p style='font-size: 16px; font-weight: bold; color: #1A365D;'>السادة رئيس وأعضاء لجنة تسيير الجالية السودانية بجدة : الموقرين</p>
        <p>يتقدم المكتب الثقافي بلجنة التسيير بخطة عمل رسمية للفترة القادمة ، تتضمن أنشطة معرفية فنية وتراثية وتهدف إلى إبراز طاقات المجتمع وتطوير مهاراته من خلال تنفيذ برنامج ثقافي احترافي ناجح يُلبي تطلعات المرحلة الانتقالية.</p>
        <p>إن المنهجية الإستراتيجية لهذا البرنامج تقوم على تحديد الأهداف والجمهور المستهدف أولاً، ومن ثمَّ تصميم المناشط والفعاليات وفقاً للغايات الأساسية للجنة التسيير والتي تنحصر في التالي :</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<h3>🎯 المنهجية الإستراتيجية للبرنامج:</h3>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class='luxury-card'>
            <ul>
                <li><b>تعزيز المعرفة ونشرها</b> بين أبناء الجالية .</li>
                <li><b>إبراز التراث الثقافي السوداني الأصيل</b> وربط الجيل الناشئ بوطنه .</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class='luxury-card'>
            <ul>
                <li><b>صقل المواهب الوطنية</b> ودعم رواد الأعمال والمبتكرين .</li>
                <li><b>تجميع الكيانات والروابط</b> تحت مظلة مؤسسية متناغمة تمهيداً لقيام الجالية .</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

elif menu_selection == "2. دراسة الفئات المستهدفة":
    st.markdown("<h2>2. دراسة الفئات المستهدفة وتحليل البيئة</h2>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:16px;'>تلتزم الأمانة الثقافية بدراسة طبيعة واحتياجات الجمهور المستهدف وتصميم برامج متخصصة تلائم كافة المكونات مع التركيز على الفئات الحيوية التالية:</p>", unsafe_allow_html=True)
    
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown("<div class='luxury-card' style='text-align:center; height:100%;'><h4>1. فئة الشباب والخريجين</h4><hr><p>لتمكينهم وتوجيه طاقاتهم المعرفية والمهنية .</p></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='luxury-card' style='text-align:center; height:100%;'><h4>2. فئة الأطفال والناشئة</h4><hr><p>عبر مناشط مخصصة لبناء الهوية الوطنية وحمايتها .</p></div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='luxury-card' style='text-align:center; height:100%;'><h4>3. فئة الأسر والنساء</h4><hr><p>من خلال فعاليات تدمج بين التكافل الاجتماعي والتطوير الاقتصادي (دعم الأسر المنتجة) .</p></div>", unsafe_allow_html=True)
    with c4:
        st.markdown("<div class='luxury-card' style='text-align:center; height:100%;'><h4>4. الكيانات والروابط</h4><hr><p>الروابط الثقافية والأدبية: لتفعيل دورها كشركاء أساسيين في بناء النسيج الموحد للجالية .</p></div>", unsafe_allow_html=True)

# الـ WOW الحقيقي والمبهر: الخريطة التخطيطية المتحركة بنبض النيون والمواقع المشعة لمدينة جدة
elif menu_selection == "🗺️ خريطة الفعاليات الحركية (جدة)":
    st.markdown("<h2>🗺️ لوحة التحكم الجغرافية الرقمية المتحركة لمشروعات الأمانة بجدة</h2>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:16px;'>نظام محاكاة حركي مباشر يوضح ترابط الفعاليات والمشروعات الميدانية عبر الشرايين والشوارع الحيوية لمدينة جدة (طريق الملك، المدينة، وفلسطين) بنبضات نيون متحركة تضمن الانبهار التام:</p>", unsafe_allow_html=True)
    
    # بناء الخريطة الحركية الفخمة بالـ HTML & CSS المطور
    map_html = """
    <div class="map-container">
        <div class="jeddah-sea">
            <div class="sea-text">RED SEA - عروس البحر الأحمر</div>
        </div>
        
        <div class="main-street king-aziz-st" title="طريق الملك عبدالعزيز"></div>
        <div class="main-street madinah-st" title="طريق المدينة المنورة"></div>
        <div class="main-street haramain-st" title="طريق الحرمين السريع"></div>
        <div class="main-street palestine-st" title="شارع فلسطين"></div>
        <div class="main-street makkah-st" title="طريق مكة القديم"></div>
        
        <div class="map-node" style="left: 31%; top: 43%;"></div>
        <div class="node-label" style="left: 35%; top: 35%;">
            🏢 أ. الصالون الأدبي وملتقيات الإبداع
            <span>تشمل المسابقات الأدبية، مناشط الفنون البصرية والخط العربي، وصالونات القراءة.</span>
        </div>
        
        <div class="map-node" style="left: 31%; top: 18%;"></div>
        <div class="node-label" style="left: 35%; top: 10%;">
            🎪 ب. ملتقى التراث (مهرجان الهوية)
            <span>المهرجانات التراثية الحية لكافة أقاليم السودان، أسواق الحرف اليدوية والطهي الحي التقليدي.</span>
        </div>
        
        <div class="map-node" style="left: 54%; top: 73%;"></div>
        <div class="node-label" style="left: 58%; top: 65%;">
            🏰 ج. مشروع المجمع الثقافي / النادي السوداني
            <span>فعاليات الأطفال والناشئة، مسرح الطفل المنهجي، والمحاضرات الفكرية وجلسات النقاش المستمر.</span>
        </div>
        
        <div class="map-node" style="left: 54%; top: 43%; background-color: #C5A059; box-shadow: 0 0 20px #C5A059;"></div>
        <div class="node-label" style="left: 58%; top: 35%; border-color: #D21034;">
            🌌 5. منصة "مَجَرَّة" للكفاءات (الحدث النوعي)
            <span>استضافة أرفع 6 كفاءات سودانية في المسرح التكنولوجي المجهز بضابط الـ 20 دقيقة والمعرض المهني.</span>
        </div>
    </div>
    """
    st.components.v1.html(map_html, height=530)
    st.success("⚡ تظهر الخريطة تدفقاً مستمراً لنبضات النيون في الشوارع الكبرى مع حلقات رادار نابضة حول مقار المشروعات لتأكيد جاهزية الأمانة ثقافياً وعملياً وميدانياً!")

elif menu_selection == "3. المسارات الإستراتيجية":
    st.markdown("<h2>3. المسارات الإستراتيجية للبرنامج الثقافي</h2>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:16px;'>لضمان جودة المخرجات وسلاسة الأداء تم تقسيم البرنامج الثقافي إلى ثلاثة مسارات ومحاور واضحة ومحددة :</p>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='luxury-card'>
        <h4>📚 أولاً مسار الندوات واللقاءات الحوارية والثقافية:</h4>
        <p>لترسيخ الوعي وتوفير منصات للنقاش الفكري البنّاء .</p>
    </div>
    <div class='luxury-card'>
        <h4>⚙️ ثانياً مسار الورش التدريبية التفاعلية :</h4>
        <p>لبناء القدرات وصقل المعارف ونقل الخبرات المهنية والعملية .</p>
    </div>
    <div class='luxury-card'>
        <h4>🖼️ ثالثاً مسار المعارض الفنية والتراثية :</h4>
        <p>لتوثيق الهوية السودانية وإبراز الإبداع البصري والموسيقي حسب انظمة ولوائح الدولة المضيفة .</p>
    </div>
    """, unsafe_allow_html=True)

elif menu_selection == "4. المشروعات والفعاليات التنفيذية":
    st.markdown("<h2>4. المشروعات والفعاليات التنفيذية المقترحة</h2>", unsafe_allow_html=True)
    
    tab_a, tab_b, tab_c = st.tabs(["أ. الصالون الأدبي وملتقيات الإبداع", "ب. ملتقى التراث والفنون الأدائية (مهرجان الهوية)", "ج. مشروع "])
    
    with tab_a:
        st.markdown("""
        <div class='luxury-card'>
            <ul>
                <li><b>المسابقات الأدبية:</b> إطلاق مسابقات رسمية في مجالات كتابة وتأليف المقالات والقصص القصيرة والرواية والشعر لتشجيع الإبداع وحصر الطاقات الأدبية في المهجر .</li>
                <li><b>المناشط الفنية والتشكيلية:</b> تنظيم معارض ومعاهد متخصصة لتعليم وصقل المعارف الفنية في مجالات الرسم والتصوير الفوتوغرافي والفنون البصرية والخط العربي مع إقامة معارض دورية لعرض أعمال المبدعين السودانيين بجدة .</li>
                <li><b>معارض المهرجانات والكتاب:</b> تنظيم صالونات للقراءة وزيارة وتنظيم معارض مصغرة للكتاب، لتشجيع القراءة ونشر الوعي الثقافي بين الأسر والشباب .</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with tab_b:
        st.markdown("""
        <div class='luxury-card'>
            <ul>
                <li><b>المهرجانات التراثية الحية:</b> إقامة ملتقيات تراثية مغلقة تشمل عروضاً للفرق الموسيقية التراثية والرقص الشعبي الممثل لكافة أقاليم السودان ، لتقديم لوحة وطنية متكاملة تبرز التنوع كعنصر وحدة .</li>
                <li><b>أسواق الحرف اليدوية والطهي:</b> تنظيم أسواق ومعارض مصاحبة للحرف اليدوية السودانية، المشغولات الجلدية والخزف، يصاحبها استعراض حي للمأكولات التقليدية لربط الوجدان والأسرة بالثقافة المحلية .</li>
                <li><b>ورش العمل التعليمية للتقاليد:</b> تنظيم ورش سريعة وموجهة للأطفال تسلط الضوء على عادات وتقاليد المجتمع السوداني في المناسبات والأعياد لترسيخ قيم التكافل .</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with tab_c:
        st.markdown("""
        <div class='luxury-card'>
            <h4>ج. مشروع "المجمع الثقافي / النادي السوداني"</h4>
            <ul>
                <li><b>فعاليات الأطفال والناشئة:</b> تخصيص أيام ترفيهية ومعرفية دورية وممنهجة للأطفال، تشمل مسرح الطفل والألعاب التعليمية والمسابقات الثقافية لتعزيز الانتماء للوطن بأساليب محببة وجاذبة .</li>
                <li><b>المحاضرات وجلسات النقاش:</b> عقد محاضرات دورية مستمرة تستضيف قادة الرأي والفكر لمناقشة آليات تطوير العمل العام وتوفيق أوضاع الكيانات وتوطيد العلاقات الاجتماعية الإيجابية.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

elif menu_selection == "5. منصة 'مَجَرَّة' للكفاءات":
    st.markdown("<h2>5. المشروع النوعي المبتكر: منصة \"مَجَرَّة\" للكفاءات</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='gold-luxury-card'>
        <p style='font-size: 16px; font-style: italic; text-align: center; margin: 0; color: #C5A059;'>
        "مواكبة لأحدث النظم العالمية في نقل المعرفة، تم ابتكار منصة 'مَجَرَّة ' لتكون الحاضنة المعرفية والتنموية الكبرى لأبناء الوطن في المهجر. حيث يُشبه كل خبير أو عالم أو رائد أعمال سوداني بـ 'النجم الساطع' في مجاله، وتأتي المنصة لتجمع هذه النجوم في فلك تنموي واحد يخدم قضايا الجالية وتطلعات شبابها ."
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col_x, col_y = st.columns(2)
    with col_x:
        st.markdown("""
        <div class='luxury-card' style='height:100%;'>
            <h4>⚙️ الآلية وضوابط التقديم:</h4>
            <ul>
                <li><b>آلية التنفيذ والتقديم:</b> يُجهز مسرح القاعة بأحدث التقنيات البصرية والصوتية المناسبة للعروض التقديمية الاحترافية والملهمة .</li>
                <li><b>المتحدثون:</b> يتم استضافة 6 شخصيات من أرفع الكفاءات السودانية بالمنطقة الغربية (في مجالات: الأكاديمية والهندسة والتقنية والطب والإدارة وريادة الأعمال) .</li>
                <li><b>ضوابط المنصة:</b> يُمنح كل متحدث <b>20 دقيقة محددة وصارمة</b>، يستعرض فيها "خلاصة تجربته المهنية والعلمية" ويقدم حلولاً وتوصيات عملية للشباب والخريجين بعيداً عن السرد الإنشائي التقليدي .</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    with col_y:
        st.markdown("""
        <div class='luxury-card' style='height:100%;'>
            <h4>🚀 المعرض المهني المصاحب (دعم رواد الأعمال):</h4>
            <p>على هامش المنصة يُقام معرض لرواد الأعمال الشباب وأصحاب المشاريع والابتكارات والمهن الحرة لتبادل بطاقات العمل والتطوير المعرفي لترسيخ دور الجالية كحاضنة اقتصادية ومعرفية داعمة ومطورة لأبنائها .</p>
        </div>
        """, unsafe_allow_html=True)

elif menu_selection == "6. آليات التفعيل والحوكمة":
    st.markdown("<h2>6. آليات التفعيل ( الحوكمة والمتابعة )</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='luxury-card'>
        <h4>🎟️ 1. بطاقة العضوية الثقافية (المتابعة) :</h4>
        <p>إصدار بطاقات حضور رمزية تسلسلية للمشاركين تسهم في قياس مدى التزام وتفاعل العضوية وتمنح ميزات تفضيلية للملتزمين بالمسارات التدريبية في الفعاليات الختامية .</p>
    </div>
    <div class='luxury-card'>
        <h4>📥 2. صندوق "صوت المواطن":</h4>
        <p>صندوق مقترحات رسمي وموثق يتنقل بين كافة المشروعات والفعاليات الحضرية ويتيح لأبناء الجالية تقديم أفكارهم ورؤاهم المكتوبة مباشرة إلى لجنة التسيير، إيماناً بمبدأ الشفافية والمشاركة الجماعية في صنع القرار .</p>
    </div>
    <div class='luxury-card'>
        <h4>⚖️ 3. الحوكمة والتنفيذ :</h4>
        <p>تخضع كافة الفعاليات مباشرة من الأمانة الثقافية بلجنة التسيير وبالتنسيق الكامل مع رئيس لجنة التسيير القنصلية العامة لجمهورية السودان بجدة لضمان الالتزام بالضوابط والأنظمة .</p>
    </div>
    """, unsafe_allow_html=True)

else:
    st.markdown("<h2>7. الخاتمة والتوصيات</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='luxury-card' style='border-right-color: #C5A059;'>
        <p>إن هذا البرنامج الثقافي المتكامل بمساراته الواضحة وأهدافه المحددة ومستهدفاته المدروسة، يمثل الركيزة الأساسية واللبنة الأولى لصياغة مستقبل جالية نموذجية ومتلاحمة ورائدة تعكس الوجه المشرق للسودان وأبنائه في المملكة العربية السعودية .</p>
        <p>تتقدم الأمانة الثقافية بلجنة التسيير بهذا المقترح الإسترايجي لسعادتكم للمناقشة والإجازة .</p>
        <p style='text-align: center; font-weight: bold; font-size: 16px; margin-top: 20px; color: #1A365D;'>سائلين الله التوفيق والسداد لما فيه خير العباد والبلاد .</p>
        <p style='text-align: center; font-weight: bold; color: #C5A059;'>،، وتفضلوا بقبول وافر الشكر والتقدير،،</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style='text-align: center; margin-top: 40px; font-weight: bold; color: #1A365D;'>
        <p style='margin:0; font-size: 16px;'>امانة الثقافة بلجنة تسيير الجالية السودانية بجدة</p>
        <p style='color: #C5A059; margin: 8px 0; font-size: 18px;'>بابكر عبدالله &nbsp;&nbsp;|&nbsp;&nbsp; وليد البليل</p>
    </div>
    """, unsafe_allow_html=True)
