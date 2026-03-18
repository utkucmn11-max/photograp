import streamlit as st

# 1. SAYFA AYARLARI
st.set_page_config(page_title="UTKU | ARCHIVE", layout="wide", initial_sidebar_state="collapsed")

# 2. ÖZEL CSS (Sedef Mavi & Saf Siyah)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;400&display=swap');

    html, body, [data-testid="stAppViewContainer"] {
        background-color: #000000;
        font-family: 'Inter', sans-serif;
        color: #ffffff;
    }

    /* Başlık: Sedef Mavi Parlama */
    .header-container {
        padding: 100px 0px 60px 8%;
    }
    .main-title {
        font-weight: 100;
        letter-spacing: -3px;
        font-size: 7rem;
        line-height: 0.8;
        color: #88ccff; 
        text-shadow: 0 0 25px rgba(136, 204, 255, 0.4);
    }
    .sub-title {
        letter-spacing: 10px;
        color: #444;
        font-size: 0.8rem;
        text-transform: uppercase;
        margin-top: 10px;
    }

    /* Çapraz Duruş: Sağ sütun 180px aşağıdan başlar */
    [data-testid="column"]:nth-child(2) {
        margin-top: 180px; 
    }

    /* Fotoğraf Tasarımı ve Hover */
    [data-testid="stImage"] {
        border-radius: 0px;
        margin-bottom: 120px; /* Fotoğraflar arası ferah boşluk */
        border: 1px solid #111;
        transition: all 0.7s cubic-bezier(0.16, 1, 0.3, 1);
    }
    [data-testid="stImage"]:hover {
        transform: scale(1.03);
        border: 1px solid #88ccff;
        box-shadow: 0px 0px 40px rgba(136, 204, 255, 0.25);
        cursor: crosshair;
    }

    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. BAŞLIK
st.markdown("""
    <div class="header-container">
        <div class="main-title">UTKU.</div>
        <div class="sub-title">2026 / Visual Archive / 09 Works</div>
    </div>
    """, unsafe_allow_html=True)

# 4. VİTRİN (2 SÜTUNLU ASİMETRİK - 9 FOTOĞRAF)
col1, col2 = st.columns(2)

# TOPLAM 9 FOTOĞRAF (İsimleri kendi dosyalarınla değiştir)
photos = [
    "1.jpg",
    "2.jpg",
    "3.jpg",
    "4.jpg",
    "5.jpg",
    "6.jpg",
    "7.jpg",
    "8.jpg",
    "9.jpg",
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
st.markdown("<p style='text-align: center; color: #111; font-size: 10px; letter-spacing: 5px;'>UTKU ÇİMEN STUDIO</p>", unsafe_allow_html=True)
