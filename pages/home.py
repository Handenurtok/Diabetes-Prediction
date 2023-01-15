"""This modules contains data about home page"""

# gerekli kütüphaneyi import etme
import streamlit as st

def app():
    """This function create the home page"""
    
    # Başlık ekleme
    st.title("Diyabet Tahmini Web Uygulaması")

    
   

    # # Web uygulamanızın kısa açıklamasını ekleyin
    st.markdown(
    """<p style="font-size:20px;">
            Diyabet, vücudunuzun yiyecekleri enerjiye dönüştürme şeklini etkileyen kronik (uzun süreli) bir sağlık durumudur.
             Diyabet için henüz bir tedavi yoktur, ancak kilo vermek, sağlıklı beslenmek ve aktif olmak diyabetin etkisini azaltmada gerçekten yardımcı olabilir.
             Bu Web uygulaması, Destek Vektör makinesini kullanarak çeşitli özelliklerin değerlerini analiz ederek bir kişinin diyabet hastası olup olmadığını veya gelecekte diyabet hastası olmaya eğilimli olup olmadığını tahmin etmenize yardımcı olacaktır.
             
             Ad : Hande Nur
             Soyad : TOKPUNAR
             Numara : 22833301503
        </p>
    """, unsafe_allow_html=True)