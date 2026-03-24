import streamlit as st
import os
import random

# 1. SAYFA AYARI
st.set_page_config(page_title="UTKUÇİMEN | ARCHIVE", layout="wide", initial_sidebar_state="collapsed")

# 2. JS İLE OTO-YENİLEME (5 SAAT)
st.components.v1.html(
    """
    <script>
    setTimeout(function(){ window.location.reload(); }, 18000000);
    </script>
    """,
    height=0,
)

# 3. ZİYARETÇİ SAYACI
def get_visitor_count():
    file_path = "counter.txt"
    if not os.path.exists(file_path):
        with open(file_path, "w") as f: f.write("0")
    with open(file_path, "r") as f:
        try:
            line = f.read().strip()
            count = int(line) if line else 0
        except:
            count = 0
    if 'counted' not in st.session_state:
        count += 1
        with open(file_path, "w") as f: f.write(str(count))
        st.session_state['counted'] = True
    return count

visitor_no = get_visitor_count()

# 4. ARKA PLAN ÖĞELERİ
@st.cache_data
def get_static_elements():
    diamond_floats = "".join([f'<div class="diamond-float" style="left:{random.randint(0, 95)}%; animation-duration:{random.randint(10, 20)}s; animation-delay:{random.uniform(0, 5)}s;">💎</div>' for i in range(15)])
    camera_floats = "".join([f'<div class="camera-float" style="left:{random.randint(0, 95)}%; animation-duration:{random.randint(15, 25)}s; animation-delay:{random.uniform(0, 5)}s;">📷</div>' for i in range(10)])
    return diamond_floats, camera_floats

diamond_floats, camera_floats = get_static_elements()

# 5. CSS + HTML (Çizgiler belirginleştirildi: opacity 0.05 -> 0.15)
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@200;400&display=swap');

html, body, [data-testid="stAppViewContainer"] {{
    background-color: #000;
    font-family: 'Manrope', sans-serif;
    color: #FFD700;
    overflow-x: hidden;
    
    /* ÇİZGİLER BURADA GÜNCELLENDİ (Daha opak ve net) */
    background-image: repeating-linear-gradient(
        -45deg, 
        #000 0px, 
        #000 60px, 
        rgba(255, 215, 0, 0.15) 61px, 
        rgba(255, 215, 0, 0.15) 63px
    );
    background-size: 200% 200%;
    animation: gradient-flow 80s linear infinite;
}}

@keyframes gradient-flow {{ 0% {{ background-position: 0% 0%; }} 100% {{ background-position: 100% 100%; }} }}

#intro-layer {{ position: fixed; top: 0; left: 0; width: 100%; height: 100%; background-color: #000; display: flex; justify-content: center; align-items: center; z-index: 9999; animation: fadeOutUp 1s ease-in-out 2s forwards; }}
.intro-text {{ font-size: 15vw; font-weight: 200; letter-spacing: -10px; color: #FFD700; text-transform: uppercase; white-space: nowrap; animation: textGlow 2s infinite alternate; }}
@keyframes textGlow {{ from {{ text-shadow: 0 0 20px rgba(255,215,0,0.3); opacity: 0.6; }} to {{ text-shadow: 0 0 80px rgba(255,215,0,1); opacity: 1; }} }}
@keyframes fadeOutUp {{ 0% {{ transform: translateY(0); }} 100% {{ transform: translateY(-110%); visibility: hidden; }} }}

.bg-overlay {{ 
    position: fixed; 
    width: 100%; 
    height: 100%; 
    top: 0; 
    left: 0; 
    pointer-events: none; 
    z-index: 0; 
    overflow: hidden;
}}

.diamond-float {{ position: absolute; font-size: 1.2rem; opacity: 0.35; animation: floatDown linear infinite; }}
.camera-float {{ position: absolute; font-size: 1rem; opacity: 0.15; animation: floatUp linear infinite; }}

@keyframes floatDown {{ 0% {{ transform: translateY(-15vh) rotate(0deg); opacity: 0; }} 10% {{ opacity: 0.35; }} 90% {{ opacity: 0.35; }} 100% {{ transform: translateY(115vh) rotate(360deg); opacity: 0; }} }}
@keyframes floatUp {{ 0% {{ transform: translateY(115vh) rotate(0deg); opacity: 0; }} 10% {{ opacity: 0.15; }} 90% {{ opacity: 0.15; }} 100% {{ transform: translateY(-15vh) rotate(-360deg); opacity: 0; }} }}

.header-container {{ padding: 120px 0px 100px 8%; position: relative; z-index: 10; }}
.main-title {{ font-weight: 200; letter-spacing: -3px; font-size: 7rem; line-height: 0.8; color: #FFD700; }}

[data-testid="stImage"] {{ 
    transition: all 0.6s ease; 
    border: 1px solid rgba(255,215,0,0.3); 
    background: rgba(0,0,0,0.7); 
    margin-bottom: 150px !important; 
    position: relative; 
    z-index: 2; 
}}

[data-testid="column"]:nth-child(2) [data-testid="stImage"] {{ margin-top: 150px; }}
[data-testid="stImage"]:hover {{ transform: scale(1.02); border: 1px solid #FFD700; box-shadow: 0 0 40px rgba(255,215,0,0.25); }}

.visitor-badge {{ position: fixed; bottom: 30px; left: 30px; font-size: 0.6rem; color: #FFD700; letter-spacing: 4px; opacity: 0.8; z-index: 20; }}
#MainMenu, footer, header {{visibility: hidden;}}
</style>

<div id="intro-layer"><div class="intro-text">Utku Çimen</div></div>

<div class="bg-overlay">
    {diamond_floats}
    {camera_floats}
</div>

<div class="visitor-badge">ARCHIVE_SYSTEM // {visitor_no:05d} 💎 📷</div>
""", unsafe_allow_html=True)

# 6. İÇERİK
st.markdown('<div class="header-container"><div class="main-title">Utku Çimen</div><div style="letter-spacing: 12px; color: #B8860B; font-size: 0.75rem; margin-top:20px; font-weight: 400;">2026 / OFFSET_LAYOUT / INDEX_09</div></div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
photos = ["9.jpg", "2.jpg", "3.jpg", "4.jpg", "8.jpg", "1.jpg"]

for i, url in enumerate(photos):
    target = col1 if i % 2 == 0 else col2
    with target:
        st.image(url, use_container_width=True)

st.markdown("<br><br><br><p style='text-align:center; color:#554400; letter-spacing:10px; font-size:0.65rem;'>UTKU ÇİMEN PORTFOLIO // GOLD_EDITION_V2</p>", unsafe_allow_html=True)
