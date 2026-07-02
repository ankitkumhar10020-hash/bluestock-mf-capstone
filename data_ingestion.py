import pandas as pd
import os

RAW_PATH = "data/raw/"

files = [
    "01_fund_master.csv",
    "02_nav_history.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv",
]

for f in files:
    path = os.path.join(RAW_PATH, f)
    df = pd.read_csv(path)
    print(f"\n--- {f} ---")
    print("shape  :", df.shape)
    print("nulls  :", df.isnull().sum().sum())
    print(df.head(2))

print("\nall files loaded!")
