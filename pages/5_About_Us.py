import streamlit as st

col1, col2 = st.columns([10, 1])
with col2:
    st.markdown=st.page_link("Home.py", label=":red[Home]", icon="🏠")

st.header(':orange[Anggota Kelompok]', divider="grey")
st.write('website ini dibuat oleh:')
st.write(':blue[Azidan Rafa Fauzi]')
st.write(':blue[Elmi Wibi Ahmad Fauzi]')
st.write('Habib Irsandy')
st.write(':blue[Muhammad Billal As-sidiq]')
st.write(':blue[Naufal Fadhurrohman Pratama]')
st.write('')
st.write('')
st.write('_bagian dari project Praktik Logika dan Pemograman Komputer_')
st.write(':green[Dosen Penanggung Jawab]')
st.write(':green[Dewi Pujo Ningsih, M.Si]')
st.write('_Powered by Politeknik AKA BOGOR_')