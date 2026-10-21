import pandas as pd
from pathlib import Path

# Define paths using pathlib for cross-platform compatibility
BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"
CLEAN_DIR = BASE_DIR / "data" / "clean"

# Ensure clean directory exists
CLEAN_DIR.mkdir(parents=True, exist_ok=True)

def clean_courts():
    print("Cleaning courts.csv...")
    file_path = RAW_DIR / "courts.csv"
    if not file_path.exists():
        print(f"File not found: {file_path}")
        return
    
    df = pd.read_csv(file_path)
    # Standardize column names (lowercase, replace spaces with underscores)
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    
    # Handle missing values / drop duplicates
    df = df.drop_duplicates()
    
    output_path = CLEAN_DIR / "courts_clean.csv"
    df.to_csv(output_path, index=False)
    print(f"Saved cleaned courts to {output_path}")

def clean_lawyers():
    print("Cleaning lawyers.csv...")
    file_path = RAW_DIR / "lawyers.csv"
    if not file_path.exists():
        print(f"File not found: {file_path}")
        return
    
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    
    # Fill missing values if necessary or drop rows with missing critical IDs
    df = df.drop_duplicates()
    
    output_path = CLEAN_DIR / "lawyers_clean.csv"
    df.to_csv(output_path, index=False)
    print(f"Saved cleaned lawyers to {output_path}")

def clean_legal_cases():
    print("Cleaning legal_cases.csv...")
    file_path = RAW_DIR / "legal_cases.csv"
    if not file_path.exists():
        print(f"File not found: {file_path}")
        return
    
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    
    # Example: Convert date columns to standard datetime format if they exist
    date_columns = [col for col in df.columns if 'date' in col]
    for col in date_columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')
        
    df = df.drop_duplicates()
    
    output_path = CLEAN_DIR / "legal_cases_clean.csv"
    df.to_csv(output_path, index=False)
    print(f"Saved cleaned legal cases to {output_path}")

if __name__ == "__main__":
    clean_courts()
    clean_lawyers()
    clean_legal_cases()
    print("Data cleaning completed successfully!")