import streamlit as st

# 1. SAYFA AYARLARI
st.set_page_config(page_title="UTKU STUDIO", layout="wide", initial_sidebar_state="collapsed")

# 2. ÖZEL CSS (Mavi-Siyah, Ultra Ferah)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;300;400&display=swap');

    html, body, [data-testid="stAppViewContainer"] {
        background-color: #050505;
        background-image: 
            radial-gradient(circle at 5% 5%, rgba(0, 102, 255, 0.08) 0%, transparent 25%),
            radial-gradient(circle at 95% 95%, rgba(0, 102, 255, 0.05) 0%, transparent 25%);
        font-family: 'Inter', sans-serif;
        color: #f5f5f5;
    }

    .header-container {
        text-align: center;
        padding: 180px 0px 120px 0px; /* Üst boşluğu daha da artırdık */
    }
    .main-title {
        font-weight: 100;
        letter-spacing: 30px; /* Harf arası iyice açıldı */
        font-size: 5.5rem;
        text-transform: uppercase;
        color: #ffffff;
        margin-bottom: 30px;
    }
    .sub-title {
        letter-spacing: 10px;
        color: #0070f3; /* Canlı Mavi */
        font-size: 1.2rem;
        font-weight: 300;
    }

    /* Fotoğraf Alanı Düzenlemeleri */
    [data-testid="stImage"] {
        border-radius: 5px;
        border: 1px solid #111;
        transition: 1s all ease;
        margin-bottom: 100px; /* Fotoğraflar arası dikey boşluk (ÇOK FERAH) */
    }
    [data-testid="stImage"]:hover {
        transform: translateY(-10px); /* Yukarı doğru hafif süzülme */
        border: 1px solid #0070f3;
        box-shadow: 0px 20px 50px rgba(0, 112, 243, 0.15);
    }

    /* Sütunlar arası YATAY boşluk */
    [data-testid="stHorizontalBlock"] {
        gap: 120px !important; /* Fotoğraflar arası yatay mesafe iki katına çıktı */
    }

    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. BAŞLIK
st.markdown("""
    <div class="header-container">
        <div class="main-title">UTKU</div>
        <div class="sub-title">COLLECTION — 026</div>
    </div>
    """, unsafe_allow_html=True)

# 4. VİTRİN (2 SÜTUNLU YAPI)
# 3 yerine 2 sütun kullanarak ferahlığı sağladık
col1, col2 = st.columns(2)

# Fotoğraf listesi (Buraya kendi dosya adlarını yazmayı unutma)
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
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #222; letter-spacing: 5px;'>LIMITED EDITION STUDIO</p>", unsafe_allow_html=True)
