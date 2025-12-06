import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# from aklearn.preprocessing import LablesEncoder
from scipy.stats import chi2_contingency
import seaborn as sns

data = pd.read_csv("hypertension_dataset.csv")
# this is chi square for :  & hypertention

# Make sure Medication has no missing values
data["Medication"] = data["Medication"].fillna("None")

# List of variables you want to test against hypertension
variables = ["Family_History", "Exercise_Level", "Medication", "Smoking_Status"]

for var in variables:
    print("=====================================================")
    print(f"🔍 Chi-Square Test: {var} vs Has_Hypertension")
    print("=====================================================")
    
    # Build contingency table
    table = pd.crosstab(data[var], data["Has_Hypertension"])
    print("\nContingency Table:")
    print(table)
    
    # Apply Chi-Square test
    chi2, p, dof, expected = chi2_contingency(table)
    
    print("\nChi2:", chi2)
    print("p-value:", p)
    print("Degrees of freedom:", dof)
    print("Expected values:\n", expected)
    
    # Interpretation
    if p < 0.05:
        print("\n➡️ Result: SIGNIFICANT association (Reject H0)\n")
    else:
        print("\n➡️ Result: NOT significant (Fail to reject H0)\n")

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Fix missing Medication values
data["Medication"] = data["Medication"].fillna("None")

# Categorical variables to combine
variables = ["Family_History", "Exercise_Level", "Medication", "Smoking_Status"]

# Build a combined contingency table
combined = pd.DataFrame()

for var in variables:
    temp = pd.crosstab(data[var], data["Has_Hypertension"])
    temp.index = [f"{var}: {i}" for i in temp.index]  # Label rows as "Variable:Category"
    combined = pd.concat([combined, temp])

# Plot heatmap with CLEAR numeric values
plt.figure(figsize=(10, 12))
sns.heatmap(
    combined,
    annot=True,      # show numbers
    fmt="d",         # integer format
    cmap="Blues",    # color scale (keeps numbers readable)
    linewidths=0.5,  # thin lines for better readability
    cbar=False       # hides color bar so NUMBERS stand out
)

plt.title("Heatmap of Counts: Categorical Variables vs Hypertension", fontsize=14)
plt.xlabel("Has Hypertension", fontsize=12)
plt.ylabel("Category", fontsize=12)
plt.tight_layout()
plt.show()







