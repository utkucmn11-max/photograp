import streamlit as st
import os

# 1. ZİYARETÇİ SAYACI (Hata vermemesi için try-except ekledim)
def get_visitor_count():
    file_path = "counter.txt"
    if not os.path.exists(file_path):
        with open(file_path, "w") as f: f.write("0")
    try:
        with open(file_path, "r") as f:
            count = int(f.read())
    except:
        count = 0
    new_count = count + 1
    with open(file_path, "w") as f:
        f.write(str(new_count))
    return new_count

visitor_no = get_visitor_count()

# 2. SAYFA AYARLARI (Panel artık her zaman AÇIK - Hata ihtimali %0)
st.set_page_config(page_title="UTKUÇİMEN | ARCHIVE", layout="wide", initial_sidebar_state="expanded")

# 3. ÖZEL CSS (Panel ve Galeri Tasarımı)
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;400&display=swap');

    /* Ana Arka Plan */
    html, body, [data-testid="stAppViewContainer"] {{
        background-color: #000000;
        font-family: 'Inter', sans-serif;
        color: #ffffff;
        background-image: repeating-linear-gradient(
            -45deg,
            #000000 0px,
            #000000 100px,
            rgba(0, 255, 255, 0.03) 101px, 
            rgba(0, 255, 255, 0.03) 103px
        );
        background-size: 200% 200%;
        animation: gradient-flow 60s linear infinite; 
    }}

    @keyframes gradient-flow {{
        0% {{ background-position: 0% 0%; }}
        100% {{ background-position: 100% 100%; }}
    }}

    /* YAN PANEL (SIDEBAR) TASARIMI */
    [data-testid="stSidebar"] {{
        background-color: rgba(10, 10, 10, 0.8) !important;
        border-right: 1px solid rgba(0, 255, 255, 0.1);
        backdrop-filter: blur(10px);
    }}
    
    /* Gereksiz Streamlit yazılarını gizle */
    #MainMenu, footer, header, [data-testid="stSidebarNav"] {{visibility: hidden;}}

    /* Başlık Alanı */
    .header-container {{
        padding: 60px 0px 40px 5%;
    }}
    .main-title {{
        font-weight: 100;
        letter-spacing: -3px;
        font-size: 5.5rem;
        line-height: 0.8;
        color: #00ffff; 
        text-shadow: 0 0 20px rgba(0, 255, 255, 0.3);
    }}
    .sub-title {{
        letter-spacing: 8px;
        color: #555;
        font-size: 0.7rem;
        text-transform: uppercase;
        margin-top: 15px;
    }}

    /* Ziyaretçi Sayacı (Sol Alt) */
    .visitor-badge {{
        position: fixed; bottom: 20px; left: 20px;
        font-size: 0.65rem; color: #00ffff;
        letter-spacing: 3px; z-index: 1000; opacity: 0.4;
    }}

    /* Fotoğraf Çerçeveleri */
    [data-testid="stImage"] {{
        border: 1px solid #111;
        margin-bottom: 80px;
        transition: 0.5s ease;
    }}
    [data-testid="stImage"]:hover {{
        border: 1px solid #00ffff;
        box-shadow: 0 0 30px rgba(0, 255, 255, 0.2);
    }}

    /* Sağ sütun kaydırma efekti */
    [data-testid="column"]:nth-child(2) {{ margin-top: 150px; }}

    @media (max-width: 768px) {{
        .main-title {{ font-size: 3rem; }}
        [data-testid="column"]:nth-child(2) {{ margin-top: 0px !important; }}
    }}
    </style>
    
    <div class="visitor-badge">VISITORS // {visitor_no:04d}</div>
    """, unsafe_allow_html=True)

# 4. YAN PANEL (Her zaman orada, her zaman hazır)
with st.sidebar:
    st.markdown("<h2 style='color:#00ffff; font-weight:100; letter-spacing:2px;'>EDITOR</h2>", unsafe_allow_html=True)
    user_name = st.text_input("Name", "Utku Çimen")
    archive_year = st.text_input("Year", "2026")
    
    st.markdown("---")
    uploaded_images = st.file_uploader("Upload Works", type=["jpg", "jpeg", "png"], accept_multiple_files=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.caption("Sol üstteki '>' okuna basarak bu paneli tamamen gizleyebilirsin.")

# 5. ANA İÇERİK
st.markdown(f"""
    <div class="header-container">
        <div class="main-title">{user_name}</div>
        <div class="sub-title">{archive_year} / PERSONAL ARCHIVE / {len(uploaded_images) if uploaded_images else 0} WORKS</div>
    </div>
    """, unsafe_allow_html=True)

# 6. GALERİ (2 Sütunlu)
col1, col2 = st.columns(2)

if uploaded_images:
    for i, file in enumerate(uploaded_images):
        if i % 2 == 0:
            with col1: st.image(file, use_container_width=True)
        else:
            with col2: st.image(file, use_container_width=True)
else:
    st.info("← Sol taraftaki panelden fotoğraflarını yüklemeye başla!")

# 7. ALT BİLGİ
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #333; font-size: 14px; letter-spacing: 4px;'>PORTFOLIO BY {user_name.upper()}</p>", unsafe_allow_html=True)
