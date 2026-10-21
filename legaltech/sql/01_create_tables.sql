CREATE DATABASE IF NOT EXISTS legaltech;
USE legaltech;

DROP TABLE IF EXISTS legal_cases;
DROP TABLE IF EXISTS lawyers;
DROP TABLE IF EXISTS courts;

CREATE TABLE courts (
  court_id   VARCHAR(10) PRIMARY KEY,
  court_name VARCHAR(100),
  court_type VARCHAR(30),
  city       VARCHAR(50),
  state      VARCHAR(50)
);

CREATE TABLE lawyers (
  lawyer_id        VARCHAR(10) PRIMARY KEY,
  experience_years INT,
  team             VARCHAR(50),
  specialization   VARCHAR(50)
);

CREATE TABLE legal_cases (
  case_id             VARCHAR(10) PRIMARY KEY,
  case_type           VARCHAR(30),
  court_id            VARCHAR(10),
  department          VARCHAR(30),
  lawyer_id           VARCHAR(10),
  filing_date         DATE,
  deadline_date       DATE,
  closure_date        DATE NULL,
  case_status         VARCHAR(20),
  legal_fees_inr      DECIMAL(12,2),
  hearing_count       INT,
  priority            VARCHAR(10),
  resolution_days     INT NULL,
  is_overdue          TINYINT,
  future_closure_flag TINYINT,
  age_days            INT NULL,
  age_bucket          VARCHAR(10) NULL,
  fee_outlier_flag    TINYINT,
  filing_month        DATE,
  closure_month       DATE NULL,
  FOREIGN KEY (court_id)  REFERENCES courts(court_id),
  FOREIGN KEY (lawyer_id) REFERENCES lawyers(lawyer_id)
);