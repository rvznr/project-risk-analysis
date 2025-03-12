from data_loader import load_data
from monte_carlo import monte_carlo_simulation
from time_series import time_series_forecast

if __name__ == "__main__":
    print("📊 Running Project Risk Analysis...")

    print("\n🔹 Loading Data...")
    data = load_data()
    print(data.head())

    print("\n🔹 Running Monte Carlo Simulation...")
    monte_carlo_simulation()

    print("\n🔹 Running Time Series Forecasting...")
    time_series_forecast()