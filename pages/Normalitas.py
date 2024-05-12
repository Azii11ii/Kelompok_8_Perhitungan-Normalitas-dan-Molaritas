import streamlit as st

col1, col2 = st.columns([10, 1])
with col2:
    st.markdown=st.page_link("Home.py", label=":red[Home]", icon="🏠")

# Fungsi perhitungan normalitas
def perhitungan_normalitas(g, be, v):
    normalitas = g / (be * v)
    return normalitas

# Fungsi perhiitungan bobot dari normalitas
def perhitungan_bobot(n, be, v):
    g = n * be * v
    return g

# Fungsi perhitungan volume dari normalitas
def perhitungan_volume(n, be, g):
    v = g / (n * be)
    return v

# Fungsi semua perhitungan
def main():
    st.title(':red[Perhitungan Normalitas]')
    st.write('Rumus perhitungan Normalitas: ')
    st.latex(r'''
    Bobot (g) / (Berat Ekivalen (BE) x Volume (L))
    ''')
    st.write('Rumus perhitungan bobot(g) dari Normalitas: ')
    st.latex(r'''
    Normalitas (N) x Berat Ekivalen (BE) x Volume (L)
    ''')
    st.write('Rumus perhitungan Volume dari Normalitas: ')
    st.latex(r'''
    Bobot (g) / (Berat Ekivalen (BE) x Normalitas (N))
    ''')
    st.write('Masukkan data: ')
    g = st.number_input('Masukkan Jumlah Gram Zat Terlarut (g)', step=1e-6, format='%.4f')
    be = st.number_input('Masukkan Berat Ekivalen (BE)', min_value=0.0)
    v = st.number_input('Masukkan Volume Larutan (L)', min_value=0.0, format='%.3f')
    n = st.number_input('Masukkan Normalitas Larutan (N)', step=1e-6, format='%.4f')
    
# Tombol hasil perhitungan Normalitas
    col1, col2, col3, = st.columns([1, 1, 1])
    with col1:
        if st.button('Hitung Normalitas'):
            hasil_normalitas = perhitungan_normalitas(g, be, v)
            st.success(f"Rumus perhitungan Normalitas: {hasil_normalitas} N")
    
    with col2:
        if st.button('Hitung Bobot'):
            hasil_bobot = perhitungan_bobot(n, be, v)
            st.success(f"Rumus perhitungan bobot dari Normalitas: {hasil_bobot} g")
        
    with col3:
        if st.button('Hitung Volume'):
            hasil_volume = perhitungan_volume(n, be, g)
            st.success(f"Hasil volume yang diperoleh: {hasil_volume} L")
    
if __name__ == '__main__':
    main()
