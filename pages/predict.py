"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the prediction page"""

    # Başlık ekleme
    st.title("Tahmin Sayfası")

    
    st.markdown(
        """
            <p style="color:#FF4B4B; font-size:25px">
                This app uses <b>Decision Tree Classifier</b> for the Early Prediction of Diabetes.
            </p>
        """, unsafe_allow_html=True)
    
   
    # Alt başlık ekleme
    st.subheader("Select Values:")


    glucose = st.slider("Glikoz", int(df["Glucose"].min()), int(df["Glucose"].max()))
    bp = st.slider("Kan basıncı", int(df["Blood_Pressure"].min()), int(df["Blood_Pressure"].max()))
    insulin = st.slider("Insulin", int(df["Insulin"].min()), int(df["Insulin"].max()))
    bmi = st.slider("Vucut kütle endeksi", float(df["BMI"].min()), float(df["BMI"].max()))
    pedigree = st.slider("Genetik yatkınlık", float(df["Pedigree_Function"].min()), float(df["Pedigree_Function"].max()))
    age = st.slider("Yaş", int(df["Age"].min()), int(df["Age"].max()))

  
    features = [glucose, bp, insulin, bmi, pedigree, age]

    #Buton oluşturma
    if st.button("Tahmin"):
        # Tahmin skoru oluşturma
        prediction, score = predict(X, y, features)

        st.success("Başarı ile tahmin edildi")

        # Tahmin çıktıları
        if (prediction == 1):
            st.info("Kişinin ya diyabeti vardır ya da diyabete yatkınlığı vardır.")
        else:
            st.info("Diyabet hastalığı yoktur.")

        # skor yazdırma
        st.write("Modeliln doğruluk oranı", score)
