import streamlit as st
import os

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

# 2. SAYFA AYARI
st.set_page_config(
    page_title="UTKUÇİMEN | ARCHIVE",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 3. PREMIUM TASARIM
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@200;400&display=swap');

html, body, [data-testid="stAppViewContainer"] {{
    background-color: #000;
    font-family: 'Manrope', sans-serif;
    color: #fff;
    cursor: crosshair;

    background-image: repeating-linear-gradient(
        -45deg,
        #000 0px,
        #000 100px,
        rgba(0,255,255,0.05) 101px,
        rgba(0,255,255,0.05) 103px
    );
    background-size: 200% 200%;
    animation: gradient-flow 60s linear infinite;
}}

@keyframes gradient-flow {{
    0% {{ background-position: 0% 0%; }}
    100% {{ background-position: 100% 100%; }}
}}

.header-container {{
    padding: 100px 0px 60px 8%;
}}

.main-title {{
    font-weight: 200;
    letter-spacing: -3px;
    font-size: 7rem;
    line-height: 0.8;
    color: #00ffff;
    animation: glowPulse 3s infinite alternate;
}}

@keyframes glowPulse {{
    from {{ text-shadow: 0 0 10px rgba(0,255,255,0.3); }}
    to {{ text-shadow: 0 0 40px rgba(0,255,255,0.9); }}
}}

.sub-title {{
    letter-spacing: 10px;
    color: #444;
    font-size: 0.8rem;
    text-transform: uppercase;
    margin-top: 10px;
}}

[data-testid="stImage"] {{
    margin-bottom: 120px;
    border: 1px solid rgba(0,255,255,0.1);
    backdrop-filter: blur(10px);
    background: rgba(255,255,255,0.02);
    transition: all 0.7s cubic-bezier(0.16, 1, 0.3, 1);
    position: relative;

    opacity: 0;
    transform: translateY(40px);
    animation: fadeUp 1s ease forwards;
}}

[data-testid="stImage"]:hover {{
    transform: scale(1.03);
    border: 1px solid #00ffff;
    box-shadow: 0px 0px 40px rgba(0,255,255,0.25);
}}

[data-testid="stImage"]::after {{
    content: "VIEW";
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%) scale(0.8);
    color: #00ffff;
    opacity: 0;
    transition: 0.4s;
    letter-spacing: 5px;
}}

[data-testid="stImage"]:hover::after {{
    opacity: 1;
    transform: translate(-50%, -50%) scale(1);
}}

@keyframes fadeUp {{
    to {{
        opacity: 1;
        transform: translateY(0px);
    }}
}}

.visitor-badge {{
    position: fixed;
    bottom: 30px;
    left: 30px;
    font-size: 0.7rem;
    color: #00ffff;
    letter-spacing: 4px;
    opacity: 0.6;
}}

@media (max-width: 768px) {{
    .main-title {{ font-size: 4rem; }}
    .visitor-badge {{ left: 15px; bottom: 15px; }}
}}

#MainMenu, footer, header {{visibility: hidden;}}
</style>

<!-- HATASIZ MOUSE GLOW -->
<script>
document.addEventListener("mousemove", function(e) {{
    const x = e.clientX;
    const y = e.clientY;
    document.body.style.backgroundImage =
        "radial-gradient(circle at " + x + "px " + y + "px, rgba(0,255,255,0.08), transparent 300px)," +
        "repeating-linear-gradient(-45deg,#000 0px,#000 100px,rgba(0,255,255,0.05) 101px,rgba(0,255,255,0.05) 103px)";
}});
</script>

<div class="visitor-badge">VISITORS // {visitor_no:04d}</div>
""", unsafe_allow_html=True)

# 4. BAŞLIK
st.markdown("""
<div class="header-container">
    <div class="main-title">Utku Çimen</div>
    <div class="sub-title">2026 / Kişisel Arşiv / 09 Works</div>
</div>
""", unsafe_allow_html=True)

# 5. FOTOĞRAFLAR
col1, col2 = st.columns(2)

photos = [
    "9.jpg",
    "2.jpg",
    "3.jpg",
    "4.jpg",
    "8.jpg",
    "1.jpg",
]

for i, url in enumerate(photos):
    if i % 2 == 0:
        with col1:
            st.image(url, use_container_width=True)
    else:
        with col2:
            st.image(url, use_container_width=True)

# 6. ALT YAZI
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center; color:#008b8b; font-size:20px; letter-spacing:5px;'>Bu site Utku Çimen tarafından yapılmıştır.</p>",
    unsafe_allow_html=True
)
