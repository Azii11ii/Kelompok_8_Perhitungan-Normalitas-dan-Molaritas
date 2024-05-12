import streamlit as st

col1, col2 = st.columns([1, 5])

with col1:
    st.title('NORMALITAS DAN MOLARITAS')
    
    st.page_link("Home.py", label="Home", icon="🏠")
    st.page_link("pages/Halaman_Utama.py", label="Halaman Utama", icon="🟦")
    st.page_link("pages/Molaritas.py", label="Molaritas", icon="🟥")
    st.page_link("pages/Normalitas.py", label="Normalitas", icon="🟩")
    st.page_link("pages/Tabel_Ar.py", label="Tabel Ar", icon="🟧")
