import streamlit as st
import folium
from streamlit_folium import folium_static

# 1. إعدادات الصفحة الأساسية والهوية البصرية الكونية
st.set_page_config(
    page_title="منصة برنامج الأمانة الثقافية التفاعلية",
    page_icon="🇸🇩",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. حقن CSS متقدم لإجبار الألوان الفخمة وإصلاح مشاكل الـ Dark Mode وعرض النصوص بوضوح مبهر
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
    
    /* تعديل السايدبار ليكون فخماً ومظلماً مع خطوط ذهبية */
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
        font-size: 32px !important;
        margin: 0 0 10px 0 !important;
        border: none !important;
        padding: 0 !important;
    }
    
    /* علم السودان الجمالي السفلي */
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

    /* تجميل أزرار الراديو في السايدبار لتبدو كقائمة ملاحية احترافية */
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

# 3. الهيدر الكوني الموحد في الشاشة الرئيسية
st.markdown("""
    <div class='cosmic-header'>
        <h1>🏛️ نظام العرض التفاعلي لبرنامج الأمانة الثقافية</h1>
        <p style='margin: 0; font-size: 16px; color: #CBD5E1;'>لجنة تسيير الجالية السودانية بجدة — نسخة الإجازة والمناقشة الرسمية لعام 2026م</p>
        <div class='sudan-flag-line'></div>
    </div>
    """, unsafe_allow_html=True)

# 4. بناء السايدبار الذكي المطور كـ (Control Panel) لانبهار فوري
with st.sidebar:
    st.markdown("<div style='text-align: center; padding: 10px;'><h2 style='color: #C5A059 !important; margin:0;'>🇸🇩 لوحة القيادة</h2></div>", unsafe_allow_html=True)
    st.markdown("---")
    
    # محرك التنقل الرئيسي في الموقع
    menu_selection = st.radio(
        "🎯 انتقل بين محاور الخطة:",
        [
            "🧭 الرؤية والمنهجية الإستراتيجية",
            "👥 دراسة وفئات الجمهور",
            "🗺️ خريطة الفعاليات الحية بجدة",
            "🛣️ المسارات والمشروعات الستة",
            "🌌 منصة مَجَرَّة للكفاءات",
            "⚖️ أنظمة الحوكمة والتوصيات"
        ]
    )
    
    st.markdown("---")
    st.markdown("<h4 style='color: #C5A059 !important;'>📊 إحصائيات سريعة للقسم الحالي</h4>", unsafe_allow_html=True)
    
    # عرض إحصائيات ديناميكية تتغير حسب اختيار المستخدم للحركات التفاعلية
    if menu_selection == "🧭 الرؤية والمنهجية الإستراتيجية":
        st.metric("الغايات الاستراتيجية", "4 غايات كبرى")
    elif menu_selection == "👥 دراسة وفئات الجمهور":
        st.metric("المكونات المستهدفة", "4 فئات حيوية")
    elif menu_selection == "🗺️ خريطة الفعاليات الحية بجدة":
        st.metric("نطاق الجغرافية الرقمية", "عروس البحر الأحمر")
    elif menu_selection == "🛣️ المسارات والمشروعات الستة":
        st.metric("المدى الزمني للتنفيذ", "6 أشهر حضورية")
    elif menu_selection == "🌌 منصة مَجَرَّة للكفاءات":
        st.metric("الزمن الصارم للعرض", "20 دقيقة لكل عالم")
    else:
        st.metric("مبادئ الشفافية المطبقة", "100%")

    st.markdown("---")
    st.caption("💻 المكتب الثقافي • تم التطوير الرقمي لعام 2026م")

# 5. معالجة المحتوى الديناميكي بناءً على خيار لوحة التحكم الجانبية

