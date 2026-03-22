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

# 2. PANEL DURUMU (SESSION STATE) - Bu kısım butonun çalışmasını sağlar
if 'sidebar_state' not in st.session_state:
    st.session_state.sidebar_state = 'collapsed'

# 3. SAYFA AYARLARI
st.set_page_config(
    page_title="PERSONAL ARCHIVE", 
    layout="wide", 
    initial_sidebar_state=st.session_state.sidebar_state
)

# 4. ÖZEL CSS (Neon Buton ve Tasarım)
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

    /* STANDART MENÜLERİ GİZLE */
    #MainMenu, footer, header {{visibility: hidden;}}
    [data-testid="stSidebarCollapsedControl"] {{display: none;}}

    /* NEON SET BUTONU TASARIMI */
    .stButton > button {{
        background-color: transparent !important;
        color: #00ffff !important;
        border: 1px solid #00ffff !important;
        border-radius: 0px !important;
        width: 100% !important;
        letter-spacing: 5px !important;
        font-weight: 100 !important;
        transition: 0.5s !important;
        margin-top: 20px;
    }}
    .stButton > button:hover {{
        background-color: rgba(0, 255, 255, 0.1) !important;
        box-shadow: 0 0 20px rgba(0, 255, 255, 0.3) !important;
    }}

    .header-container {{ padding: 40px 0px 40px 8%; }}
    .main-title {{
        font-weight: 100; letter-spacing: -3px; font-size: 6rem;
        color: #00ffff; text-shadow: 0 0 25px rgba(0, 255, 255, 0.4);
        line-height: 0.8;
    }}
    .sub-title {{ letter-spacing: 10px; color: #444; font-size: 0.8rem; text-transform: uppercase; margin-top: 20px; }}
    
    .visitor-badge {{ 
        position: fixed; bottom: 30px; left: 30px; 
        font-size: 0.7rem; color: #00ffff; opacity: 0.5;
    }}

    [data-testid="column"]:nth-child(2) {{ margin-top: 180px; }}
    
    @media (max-width: 768px) {{
        .main-title {{ font-size: 3.5rem; }}
        [data-testid="column"]:nth-child(2) {{ margin-top: 0px !important; }}
    }}
    </style>
    
    <div class="visitor-badge">GLOBAL VISITORS // {visitor_no:04d}</div>
    """, unsafe_allow_html=True)

# 5. AYAR BUTONU (Sayfanın En Üstünde)
col_set1, col_set2, col_set3 = st.columns([4, 2, 4])
with col_set2:
    if st.button("OPEN SETTINGS"):
        st.session_state.sidebar_state = "expanded"
        st.rerun()

# 6. YAN PANEL İÇERİĞİ
with st.sidebar:
    st.markdown("### 🛠 KONTROL PANELİ")
    user_name = st.text_input("İsim Yazın", "Utku Çimen")
    archive_year = st.text_input("Yıl", "2026")
    uploaded_images = st.file_uploader("Fotoğrafları Sürükle", type=["jpg", "jpeg", "png"], accept_multiple_files=True)
    
    st.markdown("---")
    if st.button("KAPAT"):
        st.session_state.sidebar_state = "collapsed"
        st.rerun()

# 7. ANA İÇERİK
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
    st.info("Kendi arşivini oluşturmak için yukarıdaki 'OPEN SETTINGS' butonuna tıkla.")

# 8. ALT BİLGİ
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #008b8b; font-size: 15px; letter-spacing: 5px;'>PORTFOLIO BY {user_name.upper()}</p>", unsafe_allow_html=True)
