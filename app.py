import streamlit as st
from PIL import Image, ImageOps, ImageEnhance
import io

# 1. SAYFA YAPILANDIRMASI
st.set_page_config(page_title="STUDIO | VSCO Style", layout="wide", initial_sidebar_state="expanded")

# 2. ÖZEL CSS (Minimalist & Dark Estetik)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;300;400&display=swap');

    html, body, [data-testid="stSidebarViewPort"] {
        font-family: 'Inter', sans-serif;
        background-color: #0e0e0e;
        color: #f0f0f0;
    }

    .vsco-header {
        font-weight: 100;
        text-align: center;
        letter-spacing: 12px;
        color: #ffffff;
        padding-top: 20px;
        margin-bottom: 40px;
        font-size: 2.5rem;
    }

    /* Slider ve Buton Tasarımı */
    .stSlider > div > div > div > div { background-color: #444; }
    .stButton>button {
        border-radius: 0px;
        background-color: transparent;
        border: 1px solid #333;
        color: #fff;
        width: 100%;
        transition: 0.4s;
    }
    .stButton>button:hover {
        background-color: #fff;
        color: #000;
    }
    
    /* Resim Alanı */
    [data-testid="stImage"] {
        border: 1px solid #222;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. BAŞLIK
st.markdown("<h1 class='vsco-header'>S T U D I O</h1>", unsafe_allow_html=True)

# 4. YAN PANEL (KONTROLLER)
with st.sidebar:
    st.markdown("### 01 / UPLOAD")
    uploaded_file = st.file_uploader("Bir fotoğraf seçin", type=["jpg", "jpeg", "png"])
    
    st.markdown("---")
    st.markdown("### 02 / PRESETS")
    filter_type = st.selectbox("Bir stil seçin", ["Original", "A6 (Analog)", "M5 (Moody)", "B&W (Classic)"])
    
    st.markdown("---")
    st.markdown("### 03 / ADJUST")
    # Hata aldığın parantezleri burada tek tek kontrol ettim:
    br_val = st.slider("Brightness", 0.5, 1.5, 1.0, step=0.01)
    ct_val = st.slider("Contrast", 0.5, 1.5, 1.0, step=0.01)
    st_val = st.slider("Saturation", 0.0, 2.0, 1.0, step=0.01)

# 5. ANA EKRAN (GÖRSEL İŞLEME)
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    proc_img = img.copy()

    # Filtre Uygulama
    if filter_type == "A6 (Analog)":
        proc_img = ImageEnhance.Color(proc_img).enhance(1.2)
        proc_img = ImageEnhance.Contrast(proc_img).enhance(0.9)
    elif filter_type == "M5 (Moody)":
        proc_img = ImageEnhance.Color(proc_img).enhance(0.6)
        proc_img = ImageEnhance.Contrast(proc_img).enhance(1.3)
    elif filter_type == "B&W (Classic)":
        proc_img = ImageOps.grayscale(proc_img)

    # İnce Ayarları Uygulama
    proc_img = ImageEnhance.Brightness(proc_img).enhance(br_val)
    proc_img = ImageEnhance.Contrast(proc_img).enhance(ct_val)
    if filter_type != "B&W (Classic)": # Siyah beyaz değilse doygunluk ayarla
        proc_img = ImageEnhance.Color(proc_img).enhance(st_val)

    # Görüntüleme
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("<p style='color:#666; font-size:12px;'>BEFORE</p>", unsafe_allow_html=True)
        st.image(img, use_container_width=True)
    with c2:
        st.markdown("<p style='color:#fff; font-size:12px;'>AFTER</p>", unsafe_allow_html=True)
        st.image(proc_img, use_container_width=True)
        
        # İndirme Butonu
        buf = io.BytesIO()
        final_to_save = proc_img.convert("RGB") if proc_img.mode != "RGB" else proc_img
        final_to_save.save(buf, format="JPEG")
        st.download_button("SAVE TO GALLERY", data=buf.getvalue(), file_name="vsco_edit.jpg", mime="image/jpeg")

else:
    # Boş durumdayken galeri görünümü
    st.markdown("<p style='text-align:center; color:#444;'>Lütfen düzenlemek için bir görsel yükleyin.</p>", unsafe_allow_html=True)
    st.markdown("---")
    colA, colB, colC = st.columns(3)
    # Örnek Placeholder Görseller
    sample_url = "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?q=80&w=500"
    colA.image(sample_url, caption="Sample 01", use_container_width=True)
    colB.image(sample_url, caption="Sample 02", use_container_width=True)
    colC.image(sample_url, caption="Sample 03", use_container_width=True)
