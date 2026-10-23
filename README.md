# LegalTech Analysis Dashboard

A comprehensive legal case management and analytics system that tracks court cases, lawyers, and case metrics with data cleaning, database integration, and visualization capabilities.

## Project Overview

This project provides end-to-end data processing and analysis for legal case management, including:
- Data cleaning and standardization
- MySQL database integration
- SQL-based analytics queries
- Power BI dashboard visualization
- Excel-based analysis reports

## Project Structure

```
legaltech/
├── data/
│   ├── raw/                    # Original CSV files
│   │   ├── courts.csv
│   │   ├── lawyers.csv
│   │   └── legal_cases.csv
│   └── clean/                  # Cleaned and processed CSV files
│       ├── courts_clean.csv
│       ├── lawyers_clean.csv
│       └── legal_cases_clean.csv
├── scripts/                    # Python data processing scripts
│   ├── clean_data.py          # Data cleaning and standardization
│   └── load_to_mysql.py       # Database loading script
├── sql/                       # SQL scripts
│   ├── 01_create_tables.sql   # Database schema creation
│   └── 02_analysis_queries.sql # Analytics queries
├── LegalTech_analysis dashboard.pbix  # Power BI dashboard
└── legaltech_analysis.xlsx    # Excel analysis report
```

## Database Schema

The project uses three main tables:

### courts
- `court_id` (PK): Court identifier
- `court_name`: Name of the court
- `court_type`: Type of court
- `city`: City location
- `state`: State location

### lawyers
- `lawyer_id` (PK): Lawyer identifier
- `experience_years`: Years of experience
- `team`: Team assignment
- `specialization`: Area of specialization

### legal_cases
- `case_id` (PK): Case identifier
- `case_type`: Type of legal case
- `court_id` (FK): Associated court
- `department`: Department handling the case
- `lawyer_id` (FK): Assigned lawyer
- `filing_date`: Date case was filed
- `deadline_date`: Case deadline
- `closure_date`: Date case was closed
- `case_status`: Current status (Pending/Closed)
- `legal_fees_inr`: Legal fees in INR
- `hearing_count`: Number of hearings
- `priority`: Case priority level
- `resolution_days`: Days to resolution
- `is_overdue`: Overdue flag
- `future_closure_flag`: Future closure indicator
- `age_days`: Case age in days
- `age_bucket`: Age categorization
- `fee_outlier_flag`: Fee outlier indicator
- `filing_month`: Month of filing
- `closure_month`: Month of closure

## Prerequisites

- Python 3.7+
- MySQL 5.7+ or 8.0+
- Required Python packages:
  - pandas
  - sqlalchemy
  - pymysql

## Installation

1. Clone or download the project

2. Install Python dependencies:
```bash
pip install pandas sqlalchemy pymysql
```

3. Set up MySQL database:
```bash
mysql -u root -p < sql/01_create_tables.sql
```

4. Update database credentials in `scripts/load_to_mysql.py`:
```python
USER = "root"
PASSWORD = "your_password"  # Update with your MySQL password
HOST = "127.0.0.1"
PORT = "3306"
DB = "legaltech"
```

## Usage

### Step 1: Clean the Data

Run the data cleaning script to process raw CSV files:
```bash
python scripts/clean_data.py
```

This will:
- Standardize column names (lowercase, underscores)
- Remove duplicates
- Convert date columns to datetime format
- Save cleaned files to `data/clean/`

### Step 2: Load Data to MySQL

Load the cleaned data into the MySQL database:
```bash
python scripts/load_to_mysql.py
```

This will:
- Read cleaned CSV files
- Format dates and handle null values
- Insert data into MySQL tables in correct order (courts, lawyers, legal_cases)

### Step 3: Run Analysis Queries

Execute analytics queries in MySQL:
```bash
mysql -u root -p legaltech < sql/02_analysis_queries.sql
```

Available analyses:
- Case status overview (open/closed/overdue)
- Backlog analysis by department
- Average resolution time by case type
- Legal fees analysis by case type and department
- Monthly filings vs closures trend
- Lawyer workload ranking

### Step 4: Visualizations

- **Power BI Dashboard**: Open `LegalTech_analysis dashboard.pbix` in Power BI Desktop
- **Excel Analysis**: Open `legaltech_analysis.xlsx` in Microsoft Excel

## Analytics Capabilities

The system provides insights into:

1. **Case Status Tracking**
   - Open vs closed cases
   - Overdue case identification
   - Case aging analysis

2. **Department Performance**
   - Pending case backlog
   - Overdue percentages by department
   - Workload distribution

3. **Resolution Metrics**
   - Average resolution time
   - Resolution time by case type
   - Closure rate trends

4. **Financial Analysis**
   - Legal fees by case type
   - Fee outlier detection
   - Revenue by department

5. **Resource Management**
   - Lawyer workload ranking
   - Team utilization
   - Experience-based assignment analysis

## Data Cleaning Process

The `clean_data.py` script performs:
- Column name standardization (lowercase, underscore-separated)
- Duplicate removal
- Date column conversion to datetime format
- Missing value handling
- Data type validation

## Database Configuration

Before running the load script, ensure:
1. MySQL server is running
2. Database `legaltech` is created (via `01_create_tables.sql`)
3. User credentials in `load_to_mysql.py` are correct
4. PyMySQL is installed (`pip install pymysql`)

## Troubleshooting

**Issue**: Database connection error
- **Solution**: Verify MySQL is running and credentials are correct in `load_to_mysql.py`

**Issue**: File not found errors
- **Solution**: Ensure raw CSV files exist in `data/raw/` directory

**Issue**: Date conversion errors
- **Solution**: Check date formats in CSV files match expected format



