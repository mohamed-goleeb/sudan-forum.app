import streamlit as st

# 1. إعدادات الصفحة الأساسية والهوية البصرية بدون سايدبار
st.set_page_config(
    page_title="برنامج الأمانة الثقافية - الجالية السودانية بجدة",
    page_icon="🇸🇩",
    layout="wide"
)

# 2. حقن CSS نقي ومستقر لحل مشكلة التعليق وضمان جودة الألوان
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap');
    
    /* تثبيت الخط والاتجاه الأساسي للمحتوى */
    html, body, [data-testid="stAppViewContainer"], .main {
        font-family: 'Cairo', sans-serif !important;
        background-color: #F4F6F9 !important;
        color: #1A365D !important;
        direction: rtl !important;
        text-align: right !important;
    }
    
    /* جعل حاوية المحتوى الرئيسي تدعم القراءة من اليمين لليسار بشكل طبيعي */
    .block-container {
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
    }
    .cosmic-header h1 {
        color: #FFFDF5 !important;
        font-weight: 800 !important;
        font-size: 26px !important;
        margin: 0 0 8px 0 !important;
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
    }
    .luxury-card h4 {
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
    
    .gold-luxury-card {
        background-color: #FFFDF5 !important;
        border: 1px solid #FEF3C7 !important;
        border-right: 6px solid #C5A059 !important;
        padding: 20px !important;
        border-radius: 10px !important;
        box-shadow: 0 4px 15px rgba(197, 160, 89, 0.06) !important;
        margin-bottom: 20px !important;
        text-align: right !important;
    }

    /* تخصيص التبويبات لتكون آمنة ومتوافقة */
    div[data-testid="stTabs"] {
        direction: rtl !important;
    }
    div[data-testid="stTabs"] button[data-baseweb="tab"] {
        font-family: 'Cairo', sans-serif !important;
        font-size: 15px !important;
        font-weight: 700 !important;
        color: #64748B !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. الهيدر الموحد الفاخر للهوية الرسمية
st.markdown("""
    <div class='cosmic-header'>
        <h1>لجنة تسيير الجالية السودانية بجدة (ملتقى السودان)</h1>
        <p style='margin: 0; font-size: 16px; color: #CBD5E1; font-weight: bold;'>برنامج الأمانة الثقافية — الرؤية الإستراتيجية والمناشط للمرحلة القادمة</p>
        <div class='sudan-flag-line'></div>
    </div>
    """, unsafe_allow_html=True)

# 4. الفهرس الرقمي العلوي كبديل سريع ومستقر للسايدبار
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

# 5. استعراض الفصول بناءً على الاختيار بدون أي تعليق في الميثودز
if menu_selection == "1. المقدمة والمنهجية الإستراتيجية":
    st.markdown("<h2>1. المقدمة التعريفية والمنهجية الإستراتيجية</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class='luxury-card' style='border-right-color: #C5A059;'>
        <p style='font-size: 16px; font-weight: bold; color: #1A365D;'>السادة رئيس وأعضاء لجنة تسيير الجالية السودانية بجدة : الموقرين</p>
        <p>يتقدم المكتب الثقافي بلجنة التسيير بخطة عمل رسمية للفترة القادمة ، تتضمن أنشطة معرفية فنية وتراثية وتهدف إلى إبراز طاقات المجتمع وتطوير مهاراته من خلال تنفيذ برنامج ثقافي احترافي ناجح يُلبي تطلعات المرحلة الانتقالية.</p>
        <p>إن المنهجية الإستراتيجية لهذا البرنامج تقوم على تحديد الأهداف والجمهور المستهدف أولاً، ومن ثمَّ تصميم المناشط والفعاليات وفقاً للغايات الأساسية للجنة التسيير والتي تنحصر في تعزيز المعرفة، وإبراز التراث، وصقل المواهب الوطنية.</p>
    </div>
    """, unsafe_allow_html=True)

elif menu_selection == "2. دراسة الفئات المستهدفة وتحليل الواقع":
    st.markdown("<h2>2. دراسة الفئات المستهدفة وتحليل البيئة</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class='luxury-card'><h4>1. الشباب والخريجين</h4><p>لتمكينهم وتوجيه طاقاتهم المعرفية والمهنية لصناعة المستقبل المشرق.</p></div>
    <div class='luxury-card'><h4>2. الأطفال والناشئة</h4><p>عبر مناشط مخصصة لبناء الهوية الوطنية وحمايتها وغرس القيم السودانية الأصيلة.</p></div>
    <div class='luxury-card'><h4>3. الأسر والنساء</h4><p>فعاليات تدمج بين التكافل الاجتماعي والتطوير الاقتصادي للأسر المنتجة.</p></div>
    <div class='luxury-card'><h4>4. الكيانات والروابط الثقافية</h4><p>الروابط الثقافية والأدبية كشركاء أساسيين في بناء النسيج الاجتماعي الموحد.</p></div>
    """, unsafe_allow_html=True)

elif menu_selection == "3. المسارات الإستراتيجية للبرنامج":
    st.markdown("<h2>3. المسارات الإستراتيجية للبرنامج الثقافي</h2>", unsafe_allow_html=True)
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
            <p><b>• المناشط الفنية والتشكيلية:</b> تنظيم معارض ومعاهد متخصصة لتعليم وصقل المعارف الفنية في مجالات الرسم، التصوير الفوتوغرافي، الفنون البصرية، والخط العربي بجدة.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with tab_b:
        st.markdown("""
        <div class='luxury-card'>
            <h4>🎪 حزمة ملتقى التراث والفنون الأدائية (مهرجان الهوية)</h4>
            <p><b>• المهرجانات التراثية الحية:</b> إقامة ملتقيات تراثية مغلقة تشمل عروضاً للفرق الموسيقية التراثية والرقص الشعبي الممثل لكافة أقاليم السودان.</p>
            <p><b>• أسواق الحرف اليدوية والطهي:</b> تنظيم معارض مصاحبة للحرف اليدوية السودانية والمشغولات الجلدية لتنمية ودعم الأسر المنتجة.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with tab_c:
        st.markdown("""
        <div class='luxury-card'>
            <h4>🏰 مشروع "المجمع الثقافي / النادي السوداني"</h4>
            <p><b>• فعاليات الأطفال والناشئة:</b> تخصيص أيام ترفيهية ومعرفية دورية وممنهجة للأطفال، تشمل مسرح الطفل والألعاب التعليمية والمسابقات الثقافية لتعزيز الانتماء للوطن.</p>
        </div>
        """, unsafe_allow_html=True)

elif menu_selection == "5. منصة 'مَجَرَّة' للكفاءات (المشروع الأساسي)":
    st.markdown("<h2>5. المشروع النوعي المبتكر: منصة \"مَجَرَّة\" للكفاءات</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='gold-luxury-card'>
        <p style='font-size: 16px; font-style: italic; text-align: center; margin: 0; color: #C5A059; font-weight: bold;'>
        "مواكبة لأحدث النظم العالمية في نقل المعرفة، تم ابتكار منصة 'مَجَرَّة' لتكون الحاضنة المعرفية والتنموية الكبرى لأبناء الوطن في المهجر بالمنطقة الغربية تشبهاً بنظام منصات TEDx العالمية."
        </p>
    </div>
    <div class='luxury-card'>
        <h4>⚙️ الآلية وضوابط التقديم الصارمة:</h4>
        <p>• <b>آلية التنفيذ والتقديم:</b> يُجهز مسرح القاعة بأحدث التقنيات البصرية والصوتية المناسبة للعروض التقديمية الاحترافية والملهمة.</p>
        <p>• <b>المتحدثون والعلماء:</b> يتم استضافة 6 شخصيات من أرفع الكفاءات السودانية بالمنطقة الغربية (الأكاديمية، الهندسة، التقنية، الطب، الإدارة، وريادة الأعمال).</p>
        <p>• <b>ضوابط المنصة الزمنية:</b> يُمنح كل متحدث <b>20 دقيقة محددة وصارمة</b>، يستعرض فيها "خلاصة تجربته المهنية والعلمية" بعيداً عن السرد الإنشائي التقليدي.</p>
    </div>
    <div class='luxury-card'>
        <h4>🚀 المعرض المهني المصاحب (دعم رواد الأعمال):</h4>
        <p>على هامش المنصة يُقام معرض متكامل لرواد الأعمال الشباب وأصحاب المشاريع الناشئة والابتكارات والمهن الحرة بهدف إتاحة فرص التشبيك والتواصل، وترسيخ دور الجالية كحاضنة اقتصادية ومعرفية ملموسة.</p>
    </div>
    """, unsafe_allow_html=True)

elif menu_selection == "6. آليات التفعيل والحوكمة المستدامة":
    st.markdown("<h2>6. آليات التفعيل ( الحوكمة والضبط الإداري المرجعي )</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class='luxury-card'>
        <h4>🎟️ 1. بروتوكول التسليم والديمومة المؤسسية (الاستمرارية)</h4>
        <p>تُعتمد هذه الخطة كأصل وثائقي أساسي للأمانة الثقافية في "لجنة تيسير الجالية السودانية بجدة مايو 2026"، وتلتزم الأمانة بتسليم كافة ملفاتها التقنية والبيانات المستخرجة من المنصات الرقمية إلى رئيس لجنة التسيير، لتبدأ الإدارات المتعاقبة من حيث انتهت دون الحاجة لتأسيس حراك من الصفر.</p>
    </div>
    <div class='luxury-card'>
        <h4>📥 2. صندوق "صوت المواطن" للشفافية</h4>
        <p>تفعيل صندوق مقترحات رسمي وموثق يتنقل بين كافة المشروعات والفعاليات، ويتيح لأبناء الجالية تقديم أفكارهم ورؤاهم المكتوبة مباشرة إلى لجنة التسيير، إيماناً بمبدأ الشفافية والمشاركة الجماعية.</p>
    </div>
    """, unsafe_allow_html=True)

else:
    st.markdown("<h2>7. الخاتمة والتوصيات</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class='luxury-card' style='border-right-color: #C5A059;'>
        <p>إن هذا البرنامج الثقافي المتكامل بمساراته الواضحة وأهدافه المحددة ومستهدفاته المدروسة، يمثل الركيزة الأساسية واللبنة الأولى لصياغة مستقبل جالية نموذجية ومتلاحمة ورائدة تعكس الوجه المشرق للسودان وأبنائه.</p>
        <p style='text-align: center; font-weight: bold; font-size: 16px; margin-top: 25px; color: #1A365D;'>سائلين الله التوفيق والسداد لما فيه خير العباد والبلاد.</p>
        <p style='text-align: center; font-weight: bold; color: #C5A059; margin-top: 10px;'>،، وتفضلوا بقبول وافر الشكر والتقدير والإمتنان ،،</p>
    </div>
    <div style='text-align: center; margin-top: 35px; font-weight: bold; color: #1A365D;'>
        <p style='margin:0; font-size: 16px;'>أمانة الثقافة بلجنة تسيير الجالية السودانية بجدة</p>
        <p style='color: #C5A059; margin: 8px 0; font-size: 18px;'>بابكر عبدالله &nbsp;&nbsp;|&nbsp;&nbsp; وليد البليل</p>
    </div>
    """, unsafe_allow_html=True)

# 6. تذييل الصفحة
st.markdown("<br><hr><p style='text-align: center; color: #64748B; font-size: 13px;'>أمانة الثقافة بلجنة تسيير الجالية السودانية بجدة • مايو 2026م</p>", unsafe_allow_html=True)
