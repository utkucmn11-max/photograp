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

# 2. ARKA PLAN ÖĞELERİ (ELMASLAR + KAMERALAR)
diamonds = "".join([f'<div class="diamond" style="left:{i*5}%; animation-duration:{12 + i%5}s; animation-delay:{i*0.4}s;"></div>' for i in range(20)])
cameras = "".join([f'<div class="camera-float" style="left:{random.randint(0, 95)}%; animation-duration:{random.randint(15, 25)}s; animation-delay:{random.uniform(0, 10)}s;">📷</div>' for i in range(15)])

# 3. SAYFA AYARI
st.set_page_config(page_title="UTKUÇİMEN | ARCHIVE", layout="wide", initial_sidebar_state="collapsed")

# 4. TASARIM + EFEKTLER + YENİ PARÇACIK SİSTEMİ
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@200;400&display=swap');

html, body, [data-testid="stAppViewContainer"] {{
    background-color: #000;
    font-family: 'Manrope', sans-serif;
    color: #fff;
    cursor: none; /* Fare imlecini gizleyip yerine özel takipçi koyacağız */
    overflow-x: hidden;
}}

/* ÖZEL FARE TAKİPÇİSİ (INTERAKTIF NOKTA) */
#cursor-dot {{
    width: 4px;
    height: 4px;
    background-color: #00ffff;
    position: fixed;
    border-radius: 50%;
    pointer-events: none;
    z-index: 9999;
    transition: transform 0.1s ease-out;
    box-shadow: 0 0 15px #00ffff, 0 0 30px #00ffff;
}}

#cursor-outline {{
    width: 30px;
    height: 30px;
    border: 1px solid rgba(0, 255, 255, 0.4);
    position: fixed;
    border-radius: 50%;
    pointer-events: none;
    z-index: 9998;
    transition: transform 0.15s ease-out;
}}

/* ARKA PLAN */
.bg-overlay {{
    position: fixed; width: 100%; height: 100%; top: 0; left: 0;
    pointer-events: none; z-index: 1; overflow: hidden;
}}

.diamond {{
    position: absolute; width: 8px; height: 8px; background: rgba(0, 255, 255, 0.05);
    transform: rotate(45deg); animation: floatUp linear infinite;
}}

.camera-float {{
    position: absolute; font-size: 1rem; opacity: 0; animation: floatUp linear infinite;
    filter: grayscale(1) brightness(0.3);
}}

@keyframes floatUp {{
    0% {{ transform: translateY(110vh) rotate(0deg); opacity: 0; }}
    10% {{ opacity: 0.2; }}
    90% {{ opacity: 0.2; }}
    100% {{ transform: translateY(-10vh) rotate(360deg); opacity: 0; }}
}}

/* BAŞLIK */
.header-container {{ padding: 100px 0px 60px 8%; position: relative; z-index: 10; }}
.main-title {{
    font-weight: 200; letter-spacing: -3px; font-size: 7rem; line-height: 0.8;
    color: #00ffff; animation: glowPulse 3s infinite alternate;
}}
@keyframes glowPulse {{
    from {{ text-shadow: 0 0 10px rgba(0,255,255,0.2); }}
    to {{ text-shadow: 0 0 30px rgba(0,255,255,0.6); }}
}}

/* GÖRSELLER */
[data-testid="stImage"] {{
    margin-bottom: 120px; border: 1px solid rgba(0,255,255,0.05);
    transition: all 0.8s cubic-bezier(0.16, 1, 0.3, 1);
    filter: grayscale(1);
}}
[data-testid="stImage"]:hover {{
    transform: scale(1.02) translateY(-10px);
    border: 1px solid #00ffff;
    filter: grayscale(0);
    box-shadow: 0 20px 40px rgba(0,255,255,0.1);
}}

.visitor-badge {{
    position: fixed; bottom: 30px; left: 30px; font-size: 0.6rem;
    color: #00ffff; letter-spacing: 4px; opacity: 0.4; z-index: 20;
}}

#MainMenu, footer, header {{visibility: hidden;}}
</style>

<div id="cursor-dot"></div>
<div id="cursor-outline"></div>

<div class="bg-overlay">
    {diamonds}
    {cameras}
</div>

<script>
const dot = document.getElementById("cursor-dot");
const outline = document.getElementById("cursor-outline");

window.addEventListener("mousemove", (e) => {{
    const x = e.clientX;
    const y = e.clientY;
    
    dot.style.transform = `translate(${{x}}px, ${{y}}px)`;
    outline.style.transform = `translate(${{x - 13}}px, ${{y - 13}}px)`;
    
    // Dinamik Arka Plan Parlaması
    document.body.style.background = `radial-gradient(circle at ${{x}}px ${{y}}px, rgba(0,255,255,0.05) 0%, black 60%)`;
}});
</script>

<div class="visitor-badge">DATA_STREAM // {visitor_no:05d}</div>
""", unsafe_allow_html=True)

# 5. İÇERİK
st.markdown(f"""
<div class="header-container">
    <div class="main-title">Utku Çimen</div>
    <div style="letter-spacing: 8px; color: #666; font-size: 0.7rem; margin-top:15px;">
        EST. 2026 / MULTIMEDIA ARCHIVE / INDEX: 09
    </div>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
photos = ["9.jpg", "2.jpg", "3.jpg", "4.jpg", "8.jpg", "1.jpg"]

for i, url in enumerate(photos):
    with (col1 if i % 2 == 0 else col2):
        st.image(url, use_container_width=True)

st.markdown("<br><br><br><p style='text-align:center; color:#222; letter-spacing:10px; font-size:0.6rem;'>DESIGNED BY UTKU ÇİMEN © 2026</p>", unsafe_allow_html=True)
