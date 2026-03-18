import streamlit as st

# 1. SAYFA AYARLARI (Geniş ekran, Sidebarsız)
st.set_page_config(page_title="UTKU STUDIO | GALLERY", layout="wide", initial_sidebar_state="collapsed")

# 2. ÖZEL CSS (Ferah, Koyu Tema, Mavi Detaylar ve Arka Plan Şekilleri)
st.markdown("""
    <style>
    /* Google Fonts'tan Inter (Minimal) ve Poppins (Modern Başlık) çekelim */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;300;400&family=Poppins:wght@100;200;300;400;500&display=swap');

    /* Genel Arka Plan ve Yazı Tipi - ŞİMDİ KOYU VE ŞEKİLLİ */
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #050505; /* Çok koyu, tam siyah değil, premium durur */
        background-image: 
            linear-gradient(135deg, rgba(10, 10, 10, 0) 0%, rgba(10, 10, 10, 0.2) 50%, rgba(10, 10, 10, 0) 100%),
            radial-gradient(circle at 10% 20%, rgba(0, 102, 204, 0.1) 0%, rgba(0, 102, 204, 0) 20%), /* Hafif Mavi Parlama - Sol Üst */
            radial-gradient(circle at 90% 80%, rgba(0, 102, 204, 0.05) 0%, rgba(0, 102, 204, 0) 20%), /* Hafif Mavi Parlama - Sağ Alt */
            /* Arka Plandaki Soyut Şekiller */
            url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%"><rect width="100%" height="100%" fill="none"/><circle cx="10%" cy="10%" r="50" fill="rgba(0, 102, 204, 0.01)"/><polygon points="90,10 95,20 85,20" fill="rgba(0, 102, 204, 0.02)"/></svg>');
        background-attachment: fixed;
        background-size: cover;
        font-family: 'Inter', sans-serif;
        color: #f5f5f5; /* Açık Gri Yazılar */
    }

    /* Başlık Alanı (GÖSTERİŞLİ VE ÇOK FERAH) */
    .header-container {
        text-align: center;
        padding: 160px 0px 100px 0px; /* Çok daha fazla üst boşluk */
        position: relative;
    }
    .main-title {
        font-family: 'Poppins', sans-serif;
        font-weight: 100; /* Çok ince */
        letter-spacing: 25px; /* Çok açık harf arası */
        font-size: 5rem; /* Büyük, "Ben Buradayım" diyor */
        margin-bottom: 25px;
        text-transform: uppercase;
        color: #ffffff;
        text-shadow: 0px 4px 10px rgba(0, 102, 204, 0.1); /* Hafif Mavi Gölge */
        animation: fadeInDown 2s ease-out; /* Hafif açılma efekti */
    }
    .sub-title {
        font-family: 'Inter', sans-serif;
        font-weight: 300;
        letter-spacing: 8px;
        color: #0066cc; /* Parlak Mavi Alt Başlık */
        font-size: 1.1rem;
        animation: fadeInUp 2.2s ease-out;
    }

    /* Fotoğrafların Zarif Görünmesi (SADE VE GÖSTERİŞLİ) */
    [data-testid="stImage"] {
        border-radius: 4px; /* Hafif yumuşak kenarlar */
        border: 1px solid #1a1a1a; /* Çok ince, koyu gri çerçeve */
        transition: 0.8s all ease;
        margin-bottom: 50px; /* Fotoğraflar arası dikey ferahlık */
        box-shadow: 0px 4px 20px rgba(0,0,0,0.6); /* Derin gölge */
    }
    [data-testid="stImage"]:hover {
        transform: scale(1.03); /* Hafif büyüme efekti */
        border: 1px solid #0066cc; /* Üzerine gelince Mavi çerçeve */
        box-shadow: 0px 10px 40px rgba(0, 102, 204, 0.2); /* Mavi parlama efekti */
        cursor: crosshair; /* Tasarımcı mouse imleci */
    }

    /* Sütun Aralarındaki Boşluk - YATAY FERAHLIK */
    [data-testid="stVerticalBlock"] > [data-testid="stHorizontalBlock"] {
        gap: 60px; /* Sütunlar arası boşluk */
    }

    /* Alt Bilgi (FOOTER) - FERAH */
    .footer-container {
        text-align: center;
        padding: 100px 0px 50px 0px;
        color: #333;
        font-weight: 100;
        letter-spacing: 4px;
        font-size: 0.8rem;
    }

    /* Animasyonlar */
    @keyframes fadeInDown {
        from { opacity: 0; transform: translateY(-30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
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
        <div class="sub-title">VISUAL JOURNAL — SELECT WORKS</div>
    </div>
    """, unsafe_allow_html=True)

# 4. VİTRİN (GALLERY) ALANI
# Fotoğraflarını 3 sütuna ayırıyoruz
col1, col2, col3 = st.columns(3)

# Kendi fotoğraflarının URL'lerini veya yerel dosya yollarını ekle
# Örnek: photos = ["resim1.jpg", "resim2.png"]
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

# 5. ALT BİLGİ (FOOTER) - FERAH
st.markdown("---")
st.markdown("""
    <div class="footer-container">
        CREATED BY UTKU ÇİMEN
    </div>
    """, unsafe_allow_html=True)
