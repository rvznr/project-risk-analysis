import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def monte_carlo_simulation(file_path="data/sample_projects.csv", simulations=10000):
    """Simulating project completion risk using Monte Carlo."""
    
    df = pd.read_csv(file_path)
    
    mean_duration = df["Actual Duration (days)"].mean()
    std_dev = df["Actual Duration (days)"].std()

    simulated_durations = np.random.normal(mean_duration, std_dev, simulations)

    plt.hist(simulated_durations, bins=50, color='blue', alpha=0.7)
    plt.xlabel("Project Duration (days)")
    plt.ylabel("Frequency")
    plt.title("Monte Carlo Simulation: Project Duration Distribution")
    plt.show()

if __name__ == "__main__":
    monte_carlo_simulation()