import streamlit as st
import pandas as pd

col1, col2 = st.columns([10, 1])
with col2:
    st.markdown=st.page_link("Home.py", label=":red[Home]", icon="🏠")

# Fungsi Tabel Ar
def main():
    st.title(':blue[Tabel Atom] :red[Relatif] :green[Unsur Kimia]')
    st.write(':blue[Massa atom relatif] adalah massa suatu atom yang ditentukan dengan cara membandingkan massa atom standar. Massa atom relatif ini disimbolkan dengan (Ar) dan tidak memiliki satuan. Fungsi utama massa atom relatif adalah menentukan massa suatu atom')

# Dataframe untuk tabel unsur atom relatif
    df = pd.DataFrame({
        'Nama Unsur': ['Hidrogen', 'Helium', 'Litium', 'Berilium', 'Boron', 'Karbon', 'Nitrogen', 'Oksigen', 'Fluorin', 'Neon', 'Natrium', 'Magnesium', 'Alumunium', 'Silikon', 'Fosfor', 'Belerang', 'Klor', 'Kalium', 'Kalsium', 'Kromium', 'Mangan', 'Besi', 'Nikel', 'Tembaga', 'Seng', 'Brom', 'Perak', 'Iod', 'Barium', 'Emas', 'Raksa', 'Timbal'],
        'Simbol Unsur': ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'K', 'Ca', 'Cr', 'Mn', 'Fe', 'Ni', 'Cu', 'Zn', 'Br', 'Ag', 'I', 'Ba', 'Au', 'Hg', 'Pb'],
        'Nomor Atom Unsur': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20, 24, 25, 26, 28, 29, 30, 35, 47, 53, 56, 79, 80, 82],
        'Atom Relatif (Ar)': [1, 4, 7, 9, 11, 12, 14, 16, 19, 20, 23, 24, 27, 28, 31, 32, 35.5, 39, 40, 52, 55, 56, 59, 64, 65, 80, 108, 127, 137, 197, 201, 207]
    })

# Tampilkan tabel
    st.dataframe(df)

if __name__ == '__main__':
    main()
