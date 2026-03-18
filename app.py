import streamlit as st

# Sayfa Genişliği ve Başlık Ayarı
st.set_page_config(page_title="Minimal Gallery", layout="wide")

# VSCO Havası İçin Özel CSS (Yazı tipleri ve boşluklar)
st.markdown("""
    <style>
    .main {
        background-color: #fafafa;
    }
    h1 {
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 200;
        letter-spacing: 2px;
        text-align: center;
        color: #333;
    }
    .stImage {
        border-radius: 0px; /* Keskin kenarlar daha profesyonel durur */
        transition: 0.3s;
    }
    .stImage:hover {
        opacity: 0.8; /* Üzerine gelince hafif solma efekti */
    }
    </style>
    """, unsafe_allow_html=True)

st.title("COLLECTION / 01")

# Görsel Galeri Izgarası (3 Sütun)
col1, col2, col3 = st.columns(3)

# Örnek Görseller (Buraya kendi dosya yollarını ekleyebilirsin)
with col1:
    st.image("https://images.unsplash.com/photo-1500648767791-00dcc994a43e", caption="Portre - 01")
    st.image("https://images.unsplash.com/photo-1515886657613-9f3515b0c78f", caption="Fashion - 02")

with col2:
    st.image("https://images.unsplash.com/photo-1524504388940-b1c1722653e1", caption="Urban - 03")
    st.image("https://images.unsplash.com/photo-1494790108377-be9c29b29330", caption="Studio - 04")

with col3:
    st.image("https://images.unsplash.com/photo-1506744038136-46273834b3fb", caption="Nature - 05")