# القسم الأول: الرؤية والمنهجية
if menu_selection == "🧭 الرؤية والمنهجية الإستراتيجية":
    st.markdown("<h2>1. المنهجية التعريفية والإستراتيجية للبرنامج الثقافي</h2>", unsafe_allow_html=True)
    st.markdown("""
    تتقدم الأمانة الثقافية بلجنة التسيير بخطة عمل تفاعلية رسمية للمرحلة القادمة، تتضمن أنشطة معرفية وفنية وتراثية متكاملة [cite: 136]، 
    تستند على إبراز طاقات المجتمع وتطوير مهاراته وتلبية تطلعات المرحلة الانتقالية[cite: 136, 137].
    تعتمد المنهجية على **تحديد الأهداف والجمهور أولاً**، ومن ثم صياغة الفعاليات تلبيةً للغايات التالية[cite: 138]:
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class='luxury-card'>
            <h4>✨ الغايات المعرفية والتراثية الأصيلة</h4>
            <ul>
                <li><b>تعزيز المعرفة ونشرها:</b> بث الوعي الثقافي والمعرفي المستمر بين أبناء وبنات الجالية[cite: 144].</li>
                <li><b>إبراز الإرث الثقافي الأصيل:</b> تسليط الضوء على العمق التراثي السوداني وربط الجيل الناشئ بوطنه[cite: 144].</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class='gold-luxury-card'>
            <h4>🤝 الغايات المؤسسية والدمج المجتمعي</h4>
            <ul>
                <li><b>صقل المواهب الوطنية الحرة:</b> تقديم الدعم الكامل لرواد الأعمال، المبتكرين، والمبدعين في بلد المقر[cite: 145].</li>
                <li><b>تجميع الكيانات والروابط:</b> صهر كافة المكونات السودانية بجدة تحت مظلة مؤسسية متناغمة تمهيداً لقيام الجالية[cite: 145].</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# القسم الثاني: الفئات المستهدفة (تم إصلاح الألوان تماماً والخطوط واضحة جداً)
elif menu_selection == "👥 دراسة وفئات الجمهور":
    st.markdown("<h2>2. دراسة الفئات المستهدفة وتحليل البيئة المحيطة</h2>", unsafe_allow_html=True)
    st.markdown("تلتزم الأمانة الثقافية بدراسة طبيعة واحتياجات الجمهور بدقة وتصميم برامج متخصصة تلائمهم[cite: 147]:")
    
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown("<div class='luxury-card' style='text-align:center;'>⚡<br><br><h4>الشباب والخريجين</h4><p style='font-size:13px;'>تمكين وتوجيه الطاقات المعرفية والمهنية نحو الريادة والمستقبل[cite: 148].</p></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='luxury-card' style='text-align:center;'>🎨<br><br><h4>الأطفال والناشئة</h4><p style='font-size:13px;'>بناء وحماية الهوية الوطنية وتثبيتها في وجدان أجيال المهاجر[cite: 149].</p></div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='luxury-card' style='text-align:center;'>👩‍نطاق<br><br><h4>الأسر والنساء</h4><p style='font-size:13px;'>دمج التكافل الاجتماعي بالتطوير الاقتصادي ودعم مشاريع الأسر المنتجة[cite: 150].</p></div>", unsafe_allow_html=True)
    with c4:
        st.markdown("<div class='luxury-card' style='text-align:center;'>🎭<br><br><h4>الكيانات والروابط</h4><p style='font-size:13px;'>تفعيل الروابط الثقافية والأدبية كشركاء أصيلين لبناء النسيج الموحد[cite: 151].</p></div>", unsafe_allow_html=True)

# القسم الثالث: خريطة جدة التفاعلية الحية الفخمة بالمسارات والمواقع
elif menu_selection == "🗺️ خريطة الفعاليات الحية بجدة":
    st.markdown("<h2>📍 الجغرافية الرقمية التفاعلية لمواقع ومسارات الفعاليات بجدة</h2>", unsafe_allow_html=True)
    st.markdown("تحقيقاً للانبهار والـ **WOW** أمام اللجنة، هذه خريطة رقمية حية مبنية لمدينة جدة توضح النطاق الجغرافي المقترح لتنفيذ مشروعات وفعاليات الأمانة الثقافية على أرض الواقع:")
    
    # إحداثيات مركز مدينة جدة
    jeddah_center = [21.5433, 39.1728]
    
    # بناء الخريطة باستخدام Folium وتخصيص شكل فخم ومسارات متقاطعة
    m = folium.Map(location=jeddah_center, zoom_start=12, tiles="CartoDB positron")
    
    # إضافة معالم ونقاط الفعاليات على الخريطة
    locations = [
        {"name": "📍 الموقع الأول: تدشين كرنفال شارع النيل (الواجهة البحرية بجدة)", "coord": [21.6147, 39.1032], "desc": "تحويل المساحة المفتوحة لمحاكاة حية لشارع النيل بالخرطوم[cite: 90]."},
        {"name": "📍 الموقع الثاني: ملتقى الرأي السديد والجبنة (منطقة الحمراء والقاعات)", "coord": [21.5165, 39.1601], "desc": "صالون الحوار الفكري الحر وتوفيق أوضاع الكيانات[cite: 92, 178]."},
        {"name": "📍 الموقع الثالث: يوم الأسرة الكبير ومطبخ الجالية (استراحات الفيحاء/شمال جدة)", "coord": [21.4930, 39.2311], "desc": "تحدي الأقاليم وطبخ الأكل الشعبي لايف مع خيمة الحكواتي[cite: 101, 103, 104]."},
        {"name": "📍 الموقع الرابع: المقر الإداري وحاضنة منصة مَجَرَّة للكفاءات", "coord": [21.5411, 39.1655], "desc": "موقع مسرح العرض التقني المجهز لاستضافة العقول القيادية[cite: 113, 114]."}
    ]
    
    for loc in locations:
        folium.Marker(
            location=loc["coord"],
            popup=f"<b>{loc['name']}</b><br>{loc['desc']}",
            tooltip=loc["name"],
            icon=folium.Icon(color="darkblue", icon="info-sign")
        ).add_to(m)
        
    # رسم خط برمجى مضيء يربط الفعاليات ببعضها ليعبر عن "جسر الوجدان والمعرفة الموحد"
    path_coordinates = [[21.6147, 39.1032], [21.5165, 39.1601], [21.5411, 39.1655], [21.4930, 39.2311]]
    folium.PolyLine(locations=path_coordinates, color="#C5A059", weight=4, opacity=0.8, tooltip="جسر الوفاق الثقافي الموحد").add_to(m)
    
    # عرض الخريطة داخل ستريم ليت
    folium_static(m, width=1100, height=500)
    st.info("💡 تحريك الخريطة بالماوس والضغط على النقاط الزرقاء يعرض لك تفاصيل الفعالية وفكرتها الواردة بالمستند فوراً! [cite: 90, 92, 103, 113]")

# القسم الرابع: المسارات والمشروعات الستة بالتفصيل
elif menu_selection == "🛣️ المسارات والمشروعات الستة":
    st.markdown("<h2>3. المسارات الإستراتيجية والمشروعات التنفيذية الممتدة (6 أشهر حضورية)</h2>", unsafe_allow_html=True)
    st.markdown("ينقسم البرنامج التنفيذي على الأرض لترجمة المسارات الإستراتيجية إلى لوحة وطنية موحدة متكاملة[cite: 154, 168]:")
    
    with st.expander("🎪 الشهر الأول والثاني: صالون الإبداع والكرنفال التفاعلي"):
        st.markdown("""
        * **كرنفال شارع النيل بجدة:** تحويل ساحة مفتوحة مجهزة لمحاكاة حية لشارع النيل بالخرطوم، مع زفة شعبية موحدة لكسر الجليد وتجميع الروابط[cite: 90, 91].
        * **ملتقى الرأي السديد والجبنة:** جلسات حوارية على طاولات مستديرة بنكهة القهوة السودانية لحل التحديات الإدارية بروح أخوية[cite: 93, 95].
        """)
        
    with st.expander("🎭 الشهر الثالث والرابع: ليلة الأوبريت البصري ومهرجان الطهي الحي للأقاليم"):
        st.markdown("""
        * **مسرح المقهورين التفاعلي:** سكيتش كوميدي ساخر من تمثيل شباب الجالية لتفكيك أزمات التشرذم ودعوة القادة لمشاركة الحلول ارتجالياً على المسرح[cite: 98, 100].
        * **تحدي الأقاليم والطهي الحي:** يوم عائلي ينقسم جغرافياً (خيم الشرق، الغرب، الوسط، الشمال) لطبخ الأكلات الشعبية "لايف" وتتوسطه خيمة الحكواتي للأطفال[cite: 101, 103, 104].
        """)
        
    with st.expander("🏆 الشهر السادس: حفل الحصاد وتوقيع ميثاق الوفاق الأكبر"):
        st.markdown("""
        * **أوبريت الملحمة الوطنية:** حفل ختامي ضخم يجمع كافة المجموعات الفنية بجدة في فرقة موسيقية موحدة[cite: 108, 109].
        * **جدارية البصمة والتوقيع التاريخي:** صعود رؤساء الكيانات والروابط علناً للتوقيع والبصم على جدارية خشبية فخمة تحمل اسم "ميثاق وفاق أهل السودان بجدة" لإعلان قيام الجالية[cite: 110].
        """)

# القسم الخامس: منصة مجرة الفريدة
elif menu_selection == "🌌 منصة مَجَرَّة للكفاءات":
    st.markdown("<h2>4. المشروع النوعي المبتكر الحاضن: منصة 'مَجَرَّة' للكفاءات</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='gold-luxury-card'>
        <p style='font-size: 16px; font-style: italic; text-align:center; margin:0;'>
        "مواكبةً للنظم العالمية الفاخرة، يُمثل كل عالم أو بروفيسور أو رائد أعمال سوداني متميز بجدة 'نجماً ساطعاً في مجاله'، وتأتي منصة مَجَرَّة لتجمع النجوم في فلك تنموي موحد يخدم قضايا الجالية[cite: 112]."
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("""
        <div class='luxury-card' style='height: 100%;'>
            <h4>📐 مواصفات المسرح والضوابط الصارمة</h4>
            <ul>
                <li><b>التصميم البصري للمسرح:</b> يُصمم بإضاءة مبهرة تمنح شعور الفضاء الكوني الشاسع مع بقعة ضوء مركزية تركز على المتحدث وحده[cite: 113].</li>
                <li><b>استضافة الكفاءات النادرة:</b> اختيار 6 شخصيات مرموقة بالمنطقة الغربية في مجالات (الطب، الهندسة، ريادة الأعمال، الابتكار، والتقنية)[cite: 114].</li>
                <li><b>تحدي الـ 20 دقيقة المحددة:</b> يُمنح كل عالم <b>20 دقيقة صارمة وبدون مجاملة</b>، يقدم فيها زبدة وخلاصة تجربته العملية والحلول المباشرة بعيداً عن السرد التقليدي[cite: 186].</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col_b:
        st.markdown("""
        <div class='luxury-card' style='height: 100%;'>
            <h4>🚀 سوق عكاظ للمشاريع الناشئة والمعرض المصاحب</h4>
            <p>امتداداً للأثر الاقتصادي والتنموي للمنصة، يُقام على الهامش معرض متكامل لرواد الأعمال والابتكارات والمهن الحرة[cite: 187]:</p>
            <ul>
                <li>منح مساحات مجانية كاملة للشباب المبرمجين، أصحاب الحرف، والمشاريع الصغيرة[cite: 116].</li>
                <li>تبادل بطاقات العمل والخبرات الحرة لبناء شبكات مهنية قوية[cite: 187].</li>
                <li>ترسيخ وتأكيد دور الجالية كحاضنة اقتصادية حقيقية وداعمة ومطورة لأبنائها[cite: 116, 187].</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# القسم السادس: الحوكمة والخاتمة
else:
    st.markdown("<h2>5. آليات الحوكمة الفعالة والتوصيات المرفوعة لإجازة الخطة</h2>", unsafe_allow_html=True)
    
    ch1, ch2 = st.columns(2)
    with ch1:
        st.markdown("""
        <div class='luxury-card'>
            <h4>🎟️ 1. بطاقة العضوية الثقافية الممنهجة</h4>
            <p>إصدار بطاقات حضور رمزية متسلسلة تسهم في قياس مدى التزام وتفاعل القواعد الجماهيرية، وتمنح ميزات تفضيلية للملتزمين في الفعاليات الختامية الكبرى للجنة[cite: 190].</p>
        </div>
        <div class='luxury-card'>
            <h4>⚖️ 3. الحوكمة الإدارية والتنسيق الدبلوماسي</h4>
            <p>تخضع كافة المشروعات المعرفية لإشراف وتنسيق مباشر من الأمانة الثقافية، وبالتنسيق الكامل والمسبق مع القنصلية العامة لجمهورية السودان بجدة لضمان الالتزام بكافة الأنظمة المرعية[cite: 193, 194].</p>
        </div>
        """, unsafe_allow_html=True)
        
    with ch2:
        st.markdown("""
        <div class='luxury-card' style='height: 92%;'>
            <h4>📥 2. صندوق "صوت المواطن" والشفافية التامة</h4>
            <p>صندوق مقترحات رسمي وموثق يتنقل بين كافة المشروعات الثقافية الحية على الأرض[cite: 191].</p>
            <p>يتيح هذا الصندوق لأبناء وبنات الجالية تقديم أفكارهم، مرئياتهم، ورؤاهم المكتوبة مباشرة لغرفة صناعة القرار بلجنة التسيير؛ إيماناً بمبدأ الشفافية والمشاركة الجماعية العريضة في بناء الكيان الموحد[cite: 191].</p>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; margin-top: 20px; font-weight: bold;'>
        <p style='font-size: 18px; color: #1A365D;'>تتقدم الأمانة الثقافية بهذا المقترح الإستراتيجي المتكامل لسعادتكم وللجنة الموقرة للمناقشة والإجازة [cite: 197]،،</p>
        <p style='color: #C5A059; font-size: 16px;'>بابكر عبد الله &nbsp;|&nbsp; وليد البليل</p>
        <p style='font-size: 12px; color: #666;'>أمانة الثقافة بلجنة تسيير الجالية السودانية بجدة • مايو 2026م [cite: 200, 203]</p>
    </div>
    """, unsafe_allow_html=True)
