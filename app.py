import streamlit as st

# 1. SAYFA AYARLARI (Geniş ekran)
st.set_page_config(page_title="UTKU | STUDIO", layout="wide", initial_sidebar_state="collapsed")

# 2. ÖZEL CSS (Aydınlık & Minimal Estetik)
st.markdown("""
    <style>
    /* Google Fonts'tan Inter ve Neue Haas Grotesk alternatifi Roboto'yu çekelim */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;300;400;700&family=Roboto:wght@100;300;400;700&display=swap');

    /* Genel Arka Plan ve Yazı Tipi - ŞİMDİ AYDINLIK */
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #ffffff; /* Tam Beyaz */
        font-family: 'Inter', sans-serif;
        color: #111111; /* Koyu Gri/Siyah Yazılar */
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
        color: #000000; /* Siyah Başlık */
        animation: fadeInDown 1.5s ease-out; /* Hafif açılma efekti */
    }
    .sub-title {
        font-family: 'Roboto', sans-serif;
        font-weight: 300;
        letter-spacing: 6px;
        color: #888; /* Hafif Gri Alt Başlık */
        font-size: 1rem;
        animation: fadeInUp 1.8s ease-out;
    }

    /* Fotoğrafların Zarif Görünmesi (SADE VE GÖSTERİŞLİ) */
    [data-testid="stImage"] {
        border-radius: 0px; /* Tam keskin kenarlar */
        border: 1px solid #f0f0f0; /* Çok ince, çok açık gri çerçeve */
        filter: grayscale(0%); /* SİYAH EFEKTİ KALDIRILDI - Başlangıçta Renkli */
        transition: 0.8s all ease;
        margin-bottom: 30px;
        box-shadow: 0px 2px 10px rgba(0,0,0,0.05); /* Çok hafif gölge */
    }
    [data-testid="stImage"]:hover {
        transform: scale(1.02); /* Hafif büyüme efekti */
        border: 1px solid #000; /* Üzerine gelince Siyah çerçeve */
        box-shadow: 0px 5px 20px rgba(0,0,0,0.1); /* Hafif gölge artışı */
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
# Örnek: photos = ["resim1.jpg", "resim2.png"]
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
st.markdown("<p style='text-align: center; color: #ccc; font-weight: 100; letter-spacing: 3px; padding: 50px 0;'>UTKU ÇİMEN</p>", unsafe_allow_html=True)
