# Customer Data Analysis

Exploratory churn analysis of a small customer dataset using **Python** and **pandas**.

The goal is to find out which customer profiles are more likely to leave (churn), looking at age, income and country.

## Dataset

`customers.csv` contains 30 customers with the following columns:

| Column | Description |
|---|---|
| `CustomerID` | Unique customer identifier |
| `Country` | Spain, France, Germany or Italy |
| `Age` | Customer age |
| `Gender` | M / F |
| `Income` | Annual income |
| `Products` | Number of products owned |
| `MonthlySpend` | Average monthly spend |
| `VisitsPerMonth` | Visits per month |
| `Subscription` | Has a subscription (Yes / No) |
| `SupportTickets` | Number of support tickets opened |
| `Churn` | Whether the customer left (Yes / No) |

## What the script does

`main.py` loads the dataset and computes:

1. Total number of customers.
2. Number and percentage of customers who churned.
3. Average age of churned vs. retained customers.
4. Average monthly income (annual income / 12) of churned vs. retained customers.
5. Churn rate per country, showing the top 3.

## Results

| Metric | Value |
|---|---|
| Customers | 30 |
| Churned customers | 12 (40%) |
| Average age (churn / no churn) | 52 / 29 |
| Average monthly income (churn / no churn) | 4,638.89 / 2,490.74 |

**Churn rate by country (top 3):**

| Country | Churn rate |
|---|---|
| France | 57.14% |
| Italy | 42.86% |
| Spain | 33.33% |

### Conclusions

- Older customers churn much more often.
- Customers with higher income churn more often.
- France has the highest churn rate of the four countries.

## How to run

Requirements: Python 3.12+ and pandas.

```bash
pip install pandas
python main.py
```
