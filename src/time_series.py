import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

def time_series_forecast(file_path="data/sample_projects.csv"):
    """Predicting future project durations using ARIMA."""
    
    df = pd.read_csv(file_path)
    
    df["Start Date"] = pd.to_datetime(df["Start Date"], errors="coerce")
    df.set_index("Start Date", inplace=True)

    model = ARIMA(df["Actual Duration (days)"], order=(2,1,2))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=6)

    plt.plot(df.index, df["Actual Duration (days)"], label="Actual Durations")
    plt.plot(pd.date_range(start=df.index[-1], periods=7, freq='M')[1:], forecast, linestyle='dashed', label="Predicted")
    plt.xlabel("Date")
    plt.ylabel("Project Duration (days)")
    plt.legend()
    plt.title("Project Duration Forecasting")
    plt.show()

if __name__ == "__main__":
    time_series_forecast()