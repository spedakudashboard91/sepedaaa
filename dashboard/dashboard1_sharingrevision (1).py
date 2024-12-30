# -*- coding: utf-8 -*-
"""Dashboard1_SharingRevision.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Rultb_euMON0G15K7aFnBjXnXgrpZRnw
"""

pip install streamlit

pip install streamlit pandas numpy seaborn matplotlib plotly

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from datetime import datetime
import streamlit as st

day_df = pd.read_csv("https://raw.githubusercontent.com/spedakudashboard91/biiike/main/data/day_dataset_bike_sharing.csv")

if 'instant' in day_df.columns:
    day_df.drop(columns=['instant'], inplace=True)
else:
    print("Column 'instant' not found in DataFrame.")

day_df.head()

day_df['dteday'] = pd.to_datetime(day_df['dteday'])
day_df.head()

day_df['weekday'] = day_df['dteday'].dt.day_name()  # Changed 'dateday' to 'dteday'
day_df['year'] = day_df['dteday'].dt.year  # Changed 'dateday' to 'dteday'

# Season column (no change needed)
day_df['season'] = day_df['season'].map({
    1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'
})

# Weathersit column (no change needed)
day_df['weathersit'] = day_df['weathersit'].map({
    1: 'Clear/Partly Cloudy',
    2: 'Misty/Cloudy',
    3: 'Light Snow/Rain',
    4: 'Severe Weather'
})

day_df.head()

# Resampling data based on month and calculating total rides
monthly_rent_df = day_df.resample(rule='M', on='dteday').agg({ # Changed 'dateday' to 'dteday'
    "casual": "sum",
    "registered": "sum",
    "cnt": "sum" # Changed 'count' to 'cnt' for total rides
})

# Change index format to month-year (Jan-20, Feb-20, etc.)
monthly_rent_df.index = monthly_rent_df.index.strftime('%b-%y')
monthly_rent_df = monthly_rent_df.reset_index()

# Rename columns
monthly_rent_df.rename(columns={
    "dteday": "yearmonth", # Changed 'dateday' to 'dteday'
    "cnt": "total_rides", # Changed 'count' to 'cnt' for total rides
    "casual": "casual_rides",
    "registered": "registered_rides"
}, inplace=True)

monthly_rent_df

import pandas as pd
import matplotlib.pyplot as plt

# Load the correct dataset for total rentals (day_dataset.csv)
day_df = pd.read_csv("https://raw.githubusercontent.com/spedakudashboard91/biiike/main/data/day_dataset_bike_sharing.csv")  # Adjust the path as necessary

# Extract the month from the 'dteday' column
day_df['month'] = pd.to_datetime(day_df['dteday']).dt.month

# Grouping bike renters (casual and registered) data by month
grouped_by_month = day_df.groupby('month')

# Calculating aggregate statistics for each month
aggregated_stats_by_month = grouped_by_month['cnt'].agg(['max', 'min', 'mean', 'sum']) # Changed 'count' to 'cnt' to match the actual column name
aggregated_stats_by_month

# Grouping bike renters (casual and registered) data by weather
grouped_by_weather = day_df.groupby('weathersit')

# Calculating aggregate statistics for each weather type
# Changed 'count' to 'cnt' to match the actual column name in the dataset
aggregated_stats_by_weather = grouped_by_weather['cnt'].agg(['max', 'min', 'mean', 'sum'])
aggregated_stats_by_weather

# Grouping bike renters (casual and registered) data by holiday
grouped_by_holiday = day_df.groupby('holiday')

# Calculating aggregate statistics for each holiday condition
# Changed 'count' to 'cnt' to match the actual column name in the dataset
aggregated_stats_by_holiday = grouped_by_holiday['cnt'].agg(['max', 'min', 'mean', 'sum'])
aggregated_stats_by_holiday

# Comparing the number of bike renters on weekdays and weekends
grouped_by_weekday = day_df.groupby('weekday')

# Calculating aggregate statistics for the number of bike renters on weekdays and weekends
# Changed 'count' to 'cnt' to match the actual column name for total rentals
aggregated_stats_by_weekday = grouped_by_weekday['cnt'].agg(['max', 'min', 'mean'])
aggregated_stats_by_weekday

# Grouping bike rental data by season
grouped_by_season = day_df.groupby('season')

