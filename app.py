import streamlit as st
import folium
from streamlit_folium import folium_static

# 1. إعدادات الصفحة الأساسية والهوية البصرية الكونية
st.set_page_config(
    page_title="برنامج الأمانة الثقافية - الجالية السودانية بجدة",
    page_icon="🇸🇩",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. حقن CSS متقدم لإجبار الألوان الرسمية وإصلاح الـ Dark Mode وعرض النصوص بدقة متناهية
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
    .gold-luxury-card h4 {
        color: #C5A059 !important;
        font-weight: 700 !important;
        margin-top: 0 !important;
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
    
    # قائمة التنقل المتطابقة تماماً مع بنود فهرس المستند المعتمد
    menu_selection = st.radio(
        "📌 انتقل بين بنود البرنامج:",
        [
            "1. المقدمة والمنهجية الإستراتيجية",
            "2. دراسة الفئات المستهدفة",
            "📍 خريطة الفعاليات الحية بجدة",
            "3. المسارات الإستراتيجية",
            "4. المشروعات والفعاليات التنفيذية",
            "5. منصة 'مَجَرَّة' للكفاءات",
            "6. آليات التفعيل والحوكمة",
            "7. الخاتمة والتوصيات"
        ]
    )
    
    st.markdown("---")
    st.markdown("<h4 style='color: #C5A059 !important;'>📊 مؤشر تتبع الخطة</h4>", unsafe_allow_html=True)
    
    # مؤشرات ديناميكية ذكية للتفاعل الفوري أثناء النقاش
    if menu_selection == "1. المقدمة والمنهجية الإستراتيجية":
        st.metric("الغايات الأساسية", "4 غايات")
    elif menu_selection == "2. دراسة الفئات المستهدفة":
        st.metric("الفئات الحيوية المحددة", "4 فئات")
    elif menu_selection == "📍 خريطة الفعاليات الحية بجدة":
        st.metric("الجغرافية الرقمية", "ميداني / حيا")
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

# 5. عرض المحتوى الحرفي المعتمد ديناميكياً بناءً على اختيار السايدبار

# بند 1: المقدمة التعريفية والمنهجية الإستراتيجية
if menu_selection == "1. المقدمة والمنهجية الإستراتيجية":
    st.markdown("<h2>1. المقدمة التعريفية والمنهجية الإستراتيجية</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='luxury-card' style='border-right-color: #C5A059;'>
        <p style='font-size: 16px; font-weight: bold; color: #1A365D; text-align: left;'>السادة رئيس وأعضاء لجنة تسيير الجالية السودانية بجدة : الموقرين</p>
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

# بند 2: دراسة الفئات المستهدفة وتحليل البيئة
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

# إضافة الخريطة التفاعلية الفخمة لربط المشاريع وعمل الـ WOW
elif menu_selection == "📍 خريطة الفعاليات الحية بجدة":
    st.markdown("<h2>📍 التوزيع الجغرافي الرقمي للمشروعات والفعاليات الحية بمدينة جدة</h2>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:16px;'>تحقيقاً للمواكبة الحضرية، تظهر الخريطة أدناه نطاق تفعيل المشروعات التراثية والندوات المقترحة على أرض الواقع بمدينة جدة عبر مسارات مترابطة:</p>", unsafe_allow_html=True)
    
    jeddah_center = [21.5433, 39.1728]
    m = folium.Map(location=jeddah_center, zoom_start=12, tiles="CartoDB positron")
    
    # مواقع افتراضية إستراتيجية تمثل تنوع المناشط المذكورة في خطتك
    locations = [
        {"name": "📍 الصالون الأدبي وملتقيات الإبداع (الندوات والمناشط الفنية)", "coord": [21.5165, 39.1601], "desc": "معارض الفنون البصرية والخط العربي واللقاءات الحوارية الدورية."},
        {"name": "📍 ملتقى التراث والفنون الأدائية (مهرجان الهوية)", "coord": [21.6147, 39.1032], "desc": "المهرجانات التراثية المغلقة، أسواق الحرف اليدوية، والطهي الحي التقليدي لأقاليم السودان."},
        {"name": "📍 مشروع المجمع الثقافي / النادي السوداني", "coord": [21.4930, 39.2311], "desc": "ورش العمل التفاعلية، فعاليات الأطفال والناشئة، ومسرح الطفل المنهجي."},
        {"name": "📍 المقر التنفيذي الرقمي ومنصة مَجَرَّة للكفاءات", "coord": [21.5411, 39.1655], "desc": "قاعة المسرح التكنولوجي لاستضافة أرفع الكفاءات العلمية ورواد الأعمال."}
    ]
    
    for loc in locations:
        folium.Marker(
            location=loc["coord"],
            popup=f"<b>{loc['name']}</b><br>{loc['desc']}",
            tooltip=loc["name"],
            icon=folium.Icon(color="darkblue", icon="info-sign")
        ).add_to(m)
        
    path_coordinates = [[21.6147, 39.1032], [21.5165, 39.1601], [21.5411, 39.1655], [21.4930, 39.2311]]
    folium.PolyLine(locations=path_coordinates, color="#C5A059", weight=4, opacity=0.8, tooltip="جسر المعرفة الموحد").add_to(m)
    
    folium_static(m, width=1100, height=500)
    st.info("💡 الخريطة تفاعلية بالكامل، يمكنك تكبيرها والضغط على أي علامة لمشاهدة المشروع المقترن بها المذكور في خطتك.")

# بند 3: المسارات الإستراتيجية للبرنامج الثقافي
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

# بند 4: المشروعات والفعاليات التنفيذية المقترحة
elif menu_selection == "4. المشروعات والفعاليات التنفيذية":
    st.markdown("<h2>4. المشروعات والفعاليات التنفيذية المقترحة</h2>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:16px;'>تنطلق الفعاليات الحية لتترجم المسارات الإستراتيجية إلى مشروعات ملموسة على النحو التالي :</p>", unsafe_allow_html=True)
    
    tab_a, tab_b, tab_c = st.tabs(["أ. الصالون الأدبي وملتقيات الإبداع", "ب. ملتقى التراث والفنون الأدائية (مهرجان الهوية)", "ج. مشروع المجمع الثقافي / النادي السوداني"])
    
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
            <ul>
                <li><b>فعاليات الأطفال والناشئة:</b> تخصيص أيام ترفيهية ومعرفية دورية وممنهجة للأطفال، تشمل مسرح الطفل والألعاب التعليمية والمسابقات الثقافية لتعزيز الانتماء للوطن بأساليب محببة وجاذبة .</li>
                <li><b>المحاضرات وجلسات النقاش:</b> عقد محاضرات دورية مستمرة تستضيف قادة الرأي والفكر لمناقشة آليات تطوير العمل العام وتوفيق أوضاع الكيانات وتوطيد العلاقات الاجتماعية الإيجابية.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# بند 5: المشروع النوعي المبتكر: منصة "مَجَرَّة" للكفاءات
elif menu_selection == "5. منصة 'مَجَرَّة' للكفاءات":
    st.markdown("<h2>5. المشروع النوعي المبتكر: منصة \"مَجَرَّة\" للكفاءات</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='gold-luxury-card'>
        <p style='font-size: 16px; font-style: italic; text-align: center; margin: 0;'>
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

# بند 6: آليات التفعيل ( الحوكمة والمتابعة )
elif menu_selection == "6. آليات التفعيل والحوكمة":
    st.markdown("<h2>6. آليات التفعيل ( الحوكمة والمتابعة )</h2>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:16px;'>لضمان جودة التنفيذ وتحقيق أعلى درجات الالتزام من القواعد الجماهيرية وفق اللوائح المرعية:</p>", unsafe_allow_html=True)
    
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

# بند 7: الخاتمة والتوصيات الرسمية والتواقيع
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
    
    # التوقيعات الرسمية الحرفية كما وردت بالمستند الجديد
    st.markdown("""
    <div style='text-align: center; margin-top: 40px; font-weight: bold; color: #1A365D;'>
        <p style='margin:0; font-size: 16px;'>امانة الثقافة بلجنة تسيير الجالية السودانية بجدة</p>
        <p style='color: #C5A059; margin: 8px 0; font-size: 18px;'>بابكر عبدالله &nbsp;&nbsp;|&nbsp;&nbsp; وليد البليل</p>
    </div>
    """, unsafe_allow_html=True)
