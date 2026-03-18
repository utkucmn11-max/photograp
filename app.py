import streamlit as st
from PIL import Image, ImageOps, ImageEnhance
import io

# 1. SAYFA AYARLARI (Geniş ekran ve Koyu Tema)
st.set_page_config(page_title="STUDIO | Minimalist Editor", layout="wide", initial_sidebar_state="collapsed")

# 2. VSCO ESTETİĞİ İÇİN ÖZEL CSS (Yazı tipleri, boşluklar, butonlar)
st.markdown("""
    <style>
    /* Google Fonts'tan Inter yazı tipini çekelim */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500&display=swap');

    html, body, [data-testid="stSidebarViewPort"] {
        font-family: 'Inter', sans-serif;
        background-color: #111111; /* Çok koyu gri, tam siyah değil */
        color: #eeeeee;
    }

    /* Minimalist Başlık Stili */
    .studio-header {
        font-family: 'Inter', sans-serif;
        font-weight: 100; /* Çok ince font */
        text-align: center;
        letter-spacing: 10px; /* Harf arası boşluk */
        color: #ffffff;
        margin-top: -50px;
        margin-bottom: 50px;
    }

    /* Görsel Çerçeveleri */
    [data-testid="stImage"] {
        border-radius: 2px;
        transition: 0.5s ease;
    }
    [data-testid="stImage"]:hover {
        transform: scale(1.01); /* Hafif büyüme efekti */
        box-shadow: 0px 4px 20px rgba(255,255,255,0.1);
    }

    /* Sidebar'ı minimal yapalım */
    [data-testid="stSidebar"] {
        background-color: #1a1a1a;
        border-right: 1px solid #333;
    }

    /* Slider ve Kontrollerin Stili */
    .stSlider > div > div > div > div {
        background-color: #555;
    }

    /* Minimalist Buton */
    .stButton>button {
        border-radius: 0px;
        background-color: transparent;
        border: 1px solid #555;
        color: #eee;
        letter-spacing: 2px;
        font-weight: 200;
        width: 100%;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #eee;
        color: #111;
        border: 1px solid #eee;
    }

    </style>
    """, unsafe_allow_html=True)

# 3. BAŞLIK VE YÜKLEME ALANI
st.markdown("<h1 class='studio-header'>S T U D I O</h1>", unsafe_allow_html=True)

# Yan panelde filtre kontrolleri
with st.sidebar:
    st.markdown("### TOOLS")
    uploaded_file = st.file_uploader("Bir fotoğraf seç...", type=["jpg", "png", "jpeg"])
    
    st.markdown("---")
    st.markdown("### ADJUSTMENTS")
    # VSCO tarzı ince ayarlar
    brightness = st.slider("Brightness", 0.5, 1.5, 1.0, step=0.01)
    contrast = st.slider("Contrast", 0.5
