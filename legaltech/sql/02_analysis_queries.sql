USE legaltech;

-- Q1: open / closed / overdue
SELECT case_status, COUNT(*) AS cases FROM legal_cases GROUP BY case_status;
SELECT SUM(is_overdue) AS overdue_cases FROM legal_cases;

-- Q2: backlog by department
SELECT department,
       COUNT(*) AS pending_cases,
       SUM(is_overdue) AS overdue_cases,
       ROUND(100*SUM(is_overdue)/COUNT(*),1) AS pct_overdue
FROM legal_cases
WHERE case_status = 'Pending'
GROUP BY department
ORDER BY pending_cases DESC;

-- Q3: average resolution days (closed)
SELECT ROUND(AVG(resolution_days),1) AS avg_resolution_days
FROM legal_cases WHERE case_status = 'Closed';

SELECT case_type, ROUND(AVG(resolution_days),1) AS avg_days, COUNT(*) AS closed_cases
FROM legal_cases WHERE case_status = 'Closed'
GROUP BY case_type ORDER BY avg_days DESC;

-- Q4: fees by case type and department
SELECT case_type, department,
       COUNT(*) AS cases,
       ROUND(SUM(legal_fees_inr)) AS total_fees,
       ROUND(AVG(legal_fees_inr)) AS avg_fee
FROM legal_cases
GROUP BY case_type, department
ORDER BY total_fees DESC;

-- Q5: monthly filings vs closures
SELECT m.month,
       COALESCE(f.filed,0)  AS filed,
       COALESCE(c.closed,0) AS closed
FROM (SELECT DISTINCT filing_month AS month FROM legal_cases
      UNION
      SELECT DISTINCT closure_month FROM legal_cases WHERE closure_month IS NOT NULL) m
LEFT JOIN (SELECT filing_month AS month, COUNT(*) filed
           FROM legal_cases GROUP BY filing_month) f ON f.month = m.month
LEFT JOIN (SELECT closure_month AS month, COUNT(*) closed
           FROM legal_cases WHERE closure_month IS NOT NULL
           GROUP BY closure_month) c ON c.month = m.month
ORDER BY m.month;

-- Bonus: lawyer workload (window function)
SELECT l.lawyer_id, l.team, l.experience_years,
       COUNT(*) AS pending_cases,
       RANK() OVER (ORDER BY COUNT(*) DESC) AS workload_rank
FROM legal_cases c JOIN lawyers l USING (lawyer_id)
WHERE c.case_status = 'Pending'
GROUP BY l.lawyer_id, l.team, l.experience_years;