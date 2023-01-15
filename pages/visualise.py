"""This modules contains data about visualisation page"""


import warnings
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import plot_confusion_matrix
from sklearn import tree
import streamlit as st


from web_functions import train_model

def app(df, X, y):
    


    warnings.filterwarnings('ignore')
    st.set_option('deprecation.showPyplotGlobalUse', False)

 
    st.title("Diyabet Verilerini Görselleştir")

 
    if st.checkbox("Korelasyon ısı haritasını göster"):
        st.subheader("Korelasyon ısı haritası")

        fig = plt.figure(figsize = (10, 6))
        ax = sns.heatmap(df.iloc[:, 1:].corr(), annot = True)   
        bottom, top = ax.get_ylim()                             
        ax.set_ylim(bottom + 0.5, top - 0.5)                    
        st.pyplot(fig)

        
    if st.checkbox("Karışıklık matrisini çiz"):
        model, score = train_model(X, y)
        plt.figure(figsize = (10, 6))
        plot_confusion_matrix(model, X, y, values_format='d')
        st.pyplot()

    
