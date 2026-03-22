import streamlit as st
import os

# 1. ZİYARETÇİ SAYACI
def get_visitor_count():
    file_path = "counter.txt"
    if not os.path.exists(file_path):
        with open(file_path, "w") as f: f.write("0")
    with open(file_path, "r") as f:
        try: count = int(f.read())
        except: count = 0
    new_count = count + 1
    with open(file_path, "w") as f: f.write(str(new_count))
    return new_count

visitor_no = get_visitor_count()

# 2. SAYFA AYARLARI
st.set_page_config(page_title="PERSONAL ARCHIVE", layout="wide", initial_sidebar_state="collapsed")

# 3. ÖZEL CSS (Üçgen Tetikleyici ve Tasarım)
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;400&display=swap');

    html, body, [data-testid="stAppViewContainer"] {{
        background-color: #000000;
        font-family: 'Inter', sans-serif;
        color: #ffffff;
        background-image: repeating-linear-gradient(
            -45deg,
            #000000 0px,
            #000000 100px,
            rgba(0, 255, 255, 0.05) 101px, 
            rgba(0, 255, 255, 0.05) 103px
        );
        background-size: 200% 200%;
        animation: gradient-flow 60s linear infinite; 
    }}

    @keyframes gradient-flow {{
        0% {{ background-position: 0% 0%; }}
        100% {{ background-position: 100% 100%; }}
    }}

    /* SOL KENAR ÜÇGEN TETİKLEYİCİ */
    [data-testid="stSidebarCollapsedControl"] {{
        left: 0;
        top: 50%;
        transform: translateY(-50%);
        background-color: transparent !important;
        border: none !important;
        width: 40px !important;
        height: 60px !important;
    }}
    
    /* Standart oku gizleyip kendi cam göbeği üçgenimizi koyuyoruz */
    [data-testid="stSidebarCollapsedControl"] svg {{
        display: none;
    }}
    
    [data-testid="stSidebarCollapsedControl"]::after {{
        content: '';
        position: absolute;
        left: 0;
        width: 0;
        height: 0;
        border-top: 20px solid transparent;
        border-bottom: 20px solid transparent;
        border-left: 15px solid #00ffff; /* Cam Göbeği Üçgen */
        filter: drop-shadow(0 0 10px rgba(0, 255, 255, 0.8));
        cursor: pointer;
        transition: 0.3s;
    }}
    
    [data-testid="stSidebarCollapsedControl"]:hover::after {{
        border-left: 20px solid #ffffff;
        filter: drop-shadow(0 0 20px #00ffff);
    }}

    /* Üst Menü ve Gereksiz Alanları Gizle */
    #MainMenu, footer, header {{visibility: hidden;}}

    .header-container {{ padding: 80px 0px 40px 8%; }}
    .main-title {{
        font-weight: 100; letter-spacing: -3px; font-size: 6rem;
        color: #00ffff; text-shadow: 0 0 25px rgba(0, 255, 255, 0.4);
    }}
    .sub-title {{ letter-spacing: 10px; color: #444; font-size: 0.8rem; text-transform: uppercase; }}
    
    .visitor-badge {{ 
        position: fixed; bottom: 30px; left: 30px; 
        font-size: 0.7rem; color: #00ffff; opacity: 0.5; letter-spacing: 3px;
    }}

    [data-testid="stImage"] {{ border: 1px solid #111; margin-bottom: 120px; transition: 0.7s; }}
    [data-testid="stImage"]:hover {{ border: 1px solid #00ffff; transform: scale(1.02); }}
    
    [data-testid="column"]:nth-child(2) {{ margin-top: 180px; }}
    
    @media (max-width: 768px) {{
        .main-title {{ font-size: 3.5rem; }}
        [data-testid="column"]:nth-child(2) {{ margin-top: 0px !important; }}
    }}
    </style>
    <div class="visitor-badge">GLOBAL VISITORS // {visitor_no:04d}</div>
    """, unsafe_allow_html=True)

# 4. YAN PANEL İÇERİĞİ
with st.sidebar:
    st.markdown("### 🛠 SETTINGS")
    user_name = st.text_input("Name", "Utku Çimen")
    archive_year = st.text_input("Year", "2026")
    uploaded_images = st.file_uploader("Upload Photos", type=["jpg", "jpeg", "png"], accept_multiple_files=True)
    st.markdown("---")
    st.caption("Paneli kapatmak için sayfaya dokun veya oku kullan.")

# 5. ANA İÇERİK
st.markdown(f"""
    <div class="header-container">
        <div class="main-title">{user_name}</div>
        <div class="sub-title">{archive_year} / PERSONAL ARCHIVE / {len(uploaded_images) if uploaded_images else 0} WORKS</div>
    </div>
    """, unsafe_allow_html=True)

col1, col2 = st.columns(2)
if uploaded_images:
    for i, file in enumerate(uploaded_images):
        if i % 2 == 0:
            with col1: st.image(file, use_container_width=True)
        else:
            with col2: st.image(file, use_container_width=True)
else:
    st.info("Sol kenardaki cam göbeği üçgene tıklayarak fotoğraflarını yükle.")

# 6. ALT BİLGİ
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #008b8b; font-size: 15px; letter-spacing: 5px;'>PORTFOLIO BY {user_name.upper()}</p>", unsafe_allow_html=True)
