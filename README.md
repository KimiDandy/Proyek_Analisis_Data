
# Proyek Analisis Data Polusi Udara

## Latar Belakang

Proyek ini bertujuan untuk menganalisis tingkat polusi udara di beberapa kota besar berdasarkan data PM2.5 dan PM10. Dengan menggunakan dataset yang mencakup berbagai faktor cuaca, proyek ini menyajikan wawasan mengenai faktor-faktor yang mempengaruhi polusi udara, serta perbandingan kualitas udara antar kota. Selain itu, analisis lanjutan menggunakan teknik **RFM (Recency, Frequency, Monetary)** diterapkan untuk mengidentifikasi pola polusi dan frekuensi polusi melebihi ambang batas.

## Tujuan

Tujuan dari dashboard ini adalah:
1. Menganalisis variasi polusi udara (PM2.5 dan PM10) berdasarkan musim.
2. Mengidentifikasi faktor utama yang berkontribusi terhadap tingkat polusi.
3. Membandingkan kualitas udara antar kota berdasarkan PM2.5 dan PM10.
4. Menggunakan analisis RFM untuk mengukur polusi udara berdasarkan Recency (seberapa baru data polusi terkumpul), Frequency (seberapa sering kota melampaui ambang batas polusi), dan Monetary (total konsentrasi polusi di kota tersebut).

## Isi dari Dashboard

Dashboard ini terdiri dari beberapa bagian:
1. **Analisis Variasi Polusi Udara**: Melihat variasi polusi PM2.5 dan PM10 di berbagai musim.
2. **Faktor Kontribusi Polusi Udara**: Mengidentifikasi faktor cuaca yang paling berkontribusi terhadap tingkat polusi.
3. **Perbandingan Kualitas Udara Antar Kota**: Membandingkan tingkat polusi PM2.5 dan PM10 di berbagai kota.
4. **RFM Analysis**: Menampilkan analisis RFM untuk melihat pola polusi di setiap kota.

## Cara Menggunakan Dashboard

1. **Memilih Kota**: Gunakan sidebar untuk memilih kota yang ingin dianalisis.
2. **Memilih Rentang Tahun**: Gunakan slider di sidebar untuk menentukan rentang tahun yang ingin dianalisis.
3. **Menjelajahi Visualisasi**: Visualisasi akan muncul secara otomatis berdasarkan pilihan kota dan tahun, menampilkan grafik polusi per musim, faktor utama yang berkontribusi terhadap polusi, serta perbandingan kualitas udara antar kota.

## Cara Menjalankan Dashboard

Untuk menjalankan dashboard ini, ikuti langkah-langkah berikut:

1. Clone atau unduh repositori proyek ini ke dalam direktori lokal.
2. Pastikan Anda berada di direktori proyek. Jika menggunakan terminal, navigasikan ke folder proyek dengan perintah:
   
   ```bash
   cd Proyek_Analisis_Data
   ```

3. Jalankan dashboard dengan perintah berikut:

   ```bash
   streamlit run dashboard/dashboard.py
   ```

4. Dashboard akan terbuka di browser web Anda pada URL default `http://localhost:8501`.

5. Anda sekarang dapat berinteraksi dengan dashboard untuk menganalisis data polusi udara.
