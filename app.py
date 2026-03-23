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

# 4. TASARIM
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@200;400&display=swap');

html, body, [data-testid="stAppViewContainer"] {{
    background-color: #000;
    font-family: 'Manrope', sans-serif;
    color: #fff;
    overflow-x: hidden;
}}

/* ARKA PLAN */
.bg-overlay {{ position: fixed; width: 100%; height: 100%; top: 0; left: 0; pointer-events: none; z-index: 1; overflow: hidden; }}
.diamond {{ position: absolute; width: 8px; height: 8px; background: rgba(0, 255, 255, 0.05); transform: rotate(45deg); animation: floatUp linear infinite; }}
.camera-float {{ position: absolute; font-size: 1rem; opacity: 0; animation: floatUp linear infinite; filter: brightness(0.3); }}

@keyframes floatUp {{
    0% {{ transform: translateY(110vh) rotate(0deg); opacity: 0; }}
    10% {{ opacity: 0.2; }}
    90% {{ opacity: 0.2; }}
    100% {{ transform: translateY(-10vh) rotate(360deg); opacity: 0; }}
}}

/* BAŞLIK */
.header-container {{ padding: 120px 0px 100px 8%; position: relative; z-index: 10; }}
.main-title {{ font-weight: 200; letter-spacing: -3px; font-size: 7rem; line-height: 0.8; color: #00ffff; }}

/* FOTOĞRAF DÜZENİ */
[data-testid="stImage"] {{
    transition: all 0.6s ease;
    border: 1px solid rgba(0,255,255,0.1);
    background: rgba(255,255,255,0.02);
}}

/* Çapraz görünüm için sağ sütunu aşağı kaydırıyoruz */
[data-testid="column"]:nth-child(2) [data-testid="stImage"] {{
    margin-top: 150px;
}}

[data-testid="stImage"] {{
    margin-bottom: 150px !important;
}}

[data-testid="stImage"]:hover {{
    transform: scale(1.03);
    border: 1px solid #00ffff;
    box-shadow: 0 0 30px rgba(0,255,255,0.2);
}}

.visitor-badge {{ position: fixed; bottom: 30px; left: 30px; font-size: 0.6rem; color: #00ffff; letter-spacing: 4px; opacity: 0.4; z-index: 20; }}
#MainMenu, footer, header {{visibility: hidden;}}
</style>

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
    <div style="letter-spacing: 10px; color: #444; font-size: 0.7rem; margin-top:20px;">
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

st.markdown("<br><br><br><p style='text-align:center; color:#222; letter-spacing:10px; font-size:0.6rem;'>UTKU ÇİMEN PORTFOLIO // VER 2.1</p>", unsafe_allow_html=True)
