import streamlit as st
import os
import time
import requests
import threading
import schedule
from datetime import datetime

# ==========================================
# 1. OTOMATİK GİRİŞ (BOT) FONKSİYONU
# ==========================================
def bot_gorevi():
    # Sitenin yerel veya yayınlanmış adresini buraya yazabilirsin
    # Eğer Streamlit Cloud'da kullanacaksan linki oradakiyle değiştir.
    url = "http://localhost:8501" 
    
    def siteye_gir():
        try:
            response = requests.get(url)
            print(f"[{datetime.now()}] Otomatik giriş başarılı: {response.status_code}")
        except:
            print(f"[{datetime.now()}] Siteye henüz ulaşılamıyor (Bot beklemede...)")

    # Her gün saat 00:01'de çalışacak şekilde ayarla
    schedule.every().day.at("00:01").do(siteye_gir)

    while True:
        schedule.run_pending()
        time.sleep(30) # Her 30 saniyede bir saati kontrol et

# Botu ana koddan bağımsız, arka planda başlat (Sadece 1 kez)
if "bot_started" not in st.session_state:
    thread = threading.Thread(target=bot_gorevi, daemon=True)
    thread.start()
    st.session_state.bot_started = True

# ==========================================
# 2. ZİYARETÇİ SAYACI
# ==========================================
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

# ==========================================
# 3. SAYFA AYARLARI VE TASARIM (CSS)
# ==========================================
st.set_page_config(page_title="UTKUÇİMEN| ARCHIVE", layout="wide", initial_sidebar_state="collapsed")

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

    .header-container {{ padding: 100px 0px 60px 8%; position: relative; z-index: 10; }}
    .main-title {{ font-weight: 100; letter-spacing: -3px; font-size: 7rem; line-height: 0.8; color: #00ffff; text-shadow: 0 0 25px rgba(0, 255, 255, 0.4); }}
    .sub-title {{ letter-spacing: 10px; color: #444; font-size: 0.8rem; text-transform: uppercase; margin-top: 10px; }}

    .visitor-badge {{
        position: fixed;
        bottom: 30px;
        left: 30px;
        font-size: 0.7rem;
        color: #00ffff;
        letter-spacing: 4px;
        z-index: 100;
        opacity: 0.6;
        font-weight: 400;
    }}

    /* Fotoğraflar */
    [data-testid="stImage"] {{
        border-radius: 0px;
        margin-bottom: 120px;
        border: 1px solid #111;
        transition: all 0.7s cubic-bezier(0.16, 1, 0.3, 1);
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

# 4. BAŞLIK
st.markdown("""
    <div class="header-container">
        <div class="main-title">Utku Çimen</div>
        <div class="sub-title">2026 / Kişisel Arşiv / 09 Works</div>
    </div>
    """, unsafe_allow_html=True)

# 5. VİTRİN
col1, col2 = st.columns(2)
photos = ["9.jpg", "2.jpg", "3.jpg", "4.jpg", "8.jpg", "1.jpg"]

for i, url in enumerate(photos):
    if i % 2 == 0:
        with col1:
            if os.path.exists(url): st.image(url, use_container_width=True)
    else:
        with col2:
            if os.path.exists(url): st.image(url, use_container_width=True)

# 6. ALT BİLGİ
st.markdown("<br><br><br><p style='text-align: center; color: #008b8b; font-size: 20px; letter-spacing: 5px;'>Bu site Utku Çimen tarafından yapılmıştır.</p>", unsafe_allow_html=True)
