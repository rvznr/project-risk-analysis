# Project Risk Analysis System  

## Overview  
This project provides a **data-driven methodology** for evaluating and predicting project completion risks. It incorporates:  

- **Monte Carlo Simulation** for probabilistic risk analysis and delay estimation.  
- **ARIMA-based forecasting models** to predict future project timelines.  
- **Budget variance analysis** to monitor financial performance and optimize resource allocation.  

---

## Features  
- **Risk Simulation** – Uses Monte Carlo methods to quantify potential project delays.  
- **Predictive Modeling** – Applies time series forecasting to estimate project completion times.  
- **Data Processing & Analysis** – Cleans, structures, and analyzes project datasets.  
- **Visual Reporting** – Generates insights through graphical representations and dashboards.  

---

## Project Structure  
Project-Risk-Analysis/
│── data/
│── src/
│   ├── data_loader.py
│   ├── monte_carlo.py
│   ├── time_series.py
│   ├── main.py
│── README.md
│── requirements.txt
---
## For Quick Start  
Run the following commands to clone and run the project:  
```sh
git clone https://github.com/rvznr/project-risk-analysis.git
cd project-risk-analysis
pip install -r requirements.txt
python src/main.py
```

## Project Data  
The project works with sample data stored in **`data/sample_projects.csv`**:

| Project Name   | Start Date  | Estimated Duration (days) | Actual Duration (days) | Budget (USD) | Used Budget (USD) |
|---------------|------------|--------------------------|----------------------|-------------|-----------------|
| Project Alpha | 2024-01-10 | 90                        | 100                  | 1,000,000   | 1,200,000       |
| Project Beta  | 2024-02-15 | 120                       | 130                  | 800,000     | 850,000         |
| Project Gamma | 2024-03-20 | 60                        | 70                   | 500,000     | 600,000         |
| Project Delta | 2024-04-05 | 45                        | 50                   | 300,000     | 350,000         |
| Project Epsilon | 2024-05-10 | 150                      | 160                  | 1,200,000   | 1,250,000      |

## Key Algorithms
 Monte Carlo Simulation
	•	Simulates project delays using random variations
	•	Helps estimate worst-case and best-case scenarios

Time Series Forecasting
	•	Uses ARIMA model to predict future project durations
	•	Helps estimate expected completion times

## Future Improvements  
- **Integrate with Trello API** for real-time project tracking.  
- **Build a Streamlit dashboard** for interactive visualization.  
- **Add budget deviation analysis** to monitor financial performance.  
