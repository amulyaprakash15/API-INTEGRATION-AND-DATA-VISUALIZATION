from weather_api import fetch_current_weather, fetch_forecast, process_forecast
from visualization import create_dashboard

def main():
    print("Fetching weather data...")
    current_data = fetch_current_weather()
    forecast_data = fetch_forecast()
    forecast_df = process_forecast(forecast_data)
    
    print("Generating dashboard...")
    create_dashboard(current_data, forecast_df)
    print("Dashboard saved to 'outputs/weather_dashboard.png'")

if __name__ == "__main__":
    main()