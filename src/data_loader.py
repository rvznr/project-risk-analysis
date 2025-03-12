import pandas as pd

def load_data(file_path="data/sample_projects.csv"):
    """Loads and cleans project data."""
    df = pd.read_csv(file_path)
 
    df["Start Date"] = pd.to_datetime(df["Start Date"], errors="coerce")

    return df

if __name__ == "__main__":
    data = load_data()
    print(data.head())  


