# 📊 Project Risk Analysis System  
🚀 Predicting project risks using Monte Carlo Simulation & Time Series Forecasting  

## 🔹 Overview  
This project provides a **data-driven approach** to predicting **project completion risks** by:  
✔️ Using **Monte Carlo Simulation** for risk analysis  
✔️ Applying **ARIMA-based forecasting** for project durations  
✔️ Analyzing **budget vs. actual cost** impact on project success  

---

## 🔹 Features  
✅ **Monte Carlo Simulation** – Simulates project delays  
✅ **Time Series Forecasting** – Predicts future project durations  
✅ **CSV-based Data Processing** – Uses structured project data  
✅ **Data Visualization** – Plots risk distributions and forecasts  

---

## 🔹 Project Structure  
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
## 🔹 Quick Start  
Run the following commands to clone and run the project:  
```sh
git clone https://github.com/rvznr/project-risk-analysis.git
cd project-risk-analysis
pip install -r requirements.txt
python src/main.py

🔹 Project Data

The project works with sample data stored in data/sample_projects.csv: 
Project Name	Start Date	Estimated Duration (days)	Actual Duration (days)	Budget (USD)	Used Budget (USD)
Project Alpha	2024-01-10	90	100	1,000,000	1,200,000
Project Beta	2024-02-15	120	130	800,000	850,000
Project Gamma	2024-03-20	60	70	500,000	600,000
Project Delta	2024-04-05	45	50	300,000	350,000
Project Epsilon	2024-05-10	150	160	1,200,000	1,250,000

🔹 Key Algorithms

🎲 Monte Carlo Simulation
	•	Simulates project delays using random variations
	•	Helps estimate worst-case and best-case scenarios

📈 Time Series Forecasting
	•	Uses ARIMA model to predict future project durations
	•	Helps estimate expected completion times

🔹 Future Improvements
	•	Integrate with Trello API for real-time project tracking
	•	Build a Streamlit dashboard for interactive visualization
	•	Add budget deviation analysis