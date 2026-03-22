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

# 3. KÖKTEN ÇÖZÜM: YÜZEN AYAR BUTONU VE TASARIM
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

    /* EKRANIN SOLUNA YAPIŞIK DEVASA TETİKLEYİCİ */
    .custom-trigger {{
        position: fixed;
        left: 0;
        top: 45%;
        width: 30px;
        height: 100px;
        background-color: rgba(0, 255, 255, 0.2);
        border: 1px solid #00ffff;
        border-left: none;
        border-radius: 0 10px 10px 0;
        z-index: 999999;
        cursor: pointer;
        display: flex;
        align-items: center;
        justify-content: center;
        transition: 0.3s;
        box-shadow: 0 0 15px rgba(0, 255, 255, 0.3);
    }}
    
    .custom-trigger:hover {{
        width: 45px;
        background-color: rgba(0, 255, 255, 0.8);
        box-shadow: 0 0 30px rgba(0, 255, 255, 0.6);
    }}

    .custom-trigger::after {{
        content: '>';
        color: white;
        font-weight: bold;
        font-size: 20px;
    }}

    /* Menü ve Header Gizleme */
    #MainMenu, footer, header {{visibility: hidden;}}

    .header-container {{ padding: 80px 0px 40px 8%; }}
    .main-title {{
        font-weight: 100; letter-spacing: -3px; font-size: 6rem;
        color: #00ffff; text-shadow: 0 0 25px rgba(0, 255, 255, 0.4);
    }}
    .sub-title {{ letter-spacing: 10px; color: #444; font-size: 0.8rem; text-transform: uppercase; }}
    
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
    
    <div class="custom-trigger" onclick="document.querySelector('.st-emotion-cache-hp8886').click()"></div>
    
    <div class="visitor-badge">GLOBAL VISITORS // {visitor_no:04d}</div>
    """, unsafe_allow_html=True)

# 4. YAN PANEL İÇERİĞİ
with st.sidebar:
    st.markdown("### 🛠 SETTINGS")
    user_name = st.text_input("Name", "Utku Çimen")
    archive_year = st.text_input("Year", "2026")
    uploaded_images = st.file_uploader("Upload Photos", type=["jpg", "jpeg", "png"], accept_multiple_files=True)
    st.markdown("---")
    st.info("Panelden çıkmak için boş bir yere tıklayın.")

# 5. ANA İÇERİK
st.markdown(f"""
    <div class="header-container">
        <div class="main-title">{user_name}</div>
        <div class="sub-title">{archive_year} / PERSONAL ARŞİV / {len(uploaded_images) if uploaded_images else 0} WORKS</div>
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
    st.info("Sol kenardaki cam göbeği çubuğa tıklayarak ayarları açabilirsin.")

# 6. ALT BİLGİ
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #008b8b; font-size: 15px; letter-spacing: 5px;'>PORTFOLIO BY {user_name.upper()}</p>", unsafe_allow_html=True)
