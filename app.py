import streamlit as st
import os

# 1. ZİYARETÇİ SAYACI (Dosya tabanlı basit sayaç)
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
st.set_page_config(page_title="PERSONAL ARCHIVE", layout="wide", initial_sidebar_state="expanded")

# 3. YAN PANEL (KİŞİSELLEŞTİRME ARAÇLARI)
with st.sidebar:
    st.markdown("### 🛠 ÖZELLEŞTİR")
    user_name = st.text_input("Adınız Soyadınız", "Utku Çimen")
    archive_year = st.text_input("Arşiv Yılı", "2026")
    
    st.markdown("---")
    st.markdown("### 📸 FOTOĞRAFLARINI YÜKLE")
    uploaded_images = st.file_uploader("En fazla 10 fotoğraf seç", type=["jpg", "jpeg", "png"], accept_multiple_files=True)
    
    st.markdown("---")
    st.info("Fotoğrafları yüklediğinde sağdaki galeri anında güncellenir.")

# 4. ÖZEL CSS (Tasarımını bozmadan dinamik hale getirdik)
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

    .header-container {{
        padding: 80px 0px 40px 8%;
        position: relative;
        z-index: 10;
    }}
    .main-title {{
        font-weight: 100;
        letter-spacing: -3px;
        font-size: 6rem;
        line-height: 0.8;
        color: #00ffff; 
        text-shadow: 0 0 25px rgba(0, 255, 255, 0.4);
    }}
    .sub-title {{
        letter-spacing: 10px;
        color: #444;
        font-size: 0.8rem;
        text-transform: uppercase;
        margin-top: 15px;
    }}

    .visitor-badge {{
        position: fixed; bottom: 30px; left: 30px;
        font-size: 0.7rem; color: #00ffff;
        letter-spacing: 4px; z-index: 100; opacity: 0.6;
    }}

    @media (max-width: 768px) {{
        .main-title {{ font-size: 3.5rem; }}
        [data-testid="column"]:nth-child(2) {{ margin-top: 0px !important; }}
    }}

    @media (min-width: 769px) {{
        [data-testid="column"]:nth-child(2) {{ margin-top: 180px; }}
    }}

    [data-testid="stImage"] {{
        border-radius: 0px;
        margin-bottom: 100px;
        border: 1px solid #111;
        transition: all 0.7s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    [data-testid="stImage"]:hover {{
        transform: scale(1.03);
        border: 1px solid #00ffff;
        box-shadow: 0px 0px 40px rgba(0, 255, 255, 0.25);
    }}

    #MainMenu, footer, header {{visibility: hidden;}}
    </style>
    
    <div class="visitor-badge">GLOBAL VISITORS // {visitor_no:04d}</div>
    """, unsafe_allow_html=True)

# 5. DİNAMİK BAŞLIK
st.markdown(f"""
    <div class="header-container">
        <div class="main-title">{user_name}</div>
        <div class="sub-title">{archive_year} / KİŞİSEL ARŞİV / {len(uploaded_images) if uploaded_images else 0} WORKS</div>
    </div>
    """, unsafe_allow_html=True)

# 6. DİNAMİK VİTRİN
col1, col2 = st.columns(2)

if uploaded_images:
    for i, file in enumerate(uploaded_images):
        if i % 2 == 0:
            with col1:
                st.image(file, use_container_width=True)
        else:
            with col2:
                st.image(file, use_container_width=True)
else:
    st.info("Sol taraftaki panelden fotoğraflarını yükleyerek kendi arşivini oluşturmaya başla! ✨")

# 7. ALT BİLGİ
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #008b8b; font-size: 15px; letter-spacing: 5px;'>DESIGNED BY {user_name.upper()}</p>", unsafe_allow_html=True)
