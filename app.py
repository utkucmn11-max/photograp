import streamlit as st

# 1. SAYFA AYARLARI
st.set_page_config(page_title="UTKU", layout="centered") # 'wide' yerine 'centered' yaparak odağı topladık

# 2. ÖZEL CSS (Sadece Saf Siyah ve Saf Beyaz)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;400&display=swap');

    /* Saf Siyah Arka Plan */
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #000000;
        font-family: 'Inter', sans-serif;
        color: #ffffff;
    }

    /* Başlık: Çok sade, çok büyük, çok ince */
    .header-container {
        text-align: left; /* Sola yaslı, daha modern */
        padding: 100px 0px 50px 0px;
    }
    .main-title {
        font-weight: 100;
        letter-spacing: -2px; /* Harfleri birbirine yaklaştırarak sinematik bir hava kattık */
        font-size: 6rem;
        line-height: 1;
        margin-bottom: 10px;
    }
    .sub-title {
        letter-spacing: 5px;
        color: #444; /* Çok koyu gri, gizli bir detay gibi */
        font-size: 0.8rem;
        text-transform: uppercase;
    }

    /* Fotoğraflar: Devasa ve Kenarsız */
    [data-testid="stImage"] {
        border-radius: 0px;
        margin-bottom: 150px; /* Fotoğraflar arası uçsuz bucaksız boşluk */
        transition: opacity 0.5s ease;
    }
    [data-testid="stImage"]:hover {
        opacity: 0.8;
    }

    /* Streamlit kalabalığını temizle */
    #MainMenu, footer, header {visibility: hidden;}
    .block-container {padding-top: 2rem;}
    </style>
    """, unsafe_allow_html=True)

# 3. BAŞLIK
st.markdown("""
    <div class="header-container">
        <div class="main-title">UTKU.</div>
        <div class="sub-title">2026 / VISUAL ARCHIVE</div>
    </div>
    """, unsafe_allow_html=True)

# 4. VİTRİN (TEK SÜTUN - SİNEMATİK AKIŞ)
# Fotoğraflar artık yan yana değil, alt alta ve kocaman.
photos = [
    "https://images.unsplash.com/photo-1543326727-cf6c39e8f84c",
    "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f",
    "https://images.unsplash.com/photo-1524504388940-b1c1722653e1",
    "https://images.unsplash.com/photo-1494790108377-be9c29b29330"
]

for url in photos:
    st.image(url, use_container_width=True)

# 5. FİNAL
st.markdown("<p style='text-align: left; color: #222; font-size: 10px;'>END OF ARCHIVE</p>", unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)