# Calculating the average number of casual and registered bike rentals, as well as aggregate statistics for total bike rentals
# Changed 'count' to 'cnt' to match the actual column name for total rentals
aggregated_stats_by_season = grouped_by_season.agg({
    'casual': 'mean',
    'registered': 'mean',
    'cnt': ['max', 'min', 'mean']  # Corrected column name here
})
aggregated_stats_by_season

# Grouping data by season and calculating aggregate statistics for temperature variables (temp),
# perceived temperature (atemp),
# and humidity (hum)
aggregated_stats_by_season = day_df.groupby('season').agg({
    'temp': ['max', 'min', 'mean'],
    'atemp': ['max', 'min', 'mean'],
    'hum': ['max', 'min', 'mean']
})
aggregated_stats_by_season

import logging

# Set the logging level for Streamlit to ERROR to suppress warnings
logging.getLogger("streamlit").setLevel(logging.ERROR)

st.sidebar.header("Filter Data")
start_date = st.sidebar.date_input('Mulai dari', pd.to_datetime(day_df['dteday']).min()) # Changed 'data' to 'day_df'
end_date = st.sidebar.date_input('Sampai dengan', pd.to_datetime(day_df['dteday']).max()) # Changed 'data' to 'day_df'

day_df['dteday'] = pd.to_datetime(day_df['dteday'])
filtered_data = day_df[(day_df['dteday'] >= pd.to_datetime(start_date)) & (day_df['dteday'] <= pd.to_datetime(end_date))] # Changed 'data' to 'day_df'

st.set_page_config(page_title=" analisa Bike Sharing Dashboard", layout="wide")

st.title('🚲 Bike Sharing Dashboard')
st.markdown("Welcome to  **Bike Sharing Dashboard**! Di sini Anda bisa melihat analisis penyewaan sepeda berdasarkan berbagai faktor seperti hari kerja, hari libur, dan kondisi cuaca.")

st.markdown("""
### Insight:
- **Pertanyaan Bisnis ke 1**:Bagaimana perkembangan jumlah penyewaan sepeda dari tahun ke tahun?

- **Pertanyaan Bisnis ke 2** :Sejauh mana faktor cuaca berpengaruh terhadap tingkat penggunaan sepeda oleh pengguna?

- ** Pertanyaan Bisnis ke 3** :Apa perbedaan pola penggunaan sepeda pada hari kerja, hari libur, dan hari biasa?

- ** Pertanyaan Bisnis ke 4** :Apakah terdapat hubungan antara suhu udara dan tingkat penyewaan sepeda yang tinggi?
""")

# Membagi layar menjadi 3 kolom
col1, col2, col3 = st.columns(3)

# Menampilkan total rides di kolom pertama
with col1:
    # Use 'day_df' instead of 'main_df' to access the bike-sharing data
    total_all_rides = day_df['cnt'].sum()  # Also corrected 'count' to 'cnt'
    st.metric("Total Rides", value=total_all_rides)

# Menampilkan total casual rides di kolom kedua
with col2:
    # Use 'day_df' instead of 'main_df'
    total_casual_rides = day_df['casual'].sum()
    st.metric("Total Casual Rides", value=total_casual_rides)

# Menampilkan total registered rides di kolom ketiga
with col3:
    # Use 'day_df' instead of 'main_df'
    total_registered_rides = day_df['registered'].sum()
    st.metric("Total Registered Rides", value=total_registered_rides)

# Menampilkan pemisah horizontal
st.markdown("---")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px  # Import plotly.express

# Load the correct dataset for total rentals (day_dataset.csv)
day_df = pd.read_csv("https://raw.githubusercontent.com/spedakudashboard91/biiike/main/data/day_dataset_bike_sharing.csv")  # Adjust the path as necessary

# Extract the month from the 'dteday' column
day_df['month'] = pd.to_datetime(day_df['dteday']).dt.month

# Grouping bike renters (casual and registered) data by month
grouped_by_month = day_df.groupby('month')

# Calculating aggregate statistics for each month
aggregated_stats_by_month = grouped_by_month['cnt'].agg(['max', 'min', 'mean', 'sum']) # Changed 'count' to 'cnt' to match the actual column name


# Create a bar plot to visualize the aggregated statistics using Plotly Express
fig = px.bar(x=aggregated_stats_by_month.index, y=aggregated_stats_by_month['sum'],
             labels={'x': 'Month', 'y': 'Total Rentals'},
             title='Total Bike Rentals by Month')

