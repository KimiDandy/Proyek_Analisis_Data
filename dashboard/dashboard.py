import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Memuat dataset utama dengan menggunakan st.cache_data
@st.cache_data
def load_data():
    return pd.read_csv("dashboard/allstation_data.csv")

data = load_data()

# --- Section 1: Menjawab Pertanyaan Utama ---

st.header("Analisis Polusi Udara Secara Keseluruhan")

# Pertanyaan 1: Variasi polusi udara di berbagai musim
st.subheader("1. Variasi Polusi Udara PM2.5 dan PM10 di Berbagai Musim")

season_stats = data.groupby('season')[['PM2.5', 'PM10']].mean()

fig, ax = plt.subplots()
season_stats.plot(kind='line', ax=ax, marker='o')
ax.set_ylabel("Konsentrasi Polutan (µg/m³)")
ax.set_xlabel("Musim")
st.pyplot(fig)

# Pertanyaan 2: Faktor utama yang berkontribusi terhadap tingkat polusi
st.subheader("2. Faktor Utama yang Berkontribusi Terhadap Polusi")

factors = ['TEMP', 'WSPM', 'DEWP', 'RAIN', 'PRES']
factor_corr_pm25 = data[factors].corrwith(data['PM2.5']).abs()
factor_corr_pm10 = data[factors].corrwith(data['PM10']).abs()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
ax1.pie(factor_corr_pm25 / factor_corr_pm25.sum(), labels=factors, autopct='%1.1f%%', startangle=90, wedgeprops={'width': 0.3})
ax1.set_title("Kontribusi Faktor Cuaca untuk PM2.5")
ax2.pie(factor_corr_pm10 / factor_corr_pm10.sum(), labels=factors, autopct='%1.1f%%', startangle=90, wedgeprops={'width': 0.3})
ax2.set_title("Kontribusi Faktor Cuaca untuk PM10")
st.pyplot(fig)

# Pertanyaan 3: Perbandingan kualitas udara antar kota
st.subheader("3. Perbandingan Kualitas Udara Antar Kota")

# Sidebar Filter
st.sidebar.header("Filter Data Kota")
selected_city = st.sidebar.selectbox("Pilih Kota", data['station'].unique())
selected_year = st.sidebar.slider("Pilih Tahun", int(data['year'].min()), int(data['year'].max()), (2013, 2017))

# Highlight settings for selected city
highlight_color = 'red'  # Warna untuk kota yang di-highlight
default_color = 'blue'  # Warna default

# PM2.5
city_stats_pm25 = data.groupby('station')['PM2.5'].mean().sort_values(ascending=False)
colors_pm25 = [highlight_color if city == selected_city else default_color for city in city_stats_pm25.index]

# PM10
city_stats_pm10 = data.groupby('station')['PM10'].mean().sort_values(ascending=False)
colors_pm10 = ['orange' if city == selected_city else 'gray' for city in city_stats_pm10.index]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# PM2.5 Bar Chart
city_stats_pm25.plot(kind='bar', ax=ax1, color=colors_pm25)
ax1.set_title("Perbandingan PM2.5 di Berbagai Kota")
ax1.set_ylabel("Konsentrasi PM2.5 (µg/m³)")
ax1.set_xlabel("Kota")

# PM10 Bar Chart
city_stats_pm10.plot(kind='bar', ax=ax2, color=colors_pm10)
ax2.set_title("Perbandingan PM10 di Berbagai Kota")
ax2.set_ylabel("Konsentrasi PM10 (µg/m³)")
ax2.set_xlabel("Kota")

st.pyplot(fig)

# --- Section 2: Analisis Data Berdasarkan Kota ---

st.header("Analisis Polusi Udara Berdasarkan Kota")

# Filter data sesuai input dari sidebar
filtered_data = data[(data['station'] == selected_city) & (data['year'].between(*selected_year))]

# Visualisasi: Grafik Polusi per Musim
st.subheader(f"Rata-rata PM2.5 dan PM10 di {selected_city} per Musim")
season_avg = filtered_data.groupby('season')[['PM2.5', 'PM10']].mean()

fig, ax = plt.subplots()
season_avg.plot(kind='line', ax=ax, marker='o')
ax.set_ylabel("Konsentrasi Polutan (µg/m³)")
ax.set_xlabel("Musim")
st.pyplot(fig)

# --- Donut Chart untuk Faktor Utama di Kota ---
st.subheader(f"Faktor Utama yang Mempengaruhi Polusi di {selected_city}")

factor_contrib = filtered_data[factors].corrwith(filtered_data['PM2.5']).abs()

# Memperbaiki tata letak dengan explode pada faktor utama
explode = [0.1 if val == factor_contrib.max() else 0 for val in factor_contrib]

fig, ax = plt.subplots()
ax.pie(factor_contrib, labels=factors, autopct='%1.1f%%', startangle=90, explode=explode, labeldistance=1.1, wedgeprops={'width': 0.3})
ax.set_title(f"Faktor Utama PM2.5 di {selected_city}")
st.pyplot(fig)

# --- Visualisasi RFM Analysis dengan Keterangan Tambahan ---
st.subheader(f"RFM Analysis untuk Kota {selected_city}")

# Penjelasan tambahan mengenai RFM
st.write("""
- **Recency**: Mengukur seberapa baru data polusi PM2.5 terkumpul di kota ini.
- **Frequency**: Mengukur seberapa sering konsentrasi PM2.5 melebihi ambang batas tertentu (misalnya 75 µg/m³).
- **Monetary**: Total konsentrasi polusi PM2.5 yang tercatat.
""")

# Recency, Frequency, Monetary Calculation untuk semua kota untuk perbandingan
rfm_all_cities = data.groupby('station').agg({
    'PM2.5': ['mean', 'count', 'sum']
})
rfm_all_cities.columns = ['Recency', 'Frequency', 'Monetary']

# Meng-highlight kota yang dipilih dengan warna merah
colors_rfm = ['red' if city == selected_city else 'gray' for city in rfm_all_cities.index]

# Menggunakan bar chart untuk visualisasi perbandingan RFM antar kota
fig, ax = plt.subplots(3, 1, figsize=(12, 18))

# Chart Recency
rfm_all_cities['Recency'].plot(kind='bar', ax=ax[0], color=colors_rfm)
ax[0].set_title('Perbandingan Recency di Berbagai Kota')
ax[0].set_ylabel('Recency (Rata-rata PM2.5)')

# Chart Frequency
rfm_all_cities['Frequency'].plot(kind='bar', ax=ax[1], color=colors_rfm)
ax[1].set_title('Perbandingan Frequency di Berbagai Kota')
ax[1].set_ylabel('Frequency (Jumlah Melebihi Ambang Batas)')

# Chart Monetary
rfm_all_cities['Monetary'].plot(kind='bar', ax=ax[2], color=colors_rfm)
ax[2].set_title('Perbandingan Monetary di Berbagai Kota')
ax[2].set_ylabel('Monetary (Total Konsentrasi PM2.5)')

st.pyplot(fig)
