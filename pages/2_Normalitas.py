import streamlit as st
col1, col2 = st.columns([10, 1])
with col2:
   st.markdown=st.page_link("Home.py", label=":red[Home]", icon="🏠")

# Fungsi perhitungan normalitas
def perhitungan_normalitas(g, be, v):
    normalitas = g / (be * v)
    return round(normalitas, 4)  # Menggunakan fungsi round() untuk membatasi ke 4 angka di belakang koma

# Fungsi perhitungan bobot dari normalitas
def perhitungan_bobot(n, be, v):
    bobot = n * be * v
    return round(bobot, 4)  # Menggunakan fungsi round() untuk membatasi ke 4 angka di belakang koma

# Fungsi perhitungan volume dari normalitas
def perhitungan_volume(n, be, g):
    volume = g / (n * be)
    return round(volume, 4)  # Menggunakan fungsi round() untuk membatasi ke 4 angka di belakang koma

# Fungsi semua perhitungan
def main():
    st.title(':red[Perhitungan Normalitas]')
    st.write('Rumus perhitungan Normalitas: ')
    st.latex(r'''
    \text{Normalitas (N)} = \frac{\text{Bobot (g)}}{\text{Berat Ekivalen (BE)} \times \text{Volume (L)}}
    ''')
    st.write('Rumus perhitungan bobot (g) dari Normalitas: ')
    st.latex(r'''
    \text{Bobot (g)} = \text{Normalitas (N)} \times \text{Berat Ekivalen (BE)} \times \text{Volume (L)}
    ''')
    st.write('Rumus perhitungan volume (L) dari Normalitas: ')
    st.latex(r'''
    \text{Volume (L)} = \frac{\text{Bobot (g)}}{\text{Normalitas (N)} \times \text{Berat Ekivalen (BE)}}
    ''')
    
    opsi = ('Normalitas', 'Bobot dari Normalitas', 'Volume dari Normalitas')
    option = st.selectbox('Pilih opsi:', opsi)
    
    if option == 'Normalitas':
         g = st.number_input('Masukkan Jumlah Gram Zat Terlarut (g)', step=1e-6, format='%.4f')
         be = st.number_input('Masukkan Berat Ekivalen (BE)', min_value=0.0)
         v = st.number_input('Masukkan Volume Larutan (L)', min_value=0.0, format='%.3f')
         
         if st.button('Hitung Normalitas'):
             hasil_normalitas = perhitungan_normalitas(g, be, v)
             st.success(f"Hasil normalitas yang diperoleh: {hasil_normalitas} N")
            
    elif option == 'Bobot dari Normalitas':
        be = st.number_input('Masukkan Berat Ekivalen (BE)', min_value=0.0)
        v = st.number_input('Masukkan Volume Larutan (L)', min_value=0.0, format='%.3f')
        n = st.number_input('Masukkan Normalitas Larutan (N)', step=1e-6, format='%.4f')
        
        if st.button('Hitung Bobot'):
            hasil_bobot = perhitungan_bobot(n, be, v)
            st.success(f"Hasil bobot yang diperoleh: {hasil_bobot} g")
      
    elif option == 'Volume dari Normalitas':
        g = st.number_input('Masukkan Jumlah Gram Zat Terlarut (g)', step=1e-6, format='%.4f')
        be = st.number_input('Masukkan Berat Ekivalen (BE)', min_value=0.0)
        n = st.number_input('Masukkan Normalitas Larutan (N)', step=1e-6, format='%.4f')
        
        if st.button('Hitung Volume'):
            hasil_volume = perhitungan_volume(n, be, g)
            st.success(f"Hasil volume yang diperoleh: {hasil_volume} L")
            
if __name__ == '__main__':
    main()