# Update the layout for better visualization
fig.update_layout(xaxis_title='', yaxis_title='Total Rentals',
                  xaxis=dict(showgrid=False, showline=True, linecolor='rgb(204, 204, 204)', linewidth=2, mirror=True,
                             tickvals=aggregated_stats_by_month.index, # Set tick values to month numbers
                             ticktext=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']), # Set tick text to month names
                  yaxis=dict(showgrid=False, zeroline=False, showline=True, linecolor='rgb(204, 204, 204)', linewidth=2, mirror=True),
                  plot_bgcolor='rgba(255, 255, 255, 0)',
                  showlegend=True,
                  legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))

# Display the plot
st.plotly_chart(fig, use_container_width=True)

# Grouping bike renters (casual and registered) data by weather
grouped_by_weather = day_df.groupby('weathersit')

# Calculating aggregate statistics for each weather type
aggregated_stats_by_weather = grouped_by_weather['cnt'].agg(['max', 'min', 'mean', 'sum'])

# Create a bar plot to visualize the aggregated statistics by weather
plt.figure(figsize=(10, 6))
sns.barplot(x=aggregated_stats_by_weather.index, y=aggregated_stats_by_weather['sum'], palette='viridis')
plt.title('Total Bike Rentals by Weather Type')
plt.xlabel('Weather Situation')
plt.ylabel('Total Rentals')

# Get the actual weather descriptions from your data
weather_descriptions = day_df['weathersit'].unique()

# Set the x-axis tick labels using the actual weather descriptions
plt.xticks(aggregated_stats_by_weather.index, weather_descriptions)

plt.show()

# Plot for working day
fig1 = px.box(day_df, x='workingday', y='cnt', color='workingday', # Changed 'count' to 'cnt'
              title='Bike Rental Clusters by Working Day',
              labels={'workingday': 'Working Day', 'cnt': 'Total Rentals'}, # Changed 'count' to 'cnt'
              color_discrete_sequence=['#00FFFF', '#FF00FF', '#FFFF00', '#00FF00', '#FF0000'])
fig1.update_xaxes(title_text='Working Day')
fig1.update_yaxes(title_text='Total Rentals')

# Plot for holiday
fig2 = px.box(day_df, x='holiday', y='cnt', color='holiday', # Changed 'count' to 'cnt'
              title='Bike Rental Clusters by Holiday',
              labels={'holiday': 'Holiday', 'cnt': 'Total Rentals'}, # Changed 'count' to 'cnt' in labels
              color_discrete_sequence=['#00FFFF', '#FF00FF', '#FFFF00', '#00FF00', '#FF0000'])
fig2.update_xaxes(title_text='Holiday')
fig2.update_yaxes(title_text='Total Rentals')

# Plot for weekday
fig3 = px.box(day_df, x='weekday', y='cnt', color='weekday', # Changed 'count' to 'cnt'
              title='Bike Rental Clusters by Weekday',
              labels={'weekday': 'Weekday', 'cnt': 'Total Rentals'}, # Changed 'count' to 'cnt' in labels
              color_discrete_sequence=['#00FFFF', '#FF00FF', '#FFFF00', '#00FF00', '#FF0000'])
fig3.update_xaxes(title_text='Weekday')
fig3.update_yaxes(title_text='Total Rentals')

# Grouping data by season and calculating the total registered and casual usages
seasonal_usage = day_df.groupby('season')[['registered', 'casual']].sum().reset_index()

# Creating a bar plot
fig = px.bar(seasonal_usage, x='season', y=['registered', 'casual'],
             title='Bike Rental Counts by Season',
             labels={'season': 'Season', 'value': 'Total Rentals', 'variable': 'User Type'},
             color_discrete_sequence=["#00FF00","#0000FF"], barmode='group')

# Displaying the plot
st.plotly_chart(fig, use_container_width=True)
st.caption('Copyright (c), created by Dora Leonny Giselle')

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
#

# Commented out IPython magic to ensure Python compatibility.
# #Buat script untuk menjalankan Streamlit:
# %%writefile run_streamlit.sh
# streamlit run app.py & npx localtunnel --port 8501

#Jalankan aplikasi
# Sel untuk menjalankan Streamlit
!streamlit run app.py