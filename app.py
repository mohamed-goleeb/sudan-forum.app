import streamlit as st

# 1. إعدادات الصفحة الأساسية والهوية البصرية للتطبيق
st.set_page_config(
    page_title="برنامج الأمانة الثقافية - الجالية السودانية بجدة",
    page_icon="🇸🇩",
    layout="wide",
    initial_sidebar_state="expanded"
)

# تخصيص المظهر عبر CSS ليعكس الألوان الملكية، وعلم السودان، والمؤثرات البصرية
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    
    * {
        font-family: 'Cairo', sans-serif;
    }
    .main {
        direction: rtl;
        text-align: right;
        background-color: #FAFAFA;
    }
    div[data-testid="stSidebarUserContent"] {
        direction: rtl;
        text-align: right;
        background-color: #1A365D;
        color: white;
    }
    /* تصميم الهيدر الرئيسي مع العلم */
    .header-container {
        background: linear-gradient(135deg, #1A365D 0%, #2A4D7C 100%);
        padding: 30px;
        border-radius: 12px;
        color: white;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        margin-bottom: 25px;
        border-right: 8px solid #C5A059;
        position: relative;
    }
    .flag-bar {
        height: 6px;
        width: 100%;
        background: linear-gradient(to left, #D21034 33.3%, #FFFFFF 33.3%, #FFFFFF 66.6%, #007229 66.6%);
        border-radius: 3px;
        margin-top: 15px;
    }
    /* العناوين داخل التبويبات */
    h2 {
        color: #1A365D !important;
        border-right: 6px solid #C5A059;
        padding-right: 15px;
        margin-top: 25px;
        margin-bottom: 15px;
        font-weight: bold;
    }
    /* تصميم التبويبات الحديثة */
    .stTabs [data-baseweb="tab"] {
        color: #1A365D;
        font-size: 16px;
        font-weight: bold;
        background-color: #E2E8F0;
        border-radius: 8px 8px 0 0;
        padding: 10px 20px;
        margin-left: 4px;
    }
    .stTabs [aria-selected="true"] {
        color: white !important;
        background-color: #1A365D !important;
        border-bottom-color: #C5A059 !important;
    }
    /* الصناديق التوضيحية الفخمة */
    .premium-box {
        background-color: #ffffff;
        border: 1px solid #E2E8F0;
        border-right: 6px solid #1A365D;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        margin-bottom: 20px;
        transition: transform 0.2s;
    }
    .premium-box:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    }
    .gold-box {
        background-color: #FFFDF5;
        border: 1px solid #FEF3C7;
        border-right: 6px solid #C5A059;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        margin-bottom: 20px;
    }
    /* كرت السايدبار */
    .sidebar-card {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 15px;
        border-radius: 8px;
        border-right: 4px solid #C5A059;
        margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. الهيدر الرئيسي المطور مع العلم الرقمي وتأثير الـ Gradient
st.markdown("""
    <div class='header-container'>
        <h1 style='color: white !important; margin:0; font-size: 28px;'>🇸🇩 منصة برنامج الأمانة الثقافية التفاعلية</h1>
        <p style='color: #E2E8F0; margin: 5px 0 0 0; font-size: 16px;'>لجنة تسيير الجالية السودانية بجدة — الرؤية الإستراتيجية والمناشط للمرحلة القادمة</p>
        <div class='flag-bar'></div>
    </div>
    """, unsafe_allow_html=True)

# 3. شريط جانبي (Sidebar) فخم ومطور بحركات تفاعلية وإحصائيات
with st.sidebar:
    st.markdown("<h2 style='color: white !important; border-right-color: #C5A059; text-align: center;'>🇸🇩 لوحة التحكم</h2>", unsafe_allow_html=True)
    
    # بطاقة ترحيبية دبلوماسية بالسايدبار
    st.markdown("""
    <div class='sidebar-card'>
        <p style='margin:0; font-weight:bold; color: #FFFDF5;'>المرفوع إلى:</p>
        <p style='margin:5px 0 0 0; font-size:13px; color: #E2E8F0;'>سعادة القنصل العام لجمهورية السودان بجدة الموقر، ورئيس وأعضاء لجنة التسيير الموقرين.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 📊 مؤشرات الخطة إحصائياً")
    st.markdown("---")
    
    # حركات حلوة: عرض إحصائيات سريعة بالعدادات (Metrics) في السايدبار
    st.metric(label="🛣️ المسارات الإستراتيجية المعتمدة", value="3 مسارات")
    st.metric(label="🌌 زمن عرض متحدث منصة مَجَرَّة", value="20 دقيقة صارمة")
    st.metric(label="👥 الفئات المستهدفة بالدراسة", value="4 فئات رئيسية")
    
    st.markdown("---")
    st.caption("💻 تم التطوير رقمياً ليعكس حوكمة ومواكبة الأمانة الثقافية 2026م")

# 4. بناء تبويبات العرض (Tabs) الأنيقة
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🎯 المنهجية الإستراتيجية", 
    "👥 الفئات المستهدفة", 
    "🛣️ مسارات العمل والمشروعات", 
    "🌌 منصة مَجَرَّة النوعية", 
    "⚖️ آليات الحوكمة والتوصيات"
])

# التبويب الأول: المنهجية والأهداف
with tab1:
    st.markdown("<h2>1. المنهجية التعريفية والإستراتيجية</h2>", unsafe_allow_html=True)
    st.markdown("""
    يتقدم المكتب الثقافي بلجنة التسيير بخطة عمل رسمية للفترة القادمة، تتضمن أنشطة معرفية، فنية، وتراثية، 
    وتهدف إلى إبراز طاقات المجتمع وتطوير مهاراته من خلال تنفيذ برنامج ثقافي احترافي ناجح يلبي تطلعات المرحلة الانتقالية.
    
    إن المنهجية الإستراتيجية لهذا البرنامج تقوم على **تحديد الأهداف والجمهور المستهدف أولاً**، ومن ثم تصميم المناشط والفعاليات وفقاً للغايات الأساسية للجنة التسيير والتي تنحصر في التالي:
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class='premium-box'>
            <h4 style='color: #1A365D; margin-top:0;'>✨ الغايات المعرفية والتراثية:</h4>
            <ul>
                <li><b>تعزيز المعرفة ونشرها:</b> بث الوعي الثقافي والمعرفي المستمر بين أبناء الجالية السودانية.</li>
                <li><b>إبراز التراث الأصيل:</b> تسليط الضوء على الإرث التراثي السوداني وربط الجيل الناشئ بوطنه وجذوره.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class='gold-box'>
            <h4 style='color: #C5A059; margin-top:0;'>🤝 الغايات المؤسسية والمجتمعية:</h4>
            <ul>
                <li><b>صقل المواهب الوطنية:</b> تقديم الدعم الكامل والبيئة الخصبة لرواد الأعمال والمبتكرين والمبدعين.</li>
                <li><b>تجميع الكيانات والروابط:</b> صهر كافة المكونات تحت مظلة مؤسسية متناغمة تمهيداً لقيام الجالية.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# التبويب الثاني: الفئات المستهدفة
with tab2:
    st.markdown("<h2>2. دراسة الفئات المستهدفة وتحليل البيئة</h2>", unsafe_allow_html=True)
    st.markdown("تلتزم الأمانة الثقافية بدراسة طبيعة واحتياجات الجمهور المستهدف وتصميم برامج متخصصة تلائم كافة المكونات:")
    
    # حركات حلوة: توزيع كروت تفاعلية ملونة لكل فئة مستهدفة
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown("<div class='premium-box' style='text-align:center; border-top: 4px solid #1A365D;'>⚡<br><h4>الشباب والخريجين</h4><p style='font-size:13px; color:#555;'>لتمكينهم وتوجيه طاقاتهم المعرفية والمهنية نحو المستقبل.</p></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='premium-box' style='text-align:center; border-top: 4px solid #C5A059;'>🎨<br><h4>الأطفال والناشئة</h4><p style='font-size:13px; color:#555;'>بناء وحماية الهوية الوطنية في وجدان الأجيال الصاعدة ببلد المقر.</p></div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='premium-box' style='text-align:center; border-top: 4px solid #1A365D;'>🤝<br><h4>الأسر والنساء</h4><p style='font-size:13px; color:#555;'>فعاليات تدمج بين التكافل الاجتماعي والتطوير الاقتصادي ودعم الأسر المنتجة.</p></div>", unsafe_allow_html=True)
    with c4:
        st.markdown("<div class='premium-box' style='text-align:center; border-top: 4px solid #C5A059;'>🎭<br><h4>الكيانات والروابط</h4><p style='font-size:13px; color:#555;'>تفعيل دور الروابط الثقافية والأدبية كشركاء أساسيين لبناء النسيج الموحد.</p></div>", unsafe_allow_html=True)

# التبويب الثالث: المسارات والمشروعات
with tab3:
    st.markdown("<h2>3. المسارات الإستراتيجية والفعاليات التنفيذية المقترحة</h2>", unsafe_allow_html=True)
    st.markdown("لضمان جودة المخرجات وسلاسة الأداء، تترجم الفعاليات الحية (حضورياً داخل منشآت مصرحة) عبر ثلاثة مسارات واضحة:")
    
    # استخدام نظام الـ Expander المطور لعرض مشروعات كل مسار بشكل منسق جداً
    with st.expander("📚 المسار الأول: الصالون الأدبي وملتقيات الإبداع (ندوات ولقاءات حوارية)"):
        st.markdown("""
        * **المسابات الأدبية:** إطلاق مسابقات رسمية في مجالات كتابة وتأليف المقالات، والقصص القصيرة، والرواية، والشعر لتشجيع الإبداع وحصر الطاقات الأدبية في المهجر.
        * **المناشط الفنية والتشكيلية:** تنظيم معارض ومعاهد متخصصة لتعليم وصقل المعارف الفنية في مجالات الرسم، والتصوير الفوتوغرافي، والفنون البصرية، والخط العربي، مع إقامة معارض دورية لعرض أعمال المبدعين السودانيين بجدة.
        * **معارض المهرجانات والكتاب:** تنظيم صالونات للقراءة وزيارة وتنظيم معارض مصغرة للكتاب، لتشجيع القراءة ونشر الوعي الثقافي بين الأسر والشباب.
        """)
        
    with st.expander("🛖 المسار الثاني: ملتقى التراث والفنون الأدائية - مهرجان الهوية (معارض فنية وتراثية)"):
        st.markdown("""
        * **المهرجانات التراثية الحية:** إقامة ملتقيات تراثية مغلقة تشمل عروضاً للفرق الموسيقية التراثية والرقص الشعبي الممثل لكافة أقاليم السودان، لتقديم لوحة وطنية متكاملة تبرز التنوع كعنصر وحدة.
        * **أسواق الحرف اليدوية والطهي:** تنظيم أسواق ومعارض مصاحبة للحرف اليدوية السودانية، المشغولات الجلدية، والخزف، يصاحبها استعراض حي للمأكولات التقليدية لربط الوجدان والأسرة بالثقافة المحلية.
        * **ورش العمل التعليمية للتقاليد:** تنظيم ورش سريعة وموجهة للأطفال تسلط الضوء على عادات وتقاليد المجتمع السوداني في المناسبات والأعياد لترسيخ قيم التكافل العريقة.
        """)
        
    with st.expander("🏛️ المسار الثالث: مشروع المجمع الثقافي / النادي السوداني (ورش تدريبية تفاعلية)"):
        st.markdown("""
        * **فعاليات الأطفال والناشئة:** تخصيص أيام ترفيهية ومعرفية دورية وممنهجة للأطفال، تشمل مسرح الطفل والألعاب التعليمية والمسابقات الثقافية لتعزيز الانتماء للوطن بأساليب محببة وجاذبة.
        * **المحاضرات وجلسات النقاش:** عقد محاضرات دورية مستمرة تستضيف قادة الرأي والفكر لمناقشة آليات تطوير العمل العام، وتوفيق أوضاع الكيانات، وتوطيد العلاقات الاجتماعية الإيجابية.
        """)

# التبويب الرابع: منصة مجرة
with tab4:
    st.markdown("<h2>4. المشروع النوعي المبتكر: منصة 'مَجَرَّة' للكفاءات 🌌</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='gold-box'>
        <p style='font-size: 16px; font-style: italic; margin:0; text-align:center; color: #1A365D;'>
        <b>"مواكبةً لأحدث النظم العالمية في نقل المعرفة، تم ابتكار منصة 'مَجَرَّة' لتكون الحاضنة المعرفية والتنموية الكبرى لأبناء الوطن في المهجر."</b>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col_x, col_y = st.columns(2)
    with col_x:
        st.markdown("""
        <div class='premium-box' style='height: 100%;'>
            <h4 style='color: #1A365D; margin-top:0;'>⏱️ ضوابط منصة العرض والتقديم:</h4>
            <ul>
                <li><b>آلية التنفيذ:</b> يُجهز مسرح القاعة بأحدث التقنيات البصرية والصوتية المناسبة للعروض الاحترافية والملهمة.</li>
                <li><b>المتحدثون:</b> يتم استضافة 6 شخصيات من أرفع الكفاءات السودانية بالمنطقة الغربية (في مجالات الأكاديمية، الهندسة والتقنية، الطب، الإدارة، وريادة الأعمال).</li>
                <li><b>تحدي الـ 20 دقيقة:</b> يُمنح كل متحدث <b>20 دقيقة محددة وصارمة</b>، يستعرض فيها "خلاصة تجربته المهنية والعلمية" ويقدم حلولاً وتوصيات عملية للشباب بعيداً عن السرد الإنشائي.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col_y:
        st.markdown("""
        <div class='premium-box' style='height: 100%;'>
            <h4 style='color: #1A365D; margin-top:0;'>🚀 المعرض المهني المصاحب (دعم رواد الأعمال):</h4>
            <p>على هامش المنصة، يُقام معرض متكامل مخصص لرواد الأعمال الشباب وأصحاب المشاريع والابتكارات والمهن الحرة.</p>
            <p><b>الأهداف والمخرجات المتوقعة:</b></p>
            <ul>
                <li>تبادل بطاقات العمل والخبرات المهنية الحرة.</li>
                <li>تطوير وترسيخ المعرفة وبناء شبكات تواصل قوية.</li>
                <li>ترسيخ دور الجالية كحاضنة اقتصادية ومعرفية داعمة ومطورة لأبنائها وبناتها في المهجر.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# التبويب الخامس: الحوكمة والخاتمة والتوصيات
with tab5:
    st.markdown("<h2>5. آليات التفعيل، الحوكمة والتوصيات</h2>", unsafe_allow_html=True)
    
    col_h1, col_h2 = st.columns(2)
    with col_h1:
        st.markdown("""
        <div class='premium-box'>
            <h4 style='color: #1A365D; margin-top:0;'>🎟️ 1. بطاقة العضوية الثقافية (المتابعة والأثر):</h4>
            <p>إصدار بطاقات حضور رمزية تسلسلية للمشاركين في الفعاليات والورش، تسهم في قياس مدى التزام وتفاعل العضوية، وتمنح ميزات تفضيلية للملتزمين بالمسارات التدريبية في الفعاليات الختامية للجالية.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='premium-box'>
            <h4 style='color: #1A365D; margin-top:0;'>⚖️ 3. الحوكمة والتنفيذ الإداري المشترك:</h4>
            <p>تخضع كافة الفعاليات والمشروعات لإشراف وتنسيق مباشر من الأمانة الثقافية بلجنة التسيير، وبالتنسيق الكامل والمسبق مع القنصلية العامة لجمهورية السودان بجدة لضمان الالتزام بكافة الضوابط والأنظمة المتبعة.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_h2:
        st.markdown("""
        <div class='premium-box' style='height: 92%;'>
            <h4 style='color: #1A365D; margin-top:0;'>📥 2. صندوق "صوت المواطن" (الشفافية الكاملة):</h4>
            <p>صندوق مقترحات رسمي وموثق يتنقل بين كافة المشروعات والفعاليات الحضرية على الأرض.</p>
            <p>يتيح هذا الصندوق لأبناء وبنات الجالية تقديم أفكارهم، مرئياتهم، ورؤاهم المكتوبة مباشرة إلى لجنة التسيير؛ إيماناً بمبدأ الشفافية والمشاركة الجماعية الواعية في صنع القرار الثقافي والمجتمعي.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("<h3>📝 6. الخاتمة والتوصيات الرسمية</h3>", unsafe_allow_html=True)
    st.markdown("""
    إن هذا البرنامج الثقافي المتكامل بمساراته الواضحة وأهدافه المحددة ومستهدفاته المدروسة، يمثل الركيزة الأساسية واللبنة الأولى لصياغة مستقبل جالية نموذجية، متلاحمة، ورائدة تعكس الوجه المشرق للسودان وأبنائه في المملكة العربية السعودية.
    
    تتقدم الأمانة الثقافية بلجنة التسيير بهذا المقترح الإستراتيجي لسعادتكم ولللجنة الموقرة للمناقشة والإجازة، سائلين الله التوفيق والسداد لما فيه خير العباد والبلاد.
    
    **وتفضلوا بقبول وافر الشكر والتقدير،،**
    """)
    
    # التوقيعات الرسمية المعتمدة
    st.markdown("""
    <div style='text-align: center; margin-top: 30px; font-weight: bold; color: #1A365D;'>
        <p style='margin:0;'>أمانة الثقافة بلجنة تسيير الجالية السودانية بجدة</p>
        <p style='color: #C5A059; margin:5px 0;'>بابكر عبد الله &nbsp;|&nbsp; وليد البليل</p>
        <p style='font-size: 12px; color: #777; margin:0;'>مايو 2026م</p>
    </div>
    """, unsafe_allow_html=True)