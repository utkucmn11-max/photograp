import streamlit as st

# 1. SAYFA AYARLARI (Geniş ekran)
st.set_page_config(page_title="UTKU | STUDIO", layout="wide", initial_sidebar_state="collapsed")

# 2. ÖZEL CSS (Minimalist & Premium Estetik)
st.markdown("""
    <style>
    /* Google Fonts'tan Inter ve Neue Haas Grotesk alternatifi Roboto'yu çekelim */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;300;400;700&family=Roboto:wght@100;300;400;700&display=swap');

    /* Genel Arka Plan ve Yazı Tipi */
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #0c0c0c; /* Çok koyu grimsi siyah, premium durur */
        font-family: 'Inter', sans-serif;
        color: #f5f5f5;
    }

    /* Başlık Alanı (GÖSTERİŞLİ VE SADE) */
    .header-container {
        text-align: center;
        padding: 120px 0px 80px 0px; /* Daha fazla üst boşluk */
    }
    .main-title {
        font-family: 'Inter', sans-serif;
        font-weight: 100; /* Çok ince */
        letter-spacing: 20px; /* Çok açık harf arası */
        font-size: 4.5rem; /* Büyük, "Ben Buradayım" diyor */
        margin-bottom: 20px;
        text-transform: uppercase;
        color: #ffffff;
        animation: fadeInDown 1.5s ease-out; /* Hafif açılma efekti */
    }
    .sub-title {
        font-family: 'Roboto', sans-serif;
        font-weight: 300;
        letter-spacing: 6px;
        color: #777;
        font-size: 1rem;
        animation: fadeInUp 1.8s ease-out;
    }

    /* Fotoğrafların Zarif Görünmesi (SADE VE GÖSTERİŞLİ) */
    [data-testid="stImage"] {
        border-radius: 2px; /* Keskin, profesyonel kenarlar */
        border: 1px solid #222; /* Çok ince, koyu çerçeve */
        filter: grayscale(100%); /* Başlangıçta Siyah Beyaz */
        transition: 0.8s all ease;
        margin-bottom: 30px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.5); /* Hafif gölge */
    }
    [data-testid="stImage"]:hover {
        filter: grayscale(0%); /* Üzerine gelince Renkli */
        transform: scale(1.03); /* Hafif büyüme efekti */
        border: 1px solid #fff; /* Beyaz çerçeve */
        box-shadow: 0px 8px 30px rgba(255,255,255,0.1); /* Beyaz parlama */
        cursor: crosshair; /* Tasarımcı mouse imleci */
    }

    /* Animasyonlar */
    @keyframes fadeInDown {
        from { opacity: 0; transform: translateY(-20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Sütun Aralarındaki Boşluk */
    [data-testid="stVerticalBlock"] > [data-testid="stHorizontalBlock"] {
        gap: 30px;
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
        <div class="main-title">UTKU STUDIO</div>
        <div class="sub-title">SELECT WORKS — 2026</div>
    </div>
    """, unsafe_allow_html=True)

# 4. VİTRİN (GALLERY) ALANI
# Fotoğraflarını 3 sütuna ayırıyoruz
col1, col2, col3 = st.columns(3)

# Kendi fotoğraflarının URL'lerini veya yerel dosya yollarını ekle
photos = [
    "https://images.unsplash.com/photo-1543326727-cf6c39e8f84c",
    "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f",
    "https://images.unsplash.com/photo-1524504388940-b1c1722653e1",
    "https://images.unsplash.com/photo-1494790108377-be9c29b29330",
    "https://images.unsplash.com/photo-1506744038136-46273834b3fb",
    "https://images.unsplash.com/photo-1534528741775-53994a69daeb",
    "https://images.unsplash.com/photo-1517841905240-472988babdf9",
    "https://images.unsplash.com/photo-1520156551693-010041d5509c",
    "https://images.unsplash.com/photo-1500917293891-ef795e70e1f6"
]

# Fotoğrafları sütunlara Masonry tarzı dağıtalım
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
st.markdown("<p style='text-align: center; color: #333; font-weight: 100; letter-spacing: 3px; padding: 50px 0;'>UTKU ÇİMEN</p>", unsafe_allow_html=True)
