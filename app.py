import streamlit as st

# 1. SAYFA AYARLARI
st.set_page_config(page_title="UTKUÇİMEN| ARCHIVE", layout="wide", initial_sidebar_state="collapsed")

# 2. ÖZEL CSS (Cam Göbeği & Saf Siyah & Hareketli Arka Plan)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;400&display=swap');

    html, body, [data-testid="stAppViewContainer"] {
        background-color: #000000;
        font-family: 'Inter', sans-serif;
        color: #ffffff;
        
        /* --- GÜNCELLENDİ: CAM GÖBEĞİ ÇAPRAZ ÇİZGİLER --- */
        background-image: repeating-linear-gradient(
            -45deg,
            #000000 0px,
            #000000 100px,
            rgba(0, 255, 255, 0.05) 101px, /* Çok şeffaf cam göbeği (cyan) line */
            rgba(0, 255, 255, 0.05) 103px
        );
        background-size: 200% 200%;
        animation: gradient-flow 60s linear infinite; 
    }

    /* --- HAREKET ANİMASYONU --- */
    @keyframes gradient-flow {
        0% { background-position: 0% 0%; }
        100% { background-position: 100% 100%; }
    }

    /* Başlık: Cam Göbeği Parlama */
    .header-container {
        padding: 100px 0px 60px 8%;
        position: relative;
        z-index: 10;
    }
    .main-title {
        font-weight: 100;
        letter-spacing: -3px;
        font-size: 7rem;
        line-height: 0.8;
        color: #00ffff; /* Cam Göbeği (Cyan) */
        text-shadow: 0 0 25px rgba(0, 255, 255, 0.4);
    }
    .sub-title {
        letter-spacing: 10px;
        color: #444;
        font-size: 0.8rem;
        text-transform: uppercase;
        margin-top: 10px;
    }

    /* Mobil Uyumluluk */
    @media (max-width: 768px) {
        .main-title { font-size: 4rem; }
        [data-testid="column"]:nth-child(2) { margin-top: 0px !important; }
    }

    /* Çapraz Duruş */
    @media (min-width: 769px) {
        [data-testid="column"]:nth-child(2) { margin-top: 180px; }
    }

    /* Fotoğraf Tasarımı ve Hover */
    [data-testid="stImage"] {
        border-radius: 0px;
        margin-bottom: 120px;
        border: 1px solid #111;
        transition: all 0.7s cubic-bezier(0.16, 1, 0.3, 1);
        position: relative;
        z-index: 5;
    }
    [data-testid="stImage"]:hover {
        transform: scale(1.03);
        border: 1px solid #00ffff; /* Hover rengi cam göbeği yapıldı */
        box-shadow: 0px 0px 40px rgba(0, 255, 255, 0.25);
        cursor: crosshair;
    }

    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. BAŞLIK
st.markdown("""
    <div class="header-container">
        <div class="main-title">Utku Çimen </div>
        <div class="sub-title">2026 / Kişisel Arşiv / 09 Works</div>
    </div>
    """, unsafe_allow_html=True)

# 4. VİTRİN
col1, col2 = st.columns(2)

photos = [
    "9.jpg",
    "2.jpg",
    "3.jpg",
    "4.jpg",
    "8.jpg",
    "1.jpg",
]

for i, url in enumerate(photos):
    if i % 2 == 0:
        with col1:
            st.image(url, use_container_width=True)
    else:
        with col2:
            st.image(url, use_container_width=True)

# 5. ALT BİLGİ
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #008b8b; font-size: 20px; letter-spacing: 5px; position: relative; z-index: 10;'>Bu site Utku Çimen tarafından yapılmıştır.</p>", unsafe_allow_html=True)
