import streamlit as st
import os
import random

# 1. ZİYARETÇİ SAYACI
def get_visitor_count():
    file_path = "counter.txt"
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write("0")
    with open(file_path, "r") as f:
        try:
            count = int(f.read())
        except:
            count = 0
    new_count = count + 1
    with open(file_path, "w") as f:
        f.write(str(new_count))
    return new_count

visitor_no = get_visitor_count()

# 2. ARKA PLAN ÖĞELERİ
diamonds = "".join([f'<div class="diamond" style="left:{i*5}%; animation-duration:{12 + i%5}s; animation-delay:{i*0.4}s;"></div>' for i in range(20)])
cameras = "".join([f'<div class="camera-float" style="left:{random.randint(0, 95)}%; animation-duration:{random.randint(15, 25)}s; animation-delay:{random.uniform(0, 10)}s;">📷</div>' for i in range(15)])

# 3. SAYFA AYARI
st.set_page_config(page_title="UTKUÇİMEN | ARCHIVE", layout="wide", initial_sidebar_state="collapsed")

# 4. TASARIM + ARKA PLAN ÇİZGİLERİ + INTRO
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@200;400&display=swap');

html, body, [data-testid="stAppViewContainer"] {{
    background-color: #000;
    font-family: 'Manrope', sans-serif;
    color: #FFD700;
    overflow-x: hidden;

    /* ARKA PLAN ÇİZGİLERİ (GERİ GELDİ) */
    background-image: repeating-linear-gradient(
        -45deg,
        #000 0px,
        #000 100px,
        rgba(255, 215, 0, 0.05) 101px,
        rgba(255, 215, 0, 0.05) 103px
    );
    background-size: 500% 500%;
    animation: gradient-flow 80s linear infinite;
}}

@keyframes gradient-flow {{
    0% {{ background-position: 0% 0%; }}
    100% {{ background-position: 100% 100%; }}
}}

/* KARŞILAMA EKRANI */
#intro-layer {{
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: #000;
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 9999;
    animation: fadeOutUp 1s ease-in-out 4s forwards;
}}

.intro-text {{
    font-size: 15vw;
    font-weight: 200;
    letter-spacing: -10px;
    color: #FFD700;
    text-transform: uppercase;
    white-space: nowrap;
    animation: textGlow 2s infinite alternate;
}}

@keyframes textGlow {{
    from {{ text-shadow: 0 0 20px rgba(255,215,0,0.2); opacity: 0.6; }}
    to {{ text-shadow: 0 0 70px rgba(255,215,0,0.9); opacity: 1; }}
}}

@keyframes fadeOutUp {{
    0% {{ transform: translateY(0); }}
    100% {{ transform: translateY(-110%); visibility: hidden; }}
}}

/* ARKA PLAN OBJELERİ */
.bg-overlay {{ position: fixed; width: 100%; height: 100%; top: 0; left: 0; pointer-events: none; z-index: 1; overflow: hidden; }}
.diamond {{ position: absolute; width: 8px; height: 8px; background: rgba(255, 215, 0, 0.08); transform: rotate(45deg); animation: floatUp linear infinite; }}
.camera-float {{ position: absolute; font-size: 1rem; opacity: 0; animation: floatUp linear infinite; filter: brightness(0.6) sepia(1); }}

@keyframes floatUp {{
    0% {{ transform: translateY(110vh) rotate(0deg); opacity: 0; }}
    10% {{ opacity: 0.2; }}
    90% {{ opacity: 0.2; }}
    100% {{ transform: translateY(-10vh) rotate(360deg); opacity: 0; }}
}}

/* BAŞLIK */
.header-container {{ padding: 120px 0px 100px 8%; position: relative; z-index: 10; }}
.main-title {{ font-weight: 200; letter-spacing: -3px; font-size: 7rem; line-height: 0.8; color: #FFD700; }}

/* FOTOĞRAFLAR */
[data-testid="stImage"] {{
    transition: all 0.6s ease;
    border: 1px solid rgba(255,215,0,0.15);
    background: rgba(255,215,0,0.02);
}}

[data-testid="column"]:nth-child(2) [data-testid="stImage"] {{
    margin-top: 150px;
}}

[data-testid="stImage"] {{
    margin-bottom: 150px !important;
}}

[data-testid="stImage"]:hover {{
    transform: scale(1.03);
    border: 1px solid #FFD700;
    box-shadow: 0 0 50px rgba(255,215,0,0.25);
}}

.visitor-badge {{ position: fixed; bottom: 30px; left: 30px; font-size: 0.6rem; color: #FFD700; letter-spacing: 4px; opacity: 0.6; z-index: 20; }}
#MainMenu, footer, header {{visibility: hidden;}}
</style>

<div id="intro-layer">
    <div class="intro-text">Utku Çimen</div>
</div>

<div class="bg-overlay">
    {diamonds}
    {cameras}
</div>

<div class="visitor-badge">ARCHIVE_SYSTEM // {visitor_no:05d}</div>
""", unsafe_allow_html=True)

# 5. İÇERİK
st.markdown(f"""
<div class="header-container">
    <div class="main-title">Utku Çimen</div>
    <div style="letter-spacing: 10px; color: #554400; font-size: 0.7rem; margin-top:20px;">
        2026 / OFFSET_LAYOUT / INDEX_09
    </div>
</div>
""", unsafe_allow_html=True)

# 6. FOTOĞRAFLAR
col1, col2 = st.columns(2)
photos = ["9.jpg", "2.jpg", "3.jpg", "4.jpg", "8.jpg", "1.jpg"]

for i, url in enumerate(photos):
    if i % 2 == 0:
        with col1:
            st.image(url, use_container_width=True)
    else:
        with col2:
            st.image(url, use_container_width=True)

st.markdown("<br><br><br><p style='text-align:center; color:#333; letter-spacing:10px; font-size:0.6rem;'>UTKU ÇİMEN PORTFOLIO // GOLD_EDITION</p>", unsafe_allow_html=True)
