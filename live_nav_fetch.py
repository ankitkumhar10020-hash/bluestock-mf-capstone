import requests
import pandas as pd

schemes = {
    119551: "SBI_Bluechip",
    120503: "ICICI_Bluechip",
    118632: "Nippon_LargeCap",
    119092: "Axis_Bluechip",
    120841: "Kotak_Bluechip",
}

BASE_URL = "https://api.mfapi.in/mf/"

for code, name in schemes.items():
    print(f"fetching {name}...")
    try:
        res = requests.get(BASE_URL + str(code))
        data = res.json()
        df = pd.DataFrame(data["data"])
        df.columns = ["date", "nav"]
        df["amfi_code"] = code
        df.to_csv(f"data/raw/live_{name}.csv", index=False)
        print(f"  saved {len(df)} rows")
    except Exception as e:
        print(f"  error: {e}")

print("done!")
