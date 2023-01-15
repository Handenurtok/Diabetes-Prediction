"""This is the main module to run the app"""

# gerekli kütüphaneler import edildi.
import streamlit as st

# gerekli web fonksiyonları import edildi.
from web_functions import load_data

from pages import home, data, predict, visualise

# uygulamanın konfigürasyonu .  
st.set_page_config(
    page_title = 'Early Diabetes Prediction',
    page_icon = 'random',
    layout = 'wide',
    initial_sidebar_state = 'auto'
)

# sayfa isimleri
pages = {
    "Home": home,
    "Veri Bilgisi": data,
    "Diyabet Tahmini": predict,
    "Görselleştirme": visualise,
    
}

# sidebar oluşturulması
# sidebar ismi
st.sidebar.title("Navigasyon")


page = st.sidebar.radio("Sayfalar", list(pages.keys()))

# veri setinin yüklenmesi.
df, X, y = load_data()


if page in ["Diyabet Tahmini", "Görselleştirme"]:
    pages[page].app(df, X, y)
elif (page == "Veri Bilgisi"):
    pages[page].app(df)
else:
    pages[page].app()