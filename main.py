from pathlib import Path

import pandas as pd

df = pd.read_csv(Path(__file__).parent / "customers.csv")
print("Initial Data:")

print(f"Number of customers: {df["Age"].count()}")
print("Statists: ")

churn_count = (df["Churn"] == "Yes").sum()
customers_quant = len(df)
customers_churn_percentage = churn_count/customers_quant * 100
print(f"Quantity of churn: {churn_count} ({customers_churn_percentage}%)")

print(f"Average age / churn:")
print(df.groupby("Churn")["Age"].mean().round())

#Analysis: Older people churn more often

print("Average income / churn:")
monthly_income=(df.groupby("Churn")["Income"].mean())/12
print(monthly_income.round(2))

#Analysis: People with an higher wage churn more often

cuant_of_people_per_country = df.groupby("Country").size()
cuant_of_churn_per_country = (df["Churn"] == "Yes").groupby(df["Country"]).sum()
churn_rate_per_country = cuant_of_churn_per_country/cuant_of_people_per_country * 100
churn_rate_per_country = churn_rate_per_country.sort_values(ascending=False)

print(f"Countries with higher churn rates:{churn_rate_per_country[:3].round(2)}")