import matplotlib.pyplot as plt
from config import CITY

def create_dashboard(current_data, forecast_df):
    plt.figure(figsize=(14, 10))
    
    # Current Weather Summary
    plt.subplot(2, 2, 1)
    current_temp = current_data['main']['temp']
    current_humidity = current_data['main']['humidity']
    current_wind = current_data['wind']['speed']
    weather_desc = current_data['weather'][0]['description']
    
    summary_text = (
        f"Weather in {CITY}:\n"
        f"Temp: {current_temp}°C\n"
        f"Humidity: {current_humidity}%\n"
        f"Wind: {current_wind} m/s\n"
        f"Conditions: {weather_desc.title()}"
    )
    plt.text(0.1, 0.5, summary_text, fontsize=12)
    plt.axis('off')
    plt.title("Current Weather", fontsize=14)
    
    # Temperature Forecast
    plt.subplot(2, 2, 2)
    forecast_df['date'] = forecast_df['datetime'].dt.date
    daily_avg = forecast_df.groupby('date')['temperature'].mean()
    plt.plot(daily_avg.index, daily_avg.values, marker='o', color='red')
    plt.title("5-Day Temperature Forecast")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', alpha=0.5)
    
    # Humidity Forecast
    plt.subplot(2, 2, 3)
    daily_humidity = forecast_df.groupby('date')['humidity'].mean()
    plt.bar(daily_humidity.index, daily_humidity.values, color='blue')
    plt.title("Average Daily Humidity")
    plt.xlabel("Date")
    plt.ylabel("Humidity (%)")
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', alpha=0.5)
    
    # Wind Speed Forecast
    plt.subplot(2, 2, 4)
    daily_wind = forecast_df.groupby('date')['wind_speed'].mean()
    plt.plot(daily_wind.index, daily_wind.values, marker='o', color='green')
    plt.title("Average Wind Speed")
    plt.xlabel("Date")
    plt.ylabel("Wind Speed (m/s)")
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', alpha=0.5)
    
    plt.tight_layout()
    plt.savefig('outputs/weather_dashboard.png')
    plt.show()