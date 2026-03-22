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

# 2. PANEL DURUMU KONTROLÜ (Session State)
if 'sidebar_state' not in st.session_state:
    st.session_state.sidebar_state = 'collapsed'

# 3. SAYFA AYARLARI
st.set_page_config(
    page_title="PERSONAL ARCHIVE", 
    layout="wide", 
    initial_sidebar_state=st.session_state.sidebar_state
)

# 4. ÖZEL CSS
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

    #MainMenu, footer, header {{visibility: hidden;}}
    
    /* SET BUTONU TASARIMI */
    .stButton > button {{
        position: fixed;
        top: 20px;
        right: 40px;
        background-color: transparent;
        color: #00ffff;
        border: 1px solid #00ffff;
        border-radius: 0px;
        padding: 5px 15px;
        z-index: 1000;
        letter-spacing: 3px;
    }}

    .header-container {{ padding: 80px 0px 40px 8%; }}
    .main-title {{
        font-weight: 100; letter-spacing: -3px; font-size: 6rem;
        color: #00ffff; text-shadow: 0 0 25px rgba(0, 255, 255, 0.4);
    }}
    .sub-title {{ letter-spacing: 10px; color: #444; font-size: 0.8rem; text-transform: uppercase; }}
    .visitor-badge {{ position: fixed; bottom: 30px; left: 30px; font-size: 0.7rem; color: #00ffff; opacity: 0.6; }}

    [data-testid="stImage"] {{ border: 1px solid #111; margin-bottom: 120px; }}
    [data-testid="column"]:nth-child(2) {{ margin-top: 180px; }}
    
    @media (max-width: 768px) {{
        .main-title {{ font-size: 3.5rem; }}
        [data-testid="column"]:nth-child(2) {{ margin-top: 0px !important; }}
    }}
    </style>
    <div class="visitor-badge">GLOBAL VISITORS // {visitor_no:04d}</div>
    """, unsafe_allow_html=True)

# 5. SET BUTONU MANTIĞI
if st.button("SET"):
    # Butona basılınca durumu "expanded" yap ve sayfayı yenile
    st.session_state.sidebar_state = 'expanded' if st.session_state.sidebar_state == 'collapsed' else 'collapsed'
    st.rerun()

# 6. YAN PANEL İÇERİĞİ
with st.sidebar:
    st.markdown("### 🛠 CONTROL CENTER")
    user_name = st.text_input("Name / Nickname", "Utku Çimen")
    archive_year = st.text_input("Year", "2026")
    uploaded_images = st.file_uploader("Select images", type=["jpg", "jpeg", "png"], accept_multiple_files=True)
    
    if st.button("CLOSE"):
        st.session_state.sidebar_state = 'collapsed'
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
    st.info("Kendi arşivini oluşturmak için sağ üstteki SET butonuna bas.")

st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #008b8b; font-size: 15px; letter-spacing: 5px;'>PORTFOLIO BY {user_name.upper()}</p>", unsafe_allow_html=True)
