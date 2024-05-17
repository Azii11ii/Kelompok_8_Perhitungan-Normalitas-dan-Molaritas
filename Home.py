import streamlit as st 
from PIL import Image
img=Image.open("pages/Politeknik_Akademi_Kimia_Analisis_Bogor.png")


st.write("<h1 style='text-align: center;'>Kalkulator Normalitas & Molaritas</h1>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    st.write("")

with col2:
    st.image(img, width=200, use_column_width= "auto")

with col3:
    st.write("")
    
st.page_link("Home.py", label="Home", icon="🏠")
st.page_link("pages/1_Pengertian.py", label="Pengertian dan Infomasi", icon="📚")
st.page_link("pages/2_Normalitas.py", label="Noramlitas", icon="🔶")
st.page_link("pages/3_Molaritas.py", label="Molaritas", icon="🔷")
st.page_link("pages/4_Tabel_Ar.py", label="Tabel Ar", icon="📁")
st.page_link("pages/5_About_Us.py", label="About Us", icon="👥")
