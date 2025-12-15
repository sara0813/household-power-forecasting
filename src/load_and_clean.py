import pandas as pd
from pathlib import Path

DATA_PATH = Path("data/raw/household_power_consumption.txt")

df = pd.read_csv(
    DATA_PATH,
    sep=";",
    na_values="?",
    low_memory=False
)

print("Raw shape:", df.shape)

df["Datetime"] = pd.to_datetime(
    df["Date"] + " " + df["Time"],
    format="%d/%m/%Y %H:%M:%S"
)
df = df.drop(columns=["Date", "Time"])
df = df.set_index("Datetime")

df = df.sort_index()
df = df.astype(float)

print("After datetime & type cast:", df.shape)
print(df.head())
print(df.isna().mean())


df = df.ffill()

out_path = Path("data/processed/power_1min.csv")
out_path.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(out_path)

print("Saved to:", out_path)


