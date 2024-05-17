import streamlit as st
col1, col2 = st.columns([10, 1])
with col2:
   st.markdown=st.page_link("Home.py", label=":red[Home]", icon="🏠")

# Fungsi perhitungan Molaritas
def perhitungan_molaritas(g, bm, v):
    molaritas = g / (bm * v)
    return molaritas

# Fungsi perhitungan bobot dari Molaritas
def perhitungan_bobot(m, bm, v):
    bobot = m * bm * v
    return bobot

# Fungsi perhitungan volume dari Molaritas
def perhitungan_volume(m, bm, g):
    volume = g / (m * bm)
    return volume

# Fungsi semua perhitungan
def main():
    st.title(':green[Perhitungan Molaritas]')
    st.write('Rumus perhitungan Molaritas: ')
    st.latex(r'''
    \text{Molaritas (M)} = \frac{\text{Bobot (g)}}{\text{Berat Molekul (BM)} \times \text{Volume (L)}}
    ''')
    st.write('Rumus perhitungan bobot (g) dari Molaritas: ')
    st.latex(r'''
    \text{Bobot (g)} = \text{Molaritas (M)} \times \text{Berat Molaritas (BM)} \times \text{Volume (L)}
    ''')
    st.write('Rumus perhitungan volume (L) dari Molaritas: ')
    st.latex(r'''
    \text{Volume (L)} = \frac{\text{Bobot (g)}}{\text{Molaritas (M)} \times \text{Berat Molaritas (BM)}}
    ''')
    opsi = ('Molaritas', 'Bobot dari Molaritas', 'Volume dari Molaritas')
    option = st.selectbox('Pilih opsi:', opsi)
    
    if option == 'Molaritas':
         g = st.number_input('Masukkan Jumlah Gram Zat Terlarut (g)', step=1e-6, format='%.4f')
         bm = st.number_input('Masukkan Berat Molekul (BM)', min_value=0.0)
         v = st.number_input('Masukkan Volume Larutan (L)', min_value=0.0, format='%.3f')
         
         if st.button('Hitung Normalitas'):
             hasil_molaritas = perhitungan_molaritas(g, bm, v)
             st.success(f"Hasil molaritas yang diperoleh: {hasil_molaritas} N")
            
    elif option == 'Bobot dari Molaritas':
        bm = st.number_input('Masukkan Berat Molekul (BM)', min_value=0.0)
        v = st.number_input('Masukkan Volume Larutan (L)', min_value=0.0, format='%.3f')
        m = st.number_input('Masukkan Molaritas Larutan (M)', step=1e-6, format='%.4f')
        
        if st.button('Hitung Bobot'):
            hasil_bobot = perhitungan_bobot(m, bm, v)
            st.success(f"Hasil bobot yang diperoleh: {hasil_bobot} g")
      
    elif option == 'Volume dari Molaritas':
        g = st.number_input('Masukkan Jumlah Gram Zat Terlarut (g)', step=1e-6, format='%.4f')
        bm = st.number_input('Masukkan Berat Molekul (BM)', min_value=0.0)
        m = st.number_input('Masukkan Molaritas Larutan (M)', step=1e-6, format='%.4f')
        
        if st.button('Hitung Volume'):
            hasil_volume = perhitungan_volume(m, bm, g)
            st.success(f"Hasil volume yang diperoleh: {hasil_volume} L")
            
if __name__ == '__main__':
    main()