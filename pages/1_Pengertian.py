import streamlit as st
import requests

from streamlit_lottie import st_lottie
col1, col2 = st.columns([10, 1])
with col2:
    st.markdown=st.page_link("Home.py", label=":red[Home]", icon="🏠")
    
# Halaman utama
def judul():
    col1, col2 = st.columns([1, 10])
    with col2:
        st.title(':blue[Normalitas dan Molaritas]')
    
if __name__ == '__main__':
    judul()

# Animasi di halaman utama
lottie_url= "https://lottie.host/5be44834-2c64-4955-947c-678915e3f42c/5TwYIVz3Ru.json"

def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_json = load_lottie_url(lottie_url)
st_lottie(lottie_json, width=300, height=300, key = 'hello')


# Pembahasan Normalitas dan Molaritas
col1,col2,col3 = st.columns([1, 0.2, 1])

#Pembahasan Normalitas
with col1:
    st.title(':red[Normalitas]')
    st.write("""
    ## Apa itu Normalitas?

    :green[Normalitas] adalah ukuran yang menunjukkan konsentrasi pada berat setara dalam gram per liter larutan. Berat ekivalen itu sendiri adalah ukuran kapasitas reaktif molekul yang dilarutkan dalam larutan. Dalam suatu reaksi, tugas zat terlarut adalah menentukan normalitas suatu larutan. Normalitas juga disebut satuan konsentrasi larutan ekivalen.
    Normalitas dapat di singkat dengan huruf "N", yang merupakan salah satu
    opsi paling efektif dan berguna dalam proses laboratorium. Normalitas 
    umumnya hampir sama dengan molaritas atau M. Ketika molaritas adalah unit konsentrasi yang mewakili konsentrasi ion atau senyawa terlarut dalam suatu larutan, normalitas memiliki fungsi yang lebih lengkap, dengan 
    normalitas mewakili konsentrasi molar hanya dari komponen asam atau komponen dasar.

    Rumus untuk menghitung Normalitas adalah sebagai berikut:

    Normalitas (N) = Jumlah ekuivalen zat terlarut (mol) / Volume larutan (L) atau Bobot (g) / (Berat Ekuivalen x Volume (L))

    ## Mengapa Normalitas Penting?

    Normalitas penting dalam banyak reaksi kimia, terutama dalam reaksi titrasi di mana kita ingin mengetahui konsentrasi titran atau analit secara akurat.

    """)
    
#Pembahasan Molaritas
with col3:
    st.title(':green[Molaritas]')
    st.write("""
    ## Apa itu Molaritas?

    :red[Molaritas] dalam konsentrasi larutan dikenal dengan istilah konsentrasi molar atau molaritas dengan simbol yang dimiliki yaitu M. Molaritas digunakan untuk mendapatkan konsentrasi larutan secara kuantitatif. 
    Molaritas dinyatakan sebagai jumlah mol suatu solut dalam larutan dibagi dengan volume larutan yang ditentukan dalam liter. Molaritas juga dipengaruhi oleh volume, suhu, dan tekanan zat pelarut. Jika volume meningkat, suhu juga akan ikut meningkat sehingga molaritas larutan berkurang.

    Rumus untuk menghitung molaritas adalah sebagai berikut:

    Molaritas (M) = Jumlah mol zat terlarut (mol) / Volume larutan (L) atau bobot (g) / (Berat Molekul x Volume (L))

    ## Mengapa Molaritas Penting?

    Molaritas merupakan salah satu cara untuk mengukur konsentrasi suatu larutan. Dengan mengetahui molaritas suatu larutan, kita dapat mengetahui jumlah zat terlarut yang ada dalam larutan tersebut, yang sangat penting dalam banyak aplikasi kimia seperti dalam pembuatan larutan standar, reaksi kimia, dan analisis kuantitatif.

    """)
