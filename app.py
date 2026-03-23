import streamlit as st
import os
import random

# 1. ZİYARETÇİ SAYACI
# Bu fonksiyon, siteye her girişte counter.txt dosyasındaki sayıyı artırır.
def get_visitor_count():
    file_path = "counter.txt"
    # Dosya yoksa oluştur ve 0 yaz
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write("0")
    # Dosyayı oku
    with open(file_path, "r") as f:
        try:
            count = int(f.read())
        except:
            # Okuma hatası olursa 0'dan başla
            count = 0
    # Sayıyı bir artır
    new_count = count + 1
    # Yeni sayıyı dosyaya kaydet
    with open(file_path, "w") as f:
        f.write(str(new_count))
    # Güncel sayıyı döndür
    return new_count

# Ziyaretçi sayısını al
visitor_no = get_visitor_count()

# 2. ARKA PLAN ÖĞELERİ (ELMASLAR VE KAMERALAR)
# Arka planda yüzen elmas efektleri
diamonds = "".join([f'<div class="diamond" style="left:{i*5}%; animation-duration:{12 + i%5}s; animation-delay:{i*0.4}s;"></div>' for i in range(20)])
# Arka planda süzülen kamera emojileri (rastgele konum ve hızda)
cameras = "".join([f'<div class="camera-float" style="left:{random.randint(0, 95)}%; animation-duration:{random.randint(15, 25)}s; animation-delay:{random.uniform(0, 10)}s;">📷</div>' for i in range(15)])

# 3. STREAMLIT SAYFA AYARI
st.set_page_config(
    page_title="UTKUÇİMEN | ARCHIVE",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 4. CSS TASARIM VE PARÇALANMA ANIMASYONU
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@200;400&display=swap');

/* GENEL SAYFA STİLLERİ */
html, body, [data-testid="stAppViewContainer"] {{
    background-color: #000; /* Saf siyah arka plan */
    font-family: 'Manrope', sans-serif;
    color: #FFD700; /* TÜM YAZILAR ALTIN SARISI */
    overflow-x: hidden;
}}

/* KARŞILAMA EKRANI VE PARÇALANMA EFEKTİ */
#intro-layer {{
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: #000;
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 9999; /* En üst katmanda durur */
    /* Ana katman 5.5s sonra tamamen kaybolur (4s bekleme + 1.5s dağılma) */
    animation: hideIntroLayer 0.1s ease-in-out 5.5s forwards;
}}

.intro-text-wrapper {{
    position: relative;
    font-size: 8vw; /* Ekrana göre ölçeklenen yazı tipi boyutu */
    font-weight: 200;
    letter-spacing: -5px;
    color: #FFD700; /* Altın sarısı karşılama yazısı */
    text-transform: uppercase;
    text-shadow: 0 0 30px rgba(255, 215, 0, 0.6); /* Altın sarısı parıltı */
}}

/* Yazı parçalarını oluşturmak için ortak sınıf */
.text-fragment {{
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    opacity: 0; /* Başlangıçta görünmez */
}}

/* 1. Parça (Sol Üst) */
.fragment-1 {{
    clip-path: polygon(0 0, 50% 0, 50% 50%, 0 50%);
    animation: fragmentIn 0.5s ease-out 0s forwards, fragmentOut1 1.5s ease-in 4s forwards;
}}

/* 2. Parça (Sağ Üst) */
.fragment-2 {{
    clip-path: polygon(50% 0, 100% 0, 100% 50%, 50% 50%);
    animation: fragmentIn 0.5s ease-out 0.3s forwards, fragmentOut2 1.5s ease-in 4s forwards;
}}

/* 3. Parça (Sol Alt) */
.fragment-3 {{
    clip-path: polygon(0 50%, 50% 50%, 50% 100%, 0 100%);
    animation: fragmentIn 0.5s ease-out 0.6s forwards, fragmentOut3 1.5s ease-in 4s forwards;
}}

/* 4. Parça (Sağ Alt) */
.fragment-4 {{
    clip-path: polygon(50% 50%, 100% 50%, 100% 100%, 50% 100%);
    animation: fragmentIn 0.5s ease-out 0.9s forwards, fragmentOut4 1.5s ease-in 4s forwards;
}}

/* Giriş Animasyonu: Parçalar sırayla birleşir */
@keyframes fragmentIn {{
    0% {{ opacity: 0; transform: scale(1.2); }}
    100% {{ opacity: 1; transform: scale(1); }}
}}

/* Parçalanma Animasyonları: 4 saniye sonra farklı yönlere dağılma */
@keyframes fragmentOut1 {{
    0% {{ transform: translate(0, 0) rotate(0deg); opacity: 1; }}
    100% {{ transform: translate(-150%, -150%) rotate(-60deg); opacity: 0; }}
}}

@keyframes fragmentOut2 {{
    0% {{ transform: translate(0, 0) rotate(0deg); opacity: 1; }}
    100% {{ transform: translate(150%, -150%) rotate(60deg); opacity: 0; }}
}}

@keyframes fragmentOut3 {{
    0% {{ transform: translate(0, 0) rotate(0deg); opacity: 1; }}
    100% {{ transform: translate(-150%, 150%) rotate(60deg); opacity: 0; }}
}}

