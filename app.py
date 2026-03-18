import streamlit as st

# 1. SAYFA AYARLARI
st.set_page_config(page_title="UTKU | ARCHIVE", layout="wide", initial_sidebar_state="collapsed")

# 2. ÖZEL CSS (Asimetrik 2 Sütun ve Saf Siyah Tema)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;300;400&display=swap');

    /* Arka Plan */
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #000000;
        font-family: 'Inter', sans-serif;
        color: #ffffff;
    }

    /* Başlık Alanı */
    .header-container {
        padding: 120px 0px 80px 8%;
    }
    .main-title {
        font-weight: 100;
        letter-spacing: -3px;
        font-size: 7rem;
        line-height: 0.8;
        margin-bottom: 15px;
    }
    .sub-title {
        letter-spacing: 10px;
        color: #555;
        font-size: 0.9rem;
        text-transform: uppercase;
        margin-left: 5px;
    }

    /* Çapraz/Asimetrik Dizilim İçin Sütun Ayarları */
    .stColumn {
        padding: 0 40px !important;
    }

    /* İkinci sütunu biraz aşağı kaydırarak çapraz duruşu sağlıyoruz */
    [data-testid="column"]:nth-child(2) {
        margin-top: 150px; /* Sağ sütunu aşağı iterek asimetri yarattık */
    }

    /* Fotoğraf Tasarımı */
    [data-testid="stImage"] {
        border-radius: 0px;
        margin-bottom: 80px;
        transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
    }
    
    [data-testid="stImage"]:hover {
        transform: scale(1.02);
        cursor: crosshair;
    }

    /* Streamlit Gereksizleri Temizle */
    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. BAŞLIK
st.markdown("""
    <div class="header-container">
        <div class="main-title">UTKU.</div>
        <div class="sub-title">2026 Edition / Visual Archive</div>
    </div>
    """, unsafe_allow_html=True)

# 4. VİTRİN (2 SÜTUNLU ASİMETRİK YAPI)
col1, col2 = st.columns(2)

# Kendi fotoğraflarının listesi
photos = [
    "https://images.unsplash.com/photo-1543326727-cf6c39e8f84c",
    "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f",
    "https://images.unsplash.com/photo-1524504388940-b1c1722653e1",
    "https://images.unsplash.com/photo-1494790108377-be9c29b29330",
    "https://images.unsplash.com/photo-1506744038136-46273834b3fb",
    "https://images.unsplash.com/photo-1534528741775-53994a69daeb"
]

for i, url in enumerate(photos):
    if i % 2 == 0:
        with col1:
            st.image(url, use_container_width=True)
    else:
        with col2:
            st.image(url, use_container_width=True)

# 5. ALT BİLGİ
st.markdown("<br><br><br><br>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #222; font-size: 12px; letter-spacing: 4px;'>END OF ARCHIVE</p>", unsafe_allow_html=True)
