import streamlit as st 
import random 
import time

#image link
st.set_page_config(page_title="TebakAngkaByMoelmo")
st.markdown(
    """
    <meta property="og:title" content="Game tebak angka by Moelmo">
    <meta property="og:description" content="game berhadiah jika 1x percobaan berhasil">
    <meta property="og:image" content="https://i.ibb.co/7drbSN3/20240707-054444.png">
    <meta property="og:url" content="https://fitcheck.streamlit.app/">
    <meta name="twitter:card" content="summary_large_image">
    """,
    unsafe_allow_html=True
)


st.title("Game#1")
st.header("Tebak angka 1 sampai 100")

#untuk mendefinisikan variable baru di streamlit
if "angka" not in st.session_state:
    st.session_state.angka = 0
    st.session_state.angka2 = 0
    st.session_state.angka3 = 0
    st.session_state.angka4 = 0
    st.session_state.angka5 = 0 
if "attemp" not in st.session_state:
    st.session_state.attemp = 0
if "reset" not in st.session_state:
    st.session_state.reset = 0
if "benar" not in st.session_state:
    st.session_state.benar = 0
if "salah" not in st.session_state:
    st.session_state.salah = 0

#gamedimulai
def mulai():
    st.session_state.angka = random.randint(1,100)
    if st.session_state.angka < 6:
        st.session_state.awal = st.session_state.angka - 1
        st.session_state.akhir = st.session_state.angka + random.randint(1,3)
        st.session_state.angka2 = random.randint(1,5)
        st.session_state.angka3 = random.randint(1,5)
        st.session_state.angka4 = random.randint(1,5)
        st.session_state.angka5 = random.randint(1,5)
    elif st.session_state.angka < 20:
        st.session_state.awal = st.session_state.angka - random.randint(1,5)
        st.session_state.akhir = st.session_state.angka + random.randint(1,5)
        st.session_state.angka2 = random.randint(1,10)
        st.session_state.angka3 = random.randint(1,10)
        st.session_state.angka4 = random.randint(1,10)
        st.session_state.angka5 = random.randint(1,10)
    elif st.session_state.angka < 40:
        st.session_state.awal = st.session_state.angka - random.randint(1,10)
        st.session_state.akhir = st.session_state.angka + random.randint(1,10)
        st.session_state.angka3 = random.randint(1,15)
        st.session_state.angka4 = random.randint(1,15)
        st.session_state.angka5 = random.randint(1,15)
        st.session_state.angka2 = random.randint(1,15)
    else:
        st.session_state.awal = st.session_state.angka - random.randint(1,15)
        st.session_state.akhir = st.session_state.angka + random.randint(1,15)
        st.session_state.angka2 = random.randint(1,20)
        st.session_state.angka3 = random.randint(1,20)
        st.session_state.angka4 = random.randint(1,20)
        st.session_state.angka5 = random.randint(1,20)

if st.session_state.angka == 0:
    mulai()

st.write(f"#### Tebak angka berikut")
st.write(f"#### Clue : {st.session_state.awal} hingga {st.session_state.akhir}")

angka = st.session_state.angka
pilihan = [
    angka, 
    angka-st.session_state.angka2, 
    angka-st.session_state.angka3, 
    angka+st.session_state.angka4, 
    angka+st.session_state.angka5
    ]

if "urutan" not in st.session_state:
    random.shuffle(pilihan)
    st.session_state.urutan = pilihan

#tombol pilihan

pilihan = st.session_state.urutan

cols = st.columns(5)
for i, p in enumerate(pilihan):
    if cols[i].button(str(p), key=f"pilihan_{i}"):
        if p == angka:
            st.success("Jawaban Anda Benar")
            time.sleep(1.5)
            mulai()
            st.session_state.benar += 1
            st.session_state.attemp = 0
            st.session_state.reset = 0
            del st.session_state.urutan
            if st.session_state.benar == 1 and st.session_state.attemp == st.session_state.salah:
                code = f"@Moelmo{random.randint(1000,9999)}"
                st.write(f"Selamat anda berhasil menjawab dalam 1 percobaan, code : {code}")
                st.link_button("Claim Hadiah Disini", f"https://wa.me/6285725600225?text={code}.")

                continue
            st.rerun()
        elif st.session_state.reset > 1:
            st.warning("Ganti Soal...")
            mulai()
            st.session_state.salah += 1
            st.session_state.attemp += 1
            st.session_state.reset = 0
            time.sleep(1.5)
            del st.session_state.urutan
            st.rerun()
        else:
            st.error("Jawaban Anda Salah")
            st.session_state.salah += 1
            st.session_state.reset += 1
            st.session_state.attemp += 1

st.markdown("---")

#stats

st.write(f"Percobaan Ke : {st.session_state.attemp}")
st.write(f"Menjawab Dengan Benar : {st.session_state.benar}")
st.write(f"Menjawab Dengan Salah : {st.session_state.salah}")


# COPYRIGHT

st.markdown("---")
st.markdown("""
    <div style="text-align: center; font-size: 25px; color: #555;">
        <p>Follow us on:</p>
        <a href="https://github.com" target="https://github.com/Moelmo" style="text-decoration: none;">
            <img src="https://cdn-icons-png.flaticon.com/128/5968/5968866.png" width="35" height="35" alt="GitHub" />
        </a>
        <a href="https://discord.com" target="https://discord.users/" style="text-decoration: none;">
            <img src="https://cdn-icons-png.flaticon.com/128/2111/2111370.png" width="35" height="35" alt="Discord" />
        </a>
        <a href="https://www.tiktok.com" target="https://tiktok.com/@moelmo57" style="text-decoration: none;">
            <img src="https://cdn-icons-png.flaticon.com/128/4782/4782345.png" width="35" height="35" alt="TikTok" />
        </a>
        <a href="https://www.instagram.com" target="https://instagram.com/moelmo.57" style="text-decoration: none;">
            <img src="https://cdn-icons-png.flaticon.com/128/2111/2111463.png" width="35" height="35" alt="Instagram" />
        </a>
    </div>
    """, unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 25px; color: #888;'>© Moelmo 2025</p>", unsafe_allow_html=True)