@keyframes fragmentOut4 {{
    0% {{ transform: translate(0, 0) rotate(0deg); opacity: 1; }}
    100% {{ transform: translate(150%, 150%) rotate(-60deg); opacity: 0; }}
}}

/* Ana intro katmanını gizleme animasyonu */
@keyframes hideIntroLayer {{
    0% {{ opacity: 1; visibility: visible; }}
    100% {{ opacity: 0; visibility: hidden; }}
}}

/* ARKA PLAN EFEKTLERİ */
.bg-overlay {{ position: fixed; width: 100%; height: 100%; top: 0; left: 0; pointer-events: none; z-index: 1; overflow: hidden; }}
.diamond {{ position: absolute; width: 8px; height: 8px; background: rgba(255, 215, 0, 0.1); /* Hafif altın sarısı elmaslar */ transform: rotate(45deg); animation: floatUp linear infinite; }}
.camera-float {{ position: absolute; font-size: 1rem; opacity: 0; animation: floatUp linear infinite; filter: brightness(0.5) sepia(1) saturate(5) hue-rotate(10deg); /* Kameraları altın sarısı yap */ }}

@keyframes floatUp {{
    0% {{ transform: translateY(110vh) rotate(0deg); opacity: 0; }}
    10% {{ opacity: 0.3; }}
    90% {{ opacity: 0.3; }}
    100% {{ transform: translateY(-10vh) rotate(360deg); opacity: 0; }}
}}

/* ANA BAŞLIK STİLİ */
.header-container {{ padding: 120px 0px 100px 8%; position: relative; z-index: 10; }}
.main-title {{ font-weight: 200; letter-spacing: -3px; font-size: 7rem; line-height: 0.8; color: #FFD700; /* Altın sarısı ana başlık */ }}

/* FOTOĞRAF DÜZENİ VE EFEKTLERİ */
[data-testid="stImage"] {{
    transition: all 0.6s ease;
    border: 1px solid rgba(255, 215, 0, 0.15); /* Hafif altın sarısı çerçeve */
    background: rgba(255, 215, 0, 0.01);
}}

/* Çapraz görünüm için sağ sütunu aşağı kaydırıyoruz */
[data-testid="column"]:nth-child(2) [data-testid="stImage"] {{
    margin-top: 150px;
}}

/* Resimler arasındaki dikey boşluğu artır */
[data-testid="stImage"] {{
    margin-bottom: 150px !important;
}}

/* Resimlerin üzerine gelince parıltı efekti */
[data-testid="stImage"]:hover {{
    transform: scale(1.03);
    border: 1px solid #FFD700;
    box-shadow: 0 0 40px rgba(255, 215, 0, 0.3); /* Altın sarısı parıltı */
}}

/* ZİYARETÇİ SAYACI STİLİ */
.visitor-badge {{ 
    position: fixed; 
    bottom: 30px; 
    left: 30px; 
    font-size: 0.6rem; 
    color: #FFD700; /* Altın sarısı sayaç yazısı */ 
    letter-spacing: 4px; 
    opacity: 0.6; 
    z-index: 20; 
}}

/* Streamlit'in varsayılan menü ve logolarını gizle */
#MainMenu, footer, header {{visibility: hidden;}}
</style>

<div id="intro-layer">
    <div class="intro-text-wrapper">
        <div class="text-fragment fragment-1">Utku Çimen</div>
        <div class="text-fragment fragment-2">Utku Çimen</div>
        <div class="text-fragment fragment-3">Utku Çimen</div>
        <div class="text-fragment fragment-4">Utku Çimen</div>
    </div>
</div>

<div class="bg-overlay">
    {diamonds}
    {cameras}
</div>

<div class="visitor-badge">ARCHIVE_SYSTEM // {visitor_no:05d}</div>
""", unsafe_allow_html=True)

# 5. ANA İÇERİK: BAŞLIK VE ALT BAŞLIK
st.markdown(f"""
<div class="header-container">
    <div class="main-title">Utku Çimen</div>
    <div style="letter-spacing: 10px; color: #B8860B; /* Daha koyu altın sarısı alt başlık */ font-size: 0.7rem; margin-top:20px;">
        2026 / OFFSET_LAYOUT / INDEX_09
    </div>
</div>
""", unsafe_allow_html=True)

# 6. FOTOĞRAF GALERİSİ (ÇAPRAZ DİZİLİM)
# İki sütun oluştur
col1, col2 = st.columns(2)
# Fotoğrafların dosya adları listesi (bu dosyaların kodla aynı klasörde olması gerekir)
photos = ["9.jpg", "2.jpg", "3.jpg", "4.jpg", "8.jpg", "1.jpg"]

# Fotoğrafları sütunlara dağıt (bir sol, bir sağ)
for i, url in enumerate(photos):
    if i % 2 == 0:
        with col1:
            st.image(url, use_container_width=True)
    else:
        with col2:
            st.image(url, use_container_width=True)

# 7. SAYFA ALTI YAZISI (FOOTER)
st.markdown("<br><br><br><p style='text-align:center; color:#555; /* Soluk footer yazısı */ letter-spacing:10px; font-size:0.6rem;'>UTKU ÇİMEN PORTFOLIO // VER 3.1 // GOLDEN_EDITION</p>", unsafe_allow_html=True)
