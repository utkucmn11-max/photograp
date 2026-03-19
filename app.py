import streamlit as st
import os

# 1. ZİYARETÇİ SAYACI FONKSİYONU
def get_visitor_count():
    file_path = "counter.txt"
    # Dosya yoksa oluştur ve 0 yaz
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write("0")
    
    # Mevcut sayıyı oku ve 1 artır
    with open(file_path, "r") as f:
        try:
            count = int(f.read())
        except:
            count = 0
    
    new_count = count + 1
    
    # Yeni sayıyı dosyaya kaydet
    with open(file_path, "w") as f:
        f.write(str(new_count))
    
    return new_count

# Sayacı çalıştır
visitor_no = get_visitor_count()

# 2. SAYFA AYARLARI
st.set_page_config(page_title="UTKUÇİMEN| ARCHIVE", layout="wide", initial_sidebar_state="collapsed")

# 3. ÖZEL CSS (Cam Göbeği & Saf Siyah & Hareketli Arka Plan)
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;400&display=swap');

    html, body, [data-testid="stAppViewContainer"] {{
        background-color: #000000;
        font-family: 'Inter', sans-serif;
        color: #ffffff;
        
        /* CAM GÖBEĞİ ÇİZGİLER */
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

    /* Başlık Alanı */
    .header-container {{
        padding: 100px 0px 60px 8%;
        position: relative;
        z-index: 10;
    }}
    .main-title {{
        font-weight: 100;
        letter-spacing: -3px;
        font-size: 7rem;
        line-height: 0.8;
        color: #00ffff; 
        text-shadow: 0 0 25px rgba(0, 255, 255, 0.4);
    }}
    .sub-title {{
        letter-spacing: 10px;
        color: #444;
        font-size: 0.8rem;
        text-transform: uppercase;
        margin-top: 10px;
    }}

    /* GÜNCELLENDİ: SOL KÖŞE SAYAÇ TASARIMI */
    .visitor-badge {{
        position: fixed;
        bottom: 30px;
        left: 30px; /* Sol köşeye çekildi */
        font-size: 0.7rem;
        color: #00ffff; /* Daha net cam göbeği */
        letter-spacing: 4px;
        z-index: 100;
        opacity: 0.6;
        font-weight: 400;
    }}

    /* Mobil Ayarlar */
    @media (max-width: 768px) {{
        .main-title {{ font-size: 4rem; }}
        [data-testid="column"]:nth-child(2) {{ margin-top: 0px !important; }}
        .visitor-badge {{ left: 15px; bottom: 15px; font-size: 0.6rem; }}
    }}

    /* Masaüstü Sütun Kaydırma */
    @media (min-width: 769px) {{
        [data-testid="column"]:nth-child(2) {{ margin-top: 180px; }}
    }}

    /* Fotoğraflar */
    [data-testid="stImage"] {{
        border-radius: 0px;
        margin-bottom: 120px;
        border: 1px solid #111;
        transition: all 0.7s cubic-bezier(0.16, 1, 0.3, 1);
        position: relative;
        z-index: 5;
    }}
    [data-testid="stImage"]:hover {{
        transform: scale(1.03);
        border: 1px solid #00ffff;
        box-shadow: 0px 0px 40px rgba(0, 255, 255, 0.25);
        cursor: crosshair;
    }}

    #MainMenu, footer, header {{visibility: hidden;}}
    </style>
    
    <div class="visitor-badge">VISITORS // {visitor_no:04d}</div>
    """, unsafe_allow_html=True)

# 4. BAŞLIK İÇERİĞİ
st.markdown("""
    <div class="header-container">
        <div class="main-title">Utku Çimen </div>
        <div class="sub-title">2026 / Kişisel Arşiv / 09 Works</div>
    </div>
    """, unsafe_allow_html=True)

# 5. VİTRİN (ASİMETRİK)
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

# 6. ALT BİLGİ
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #008b8b; font-size: 20px; letter-spacing: 5px; position: relative; z-index: 10;'>Bu site Utku Çimen tarafından yapılmıştır.</p>", unsafe_allow_html=True)
