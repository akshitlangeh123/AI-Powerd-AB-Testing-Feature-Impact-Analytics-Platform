import pandas as pd
import numpy as np

np.random.seed(42)

n_users = 20000

users = pd.DataFrame({
    "user_id": range(1, n_users + 1),
    "signup_date": pd.date_range("2024-01-01", periods=n_users, freq="min"),
    "country": np.random.choice(["IN", "US", "UK"], size=n_users),
})

# Assign experiment
users["variant"] = np.random.choice(["A", "B"], size=n_users)

# Simulate conversion behavior
def simulate_conversion(row):
    base = 0.10
    
    # Variant effect
    if row["variant"] == "B":
        base += 0.025  # improvement
    
    # Country effect (adds realism)
    if row["country"] == "US":
        base += 0.02
    elif row["country"] == "IN":
        base -= 0.01

    return np.random.binomial(1, base)

users["converted"] = users.apply(simulate_conversion, axis=1)

# Save file
users.to_csv("users.csv", index=False)

print("users.csv generated!")