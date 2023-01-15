"""This modules contains data about home page"""

# gerekli kütüphanelerin eklenmesi
import streamlit as st


def app(df):
    

    # Başlık ekleme
    st.title("Veri bilgisi")

    # Alt Başlık ekleme
    st.subheader("veriyi gör")

    # Verileri kontrol etme
    with st.expander("Veriyi gör"):
        st.dataframe(df)

    
    st.subheader("Sutunlar:")

    # Checkbox oluşturma.
    if st.checkbox("Özeti görüntüle"):
        st.dataframe(df.describe())

    
    col_name, col_dtype, col_data = st.columns(3)

    
    with col_name:
        if st.checkbox("Sutun İsimleri"):
            st.dataframe(df.columns)

   
    with col_dtype:
        if st.checkbox("Sutun veri tipleri"):
            dtypes = df.dtypes.apply(lambda x: x.name)
            st.dataframe(dtypes)
    
    
    with col_data: 
        if st.checkbox("Sutun Dataları"):
            col = st.selectbox("Sutun ismi", list(df.columns))
            st.dataframe(df[col])

    #Veri setinin linkini oluşturma
    st.markdown("""
                    <p style="font-size:24px">
                        <a 
                            href="https://www.kaggle.com/uciml/pima-indians-diabetes-database"
                            target=_blank
                            style="text-decoration:none;"
                        >Get Dataset
                        </a> 
                    </p>
                """, unsafe_allow_html=True
    )