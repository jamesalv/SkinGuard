import streamlit as st


st.set_page_config(page_title="SkinWiseAI", page_icon="🌐", layout="wide")


def main_page():
    st.title("SkinWiseAI")
    st.write(
        "Kulit Sehat, Solusi Cepat\nDapatkan diagnosis kulit instan dengan teknologi AI canggih dari Skin Wise AI!"
    )

    st.button("Get started")


def services():
    st.header("Layanan")
    st.subheader("1. Diagnosis Cepat")
    st.write("Skin Wise AI memberikan diagnosis kulit instan dengan tingkat akurasi tinggi.")

    st.subheader("2. Personalisasi Perawatan")
    st.write("Skin Wise AI menyediakan rekomendasi perawatan kulit yang personal dan disesuaikan.")

    st.subheader("3. Pemantauan Berkala")
    st.write("Layanan ini memungkinkan pengguna melakukan pemantauan berkala terhadap kondisi kulit.")


def contact():
    st.header("Kontak")
    st.write("Email: skinwiseai@gmail.com")
    st.write("Telepon: +62 123 4567")
    st.write("Alamat: Jl. RadenSari Timur No. 123, Kota Semarang, Indonesia")


def features():
    st.header("Fitur")
    option = st.selectbox("Pilih fitur:", ["Unggah Gambar", "Artikel"])

    if option == "Unggah Gambar":
        st.subheader("Unggah Gambar")
        st.write("Pilih opsi ini untuk mengunggah gambar penyakit kulit.")

    elif option == "Artikel":
        st.subheader("Artikel")
        st.write("Pilih opsi ini untuk membaca artikel terkait perawatan kulit.")


def upload_image_page():
    st.title("Unggah Gambar Penyakit Kulit")
    uploaded_file = st.file_uploader("Pilih gambar", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        st.write("File berhasil diunggah!")


def sign_in_sign_up_page():
    st.title("Sign In / Sign Up")
    option = st.radio("Pilih:", ["Sign In", "Sign Up"])

    if option == "Sign In":
        st.subheader("Sign In")
        

    elif option == "Sign Up":
        st.subheader("Sign Up")
        


page = st.sidebar.selectbox("Navigasi", ["Beranda", "Layanan", "Fitur", "Kontak", "Unggah Gambar", "Sign In/Sign Up"])

# Render the selected page
if page == "Beranda":
    main_page()
elif page == "Layanan":
    services()
elif page == "Fitur":
    features()
elif page == "Kontak":
    contact()
elif page == "Unggah Gambar":
    upload_image_page()
elif page == "Sign In/Sign Up":
    sign_in_sign_up_page()
