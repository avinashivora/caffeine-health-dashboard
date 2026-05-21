import pandas as pd
import numpy as np

# Load the dataset
file_path = "synthetic_coffee_health_10000.csv"
df = pd.read_csv(file_path)

np.random.seed(42)

# --- Rename correctly ---
if "Caffeine_mg" in df.columns:
    df.rename(columns={"Caffeine_mg": "Coffee_Caffeine_mg"}, inplace=True)

# --- Derived Columns (Logical Additions) ---

# 1️⃣ Screen_Time_Hours (hours/day)
occupation_screen_factor = {
    "Student": 1.2,
    "Office": 0.8,
    "Service": 0.3,
    "Healthcare": 0.2,
    "Other": 0.5
}
df["Screen_Time_Hours"] = np.clip(
    np.random.normal(
        6 + df["Age"].apply(lambda x: -0.05 * (x - 30))
        + df["Occupation"].map(occupation_screen_factor).fillna(0),
        1.2
    ),
    1, 12
).round(1)

# 2️⃣ Work_Hours_Per_Week
occupation_hours = {
    "Office": 42, "Healthcare": 45, "Service": 48, "Student": 30, "Other": 35
}
df["Work_Hours_Per_Week"] = (
    df["Occupation"].map(occupation_hours).fillna(40)
    + np.random.randint(-5, 10, len(df))
).clip(20, 70).round(1)

# 3️⃣ Tea_Intake (cups/day)
df["Tea_Intake"] = np.clip(5 - df["Coffee_Intake"] + np.random.normal(0, 1, len(df)), 0, 5).round(1)

# 4️⃣ Tea_Caffeine_mg
df["Tea_Caffeine_mg"] = (df["Tea_Intake"] * np.random.normal(47, 5, len(df))).round(1)

# 5️⃣ Energy Drink Intake (cans/day)
stress_factor = df["Stress_Level"].map({"Low": 0.2, "Medium": 0.6, "High": 1}).fillna(0.2)
df["EnergyDrink_Intake"] = np.clip(np.random.normal(0.3, 0.3, len(df)) + stress_factor, 0, 3).round(1)

# 6️⃣ Energy Drink Caffeine
df["Energy_Caffeine_mg"] = (df["EnergyDrink_Intake"] * np.random.normal(80, 10, len(df))).round(1)

# 7️⃣ Sugar_mg (Energy Drinks)
df["Sugar_mg"] = (df["EnergyDrink_Intake"] * np.random.normal(27000, 3000, len(df))).round(1)

# 8️⃣ Mood (from Sleep Quality + Stress)
def derive_mood(row):
    if row["Sleep_Quality"] in ["Good", "Excellent"] and row["Stress_Level"] == "Low":
        return "Positive"
    elif row["Sleep_Quality"] == "Fair" or row["Stress_Level"] == "Medium":
        return "Neutral"
    else:
        return "Negative"

df["Mood"] = df.apply(derive_mood, axis=1)

# 9️⃣ Hydration_Quantity
df["Hydration_Quantity"] = (
    2.5
    + 0.1 * df["Physical_Activity_Hours"].fillna(0)
    - 0.001 * (
        df["Coffee_Caffeine_mg"].fillna(0)
        + df["Tea_Caffeine_mg"].fillna(0)
        + df["Energy_Caffeine_mg"].fillna(0)
    )
    - 0.01 * (df["Work_Hours_Per_Week"] - 40)
    + np.random.normal(0, 0.4, len(df))
)
df["Hydration_Quantity"] = df["Hydration_Quantity"].clip(0.8, 5).round(1)

# ✅ Save the cleaned base dataset (Power BI ready)
df.to_csv("enhanced_coffee_health_base.csv", index=False)

print("✅ Clean Power BI-ready dataset saved as enhanced_coffee_health_base.csv")
print("Columns included:")
print("\n".join(df.columns))
