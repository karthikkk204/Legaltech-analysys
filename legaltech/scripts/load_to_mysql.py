import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine

# 1. Setup base directory paths
BASE_DIR = Path(__file__).resolve().parent.parent
CLEAN_DIR = BASE_DIR / "data" / "clean"

# 2. Database credentials (update PASSWORD and DB name if needed)
USER = "root"
PASSWORD = "root123"  # Replace with your actual MySQL password
HOST = "127.0.0.1"
PORT = "3306"
DB = "legaltech"            # Ensure this matches the database name created in 01_create_tables.sql

# 3. Create engine connection using PyMySQL
engine = create_engine(f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}")

def main():
    print("Reading cleaned CSV files...")
    
    # Verify cleaned files exist and load them
    courts_path = CLEAN_DIR / "courts_clean.csv"
    lawyers_path = CLEAN_DIR / "lawyers_clean.csv"
    cases_path = CLEAN_DIR / "legal_cases_clean.csv"
    
    # Fallback to non-_clean names if needed
    if not courts_path.exists():
        courts_path = CLEAN_DIR / "courts.csv"
    if not lawyers_path.exists():
        lawyers_path = CLEAN_DIR / "lawyers.csv"
    if not cases_path.exists():
        cases_path = CLEAN_DIR / "cases_clean.csv"

    courts = pd.read_csv(courts_path)
    lawyers = pd.read_csv(lawyers_path)
    cases = pd.read_csv(cases_path)

    print("Formatting dates and handling null values...")
    # Convert date columns safely to Python date objects or None for NULL in SQL
    date_cols = ["filing_date", "deadline_date", "closure_date", "filing_month", "closure_month"]
    for col in date_cols:
        if col in cases.columns:
            cases[col] = pd.to_datetime(cases[col], errors='coerce').dt.date

    # Convert NaNs to None so MySQL stores them as NULL instead of string 'nan'
    cases = cases.astype(object).where(cases.notna(), None)
    courts = courts.astype(object).where(courts.notna(), None)
    lawyers = lawyers.astype(object).where(lawyers.notna(), None)

    print("Inserting data into MySQL...")
    # Order matters: courts and lawyers first, then legal_cases
    courts.to_sql("courts", con=engine, if_exists="append", index=False)
    print("Loaded courts.")
    
    lawyers.to_sql("lawyers", con=engine, if_exists="append", index=False)
    print("Loaded lawyers.")
    
    cases.to_sql("legal_cases", con=engine, if_exists="append", index=False, chunksize=500)
    print("Loaded legal_cases.")

    print("Loaded.")

if __name__ == "__main__":
    main()