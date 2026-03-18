import streamlit as st

# 1. SAYFA AYARLARI
st.set_page_config(page_title="UTKU | GALLERY", layout="wide")

# 2. VİTRİN ESTETİĞİ İÇİN ÖZEL CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400&display=swap');

    /* Genel Arka Plan ve Yazı Tipi */
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #000000;
        font-family: 'Inter', sans-serif;
        color: white;
    }

    /* Başlık Alanı */
    .header-container {
        text-align: center;
        padding: 80px 0px 50px 0px;
    }
    .main-title {
        font-weight: 100;
        letter-spacing: 15px;
        font-size: 3rem;
        margin-bottom: 10px;
        text-transform: uppercase;
    }
    .sub-title {
        font-weight: 300;
        letter-spacing: 4px;
        color: #666;
        font-size: 0.9rem;
    }

    /* Fotoğrafların Zarif Görünmesi İçin */
    [data-testid="stImage"] {
        filter: grayscale(20%); /* Hafif analog havası */
        transition: 0.6s all ease-in-out;
        margin-bottom: 20px;
    }
    [data-testid="stImage"]:hover {
        filter: grayscale(0%);
        transform: scale(1.02);
        cursor: crosshair;
    }

    /* Menü ve Gereksiz Streamlit Öğelerini Gizle */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    </style>
    """, unsafe_allow_html=True)

# 3. BAŞLIK BÖLÜMÜ
st.markdown("""
    <div class="header-container">
        <div class="main-title">Visual Journal</div>
        <div class="sub-title">UTKU ÇİMEN — 2026 EDITION</div>
    </div>
    """, unsafe_allow_html=True)

# 4. VİTRİN (GALLERY) ALANI
# Fotoğraflarını 3 sütuna ayırıyoruz
col1, col2, col3 = st.columns(3, gap="medium")

# Buradaki URL'leri kendi fotoğraflarının yollarıyla değiştirebilirsin
# Örnek: "foto1.jpg", "foto2.png" gibi...
photos = [
    "https://images.unsplash.com/photo-1500648767791-00dcc994a43e",
    "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f",
    "https://images.unsplash.com/photo-1524504388940-b1c1722653e1",
    "https://images.unsplash.com/photo-1494790108377-be9c29b29330",
    "https://images.unsplash.com/photo-1506744038136-46273834b3fb",
    "https://images.unsplash.com/photo-1534528741775-53994a69daeb"
]

# Fotoğrafları sütunlara dağıtalım
for i, url in enumerate(photos):
    if i % 3 == 0:
        with col1:
            st.image(url, use_container_width=True)
    elif i % 3 == 1:
        with col2:
            st.image(url, use_container_width=True)
    else:
        with col3:
            st.image(url, use_container_width=True)

# 5. ALT BİLGİ (FOOTER)
st.markdown("---")
st.markdown("<p style='text-align: center; color: #444; font-weight: 200; letter-spacing: 2px;'>CREATED BY UTKU</p>", unsafe_allow_html=True)
