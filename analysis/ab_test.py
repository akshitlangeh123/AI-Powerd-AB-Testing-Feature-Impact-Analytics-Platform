import os
import pandas as pd
from databricks import sql
from statsmodels.stats.proportion import proportions_ztest

# -------------------------------
# 🔌 CONNECT TO DATABRICKS
# -------------------------------
conn = sql.connect(
    server_hostname="dbc-6dbe4321-f3d1.cloud.databricks.com",
    http_path="/sql/1.0/warehouses/d0a173fa756955f0",
    access_token="dapia70dc060cf578c7cb84785a71d624c39"
)

# -------------------------------
# 📊 QUERY DATA
# -------------------------------
query = """
SELECT variant, user_id, converted
FROM ab_testing_catalog.silver.stg_users
"""

cursor = conn.cursor()
cursor.execute(query)

rows = cursor.fetchall()
columns = [col[0] for col in cursor.description]

df = pd.DataFrame(rows, columns=columns)

print("🔍 Rows fetched:", len(df))
print(df.head())

if df.empty:
    raise ValueError("❌ No data returned from query")

# -------------------------------
# 📈 AGGREGATION
# -------------------------------
agg = df.groupby("variant").agg(
    users=("user_id", "count"),
    conversions=("converted", "sum")
).reset_index()

agg["conversion_rate"] = agg["conversions"] / agg["users"]

# -------------------------------
# 🧪 Z-TEST (STATISTICS)
# -------------------------------
counts = agg["conversions"].values
nobs = agg["users"].values

z_stat, p_value = proportions_ztest(counts, nobs)

# -------------------------------
# 📊 LIFT CALCULATION
# -------------------------------
A_rate = agg.loc[agg["variant"] == "A", "conversion_rate"].values[0]
B_rate = agg.loc[agg["variant"] == "B", "conversion_rate"].values[0]

absolute_lift = B_rate - A_rate
relative_lift = absolute_lift / A_rate

# -------------------------------
# 🧾 OUTPUT RESULTS
# -------------------------------
print("\n=== A/B Test Results ===")
print(agg.to_string(index=False))

print("\n📊 Metrics:")
print(f"A Conversion Rate: {A_rate:.4f}")
print(f"B Conversion Rate: {B_rate:.4f}")

print("\n📈 Lift:")
print(f"Absolute Lift: {absolute_lift:.4f}")
print(f"Relative Lift: {relative_lift:.2%}")

print("\n🧪 Statistical Test:")
print(f"Z-stat: {z_stat:.4f}")
print(f"P-value: {p_value:.6f}")

if p_value < 0.05:
    print("✅ Statistically Significant (Reject H0)")
else:
    print("❌ Not Statistically Significant (Fail to Reject H0)")

# -------------------------------
# 🔚 CLOSE CONNECTION
# -------------------------------
cursor.close()
conn.close()