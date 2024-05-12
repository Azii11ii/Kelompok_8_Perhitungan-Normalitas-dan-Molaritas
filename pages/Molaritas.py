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
    g = m * bm * v
    return g

# Fungsi perhitungan volume dari Molaritas
def perhitungan_volume(m, bm, g):
    v = g / (m * bm)
    return v

# Fungsi semua perhitungan
def main():
    st.title(':green[Perhitungan Molaritas]')
    st.write('Rumus perhitungan Molaritas: ')
    st.latex(r'''
    Bobot (g) / (Berat Molekul (BM) x Volume (L))
    ''')
    st.write('Rumus perhitungan bobot(g) dari Molaritas: ')
    st.latex(r'''
    Molaritas (M) x Berat Molekul (BM) x Volume (L)
    ''')
    st.write('Rumus perhitungan Volume dari Molaritas: ')
    st.latex(r'''
    Bobot (g) / (Berat Molekul (BM) x Molaritas (M))
    ''')
    st.write('Masukkan data: ')
    g = st.number_input('Masukkan Jumlah Gram Zat Terlarut (g)', step=1e-6, format='%.4f')
    bm = st.number_input('Masukkan Berat Molekul (BM)', min_value=0.0)
    v = st.number_input('Masukkan Volume Larutan (L)', min_value=0.0, format='%.3f')
    m = st.number_input('Masukkan Molaritas Larutan (M)', min_value=0.0, format='%.4f')
    
# Tombol perhitungan Molaritas
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.button('Hitung Molaritas'):
            hasil_molaritas = perhitungan_molaritas(g, bm, v)
            st.success(f"Hasil Molaritas yang diperoleh: {hasil_molaritas} M")
    
    with col2:
        if st.button('Hitung Bobot'):
            hasil_bobot = perhitungan_bobot(m, bm, v)
            st.success(f"Hasil bobot yang diperoleh: {hasil_bobot} g")
    
    with col3:
        if st.button('Hitung Volume'):
            hasil_volume = perhitungan_volume(m, bm, g)
            st.success(f"Hasil volume yang diperoleh: {hasil_volume} L")
    
if __name__ == '__main__':
    main()
