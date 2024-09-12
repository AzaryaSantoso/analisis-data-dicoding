import streamlit as st
import tren, hubungan  # Import halaman yang ada

def main():
    st.sidebar.title("Navigasi Aplikasi")
    page = st.sidebar.selectbox("Pilih Halaman", ["Grafik PM2.5 dan PM10", "Data Kualitas Udara"])

    if page == "Grafik PM2.5 dan PM10":
        tren.app()  # Menjalankan fungsi app() dari page1.py
    elif page == "Data Kualitas Udara":
        hubungan.app()  # Menjalankan fungsi app() dari page2.py

if __name__ == "__main__":
    main()
