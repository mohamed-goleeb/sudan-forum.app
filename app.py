import streamlit as st

# 1. إعدادات الصفحة الأساسية والهوية البصرية بدون سايدبار
st.set_page_config(
    page_title="برنامج الأمانة الثقافية - ملتقى السودان بجدة",
    page_icon="🇸🇩",
    layout="wide",
    initial_sidebar_state="collapsed" # إغلاق السايدبار تلقائياً
)

# 2. حقن CSS المطور للألوان الفاخرة والخطوط ودعم الشاشات بدون سايدبار
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght=400;600;700;800&display=swap');
    
    /* إخفاء زر السايدبار تماماً من الواجهة */
    [data-testid="collapsedControl"] {
        display: none !important;
    }
    
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
    
    /* تصميم الهيدر العلوي الفاخر */
    .cosmic-header {
        background: linear-gradient(135deg, #1A365D 0%, #0F1E36 100%);
        padding: 25px 30px;
        border-radius: 12px;
        color: white !important;
        box-shadow: 0 10px 30px rgba(26, 54, 93, 0.15);
        margin-bottom: 25px;
        border-right: 6px solid #C5A059;
        text-align: right !important;
        direction: rtl !important;
    }
    .cosmic-header h1 {
        color: #FFFDF5 !important;
        font-weight: 800 !important;
        font-size: 26px !important;
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
        margin-top: 15px;
    }

    /* كروت العرض التفاعلية الفاخرة */
    .luxury-card {
        background-color: #FFFFFF !important;
        border: 1px solid #E2E8F0 !important;
        border-right: 6px solid #1A365D !important;
        padding: 20px !important;
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
        font-size: 15px !important;
        line-height: 1.8 !important;
        margin-bottom: 10px !important;
    }
    .luxury-card ul {
        padding-right: 20px !important;
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
        margin-bottom: 20px !important;
        text-align: right !important;
        direction: rtl !important;
    }

    /* إصلاح التبويبات (Tabs) لتكون منسابة لشاشات الجوال */
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
        overflow-x: auto !important;
        white-space: nowrap !important;
    }
    div[data-testid="stTabs"] button[data-baseweb="tab"] {
        font-family: 'Cairo', sans-serif !important;
        font-size: 15px !important;
        font-weight: 700 !important;
        color: #64748B !important;
        padding: 10px 18px !important;
        background-color: #E2E8F0 !important;
        border-radius: 6px 6px 0 0 !important;
        border: none !important;
        transition: all 0.3s ease !important;
        flex-shrink: 0 !important;
    }
    div[data-testid="stTabs"] button[data-baseweb="tab"][aria-selected="true"] {
        color: #FFFFFF !important;
        background-color: #1A365D !important;
        border-bottom: 3px solid #C5A059 !important;
    }

    /* تخصيص وتجميل أداة الاختيار العلوية الفهرس البديل للسايدبار */
    div[data-testid="stSelectbox"] label p {
        font-size: 16px !important;
        font-weight: bold !important;
        color: #1A365D !important;
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

# 4. الفهرس الرقمي العلوي كبديل أنيق وجذاب للسايدبار
st.markdown("### 📌 الفهرس المرجعي السريع")
menu_selection = st.selectbox(
    "اختر البند أو الفصل المراد استعراضه مباشرة:",
    [
        "1. المقدمة والمنهجية الإستراتيجية",
        "2. دراسة الفئات المستهدفة وتحليل الواقع",
        "3. المسارات الإستراتيجية للبرنامج",
        "4. المشروعات والفعاليات التنفيذية المقترحة",
        "5. منصة 'مَجَرَّة' للكفاءات (المشروع الأساسي)",
        "6. آليات التفعيل والحوكمة المستدامة",
        "7. الخاتمة والتوصيات المعتمدة"
    ]
)

st.markdown("---")

# 5. عرض محتوى بنود الخطاب بناءً على الاختيار العلوي وبنفس الألوان الفاخرة

if menu_selection == "1. المقدمة والمنهجية الإستراتيجية":
    st.markdown("<h2>1. المقدمة التعريفية والمنهجية الإستراتيجية</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class='luxury-card' style='border-right-color: #C5A059;'>
        <p style='font-size: 16px; font-weight: bold; color: #1A365D;'>السادة رئيس وأعضاء لجنة تسيير الجالية السودانية بجدة : الموقرين</p>
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

elif menu_selection == "2. دراسة الفئات المستهدفة وتحليل الواقع":
    st.markdown("<h2>2. دراسة الفئات المستهدفة وتحليل البيئة</h2>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:16px;'>تلتزم الأمانة الثقافية بدراسة طبيعة وااحتياجات الجمهور المستهدف وتصميم برامج متخصصة تلائم كافة المكونات مع التركيز على الفئات الحيوية التالية:</p>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='luxury-card'><h4>1. الشباب والخريجين</h4><p>لتمكينهم وتوجيه طاقاتهم المعرفية والمهنية لصناعة المستقبل.</p></div>
    <div class='luxury-card'><h4>2. الأطفال والناشئة</h4><p>عبر مناشط مخصصة لبناء الهوية الوطنية وحمايتها وغرس القيم.</p></div>
    <div class='luxury-card'><h4>3. الأسر والنساء</h4><p>فعاليات تدمج بين التكافل الاجتماعي والتطوير الاقتصادي للأسر المنتجة.</p></div>
    <div class='luxury-card'><h4>4. الكيانات والروابط</h4><p>الروابط الثقافية والأدبية كشركاء أساسيين في بناء النسيج الموحد.</p></div>
    """, unsafe_allow_html=True)

elif menu_selection == "3. المسارات الإستراتيجية للبرنامج":
    st.markdown("<h2>3. المسارات الإستراتيجية للبرنامج الثقافي</h2>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:16px;'>لضمان جودة المخرجات وسلاسة الأداء تم تقسيم البرنامج الثقافي إلى ثلاثة مسارات ومحاور واضحة ومحددة :</p>", unsafe_allow_html=True)
    
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

elif menu_selection == "4. المشروعات والفعاليات التنفيذية المقترحة":
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
            <p><b>• المناشط الفنية والتشكيلية:</b> تنظيم معارض ومعاهد متخصصة لتعليم وصقل المعارف الفنية في مجالات الرسم، التصوير الفوتوغرافي، الفنون البصرية، والخط العربي مع إقامة معارض دورية لعرض أعمال المبدعين السودانيين بجدة.</p>
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

elif menu_selection == "5. منصة 'مَجَرَّة' للكفاءات (المشروع الأساسي)":
    st.markdown("<h2>5. المشروع النوعي المبتكر: منصة \"مَجَرَّة\" للكفاءات</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='gold-luxury-card'>
        <p style='font-size: 16px; font-style: italic; text-align: center; margin: 0; color: #C5A059; font-weight: bold;'>
        "مواكبة لأحدث النظم العالمية في نقل المعرفة، تم ابتكار منصة 'مَجَرَّة' لتكون الحاضنة المعرفية والتنموية الكبرى لأبناء الوطن في المهجر."
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='luxury-card'>
        <h4>⚙️ الآلية وضوابط التقديم الصارمة:</h4>
        <ul>
            <li><b>آلية التنفيذ والتقديم:</b> يُجهز مسرح القاعة بأحدث التقنيات البصرية والصوتية المناسبة للعروض التقديمية الاحترافية والملهمة.</li>
            <li><b>المتحدثون والعلماء:</b> يتم استضافة 6 شخصيات من أرفع الكفاءات السودانية بالمنطقة الغربية (في مجالات: الأكاديمية - الهندسة – التقنية – الطب – الإدارة - وريادة الأعمال).</li>
            <li><b>ضوابط المنصة الزمنية:</b> يُمنح كل متحدث <b>20 دقيقة محددة وصارمة</b>، يستعرض فيها "خلاصة تجربته المهنية والعلمية" ويقدم حلولاً وتوصيات عملية للشباب والخريجين بعيداً عن السرد الإنشائي التقليدي.</li>
        </ul>
    </div>
    <div class='luxury-card'>
        <h4>🚀 المعرض المهني المصاحب (دعم رواد الأعمال):</h4>
        <p>على هامش المنصة يُقام معرض متكامل لرواد الأعمال الشباب وأصحاب المشاريع الناشئة والابتكارات والمهن الحرة بهدف إتاحة فرص التشبيك والتواصل، وترسيخ دور الجالية كحاضنة اقتصادية ومعرفية ملموسة.</p>
    </div>
    """, unsafe_allow_html=True)

elif menu_selection == "6. آليات التفعيل والحوكمة المستدامة":
    st.markdown("<h2>6. آليات التفعيل ( الحوكمة والضبط الإداري المرجعي )</h2>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:15px;'>تأميناً لديمومة هذه الوثيقة كإرث مؤسسي للجاليات القادمة، تخضع الخطة لمنظومة الحوكمة التالية:</p>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='luxury-card'>
        <h4>🎟️ 1. بروتوكول التسليم والديمومة المؤسسية (الاستمرارية)</h4>
        <p>تُعتمد هذه الخطة كأصل وثائقي أساسي للأمانة الثقافية في "لجنة تيسير الجالية السودانية بجدة مايو 2026"، وتلتزم الأمانة الحالية بتسليم كافة ملفاتها التقنية والبيانات المستخرجة من المنصات الرقمية إلى رئيس لجنة التسيير، لتبدأ الإدارات المتعاقبة من حيث انتهت هذه الخطة دون الحاجة لتأسيس حراك من الصفر.</p>
    </div>
    <div class='luxury-card'>
        <h4>🎫 2. بطاقة العضوية الثقافية (المتابعة وقياس الأثر)</h4>
        <p>إصدار بطاقات حضور رمزية تسلسلية للمشاركين تسهم في قياس مدى التزام وتفاعل العضوية، وتمنح ميزات تفضيلية وحصرية للملتزمين بالمسارات التدريبية في الفعاليات الختامية.</p>
    </div>
    <div class='luxury-card'>
        <h4>📥 3. صندوق "صوت المواطن" للشفافية</h4>
        <p>تفعيل صندوق مقترحات رسمي وموثق يتنقل بين كافة المشروعات والفعاليات الحضرية، ويتيح لأبناء الجالية تقديم أفكارهم ورؤاهم المكتوبة مباشرة إلى لجنة التسيير، إيماناً بمبدأ الشفافية والمشاركة الجماعية في صنع القرار.</p>
    </div>
    <div class='luxury-card'>
        <h4>⚖️ 4. الحوكمة والتنفيذ المؤسسي</h4>
        <p>تخضع كافة الفعاليات والمشروعات لإشراف مباشر من الأمانة الثقافية بلجنة التسيير، وبالتنسيق الكامل والمنظم مع رئيس وأعضاء لجنة التسيير والقنصلية العامة لجمهورية السودان بجدة لضمان الالتزام المطلق بالضوابط والأنظمة المتبعة في الدولة المضيفة.</p>
    </div>
    """, unsafe_allow_html=True)

else:
    st.markdown("<h2>7. الخاتمة والتوصيات</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='luxury-card' style='border-right-color: #C5A059;'>
        <p>إن هذا البرنامج الثقافي المتكامل بمساراتها الواضحة وأهدافه المحددة ومستهدفاته المدروسة، يمثل الركيزة الأساسية واللبنة الأولى لصياغة مستقبل جالية نموذجية ومتلاحمة ورائدة تعكس الوجه المشرق للسودان وأبنائه في المملكة العربية السعودية.</p>
        <p>تتقدم الأمانة الثقافية بلجنة تسيير الجالية السودانية بجدة بهذا المقترح الإستراتيجي لسعادتكم للمناقشة والإجازة وبدء التنفيذ الميداني وحفظه كإرث تنظيمي دائم.</p>
        <p style='text-align: center; font-weight: bold; font-size: 16px; margin-top: 25px; color: #1A365D;'>سائلين الله التوفيق والسداد لما فيه خير العباد والبلاد.</p>
        <p style='text-align: center; font-weight: bold; color: #C5A059; margin-top: 10px;'>،، وتفضلوا بقبول وافر الشكر والتقدير والإمتنان ،،</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style='text-align: center; margin-top: 35px; font-weight: bold; color: #1A365D;'>
        <p style='margin:0; font-size: 16px;'>أمانة الثقافة بلجنة تسيير الجالية السودانية بجدة</p>
        <p style='color: #C5A059; margin: 8px 0; font-size: 18px;'>بابكر عبدالله &nbsp;&nbsp;|&nbsp;&nbsp; وليد البليل</p>
    </div>
    """, unsafe_allow_html=True)

# 6. تذييل الصفحة اللطيف والمستقر بدون تداخلات
st.markdown("<br><hr><p style='text-align: center; color: #64748B; font-size: 13px;'>أمانة الثقافة بلجنة تسيير الجالية السودانية بجدة • مايو 2026م</p>", unsafe_allow_html=True)
