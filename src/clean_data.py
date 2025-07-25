import pandas as pd
import os

RAW_DATA_PATH = "data/dirty_test_data.csv"
CLEANED_DATA_PATH = "data/cleaned_data.csv"

def clean_data():
    df = pd.read_csv(RAW_DATA_PATH)

    # Basic cleaning: drop NaNs, strip spaces, etc.
    df.dropna(inplace=True)
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    # Save cleaned file
    os.makedirs(os.path.dirname(CLEANED_DATA_PATH), exist_ok=True)
    df.to_csv(CLEANED_DATA_PATH, index=False)
    print(f"Cleaned data saved to {CLEANED_DATA_PATH}")

if __name__ == "__main__":
    clean_data()
