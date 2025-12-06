# print (data.head())
# print (data.info())
# print (data.shape)
# count the null fields
# nullcount = data.isnull().sum
# print (f"Number of null rows is : {nullcount}")
# to delete the null 
# cleaned_data = data.dropna()

# duplicate_count = data.duplicated().sum()
# print (duplicate_count)  # there is no duplicates

# data.boxplot(figsize=(10,6))
# plt.title('outlier detection')
# plt.xticks(rotation=45)
# plt.show()

# Create contingency table
# table = pd.crosstab(data["Smoking_Status"], data["Has_Hypertension"])

# pi square
# table = pd.crosstab(data["Smoking_Status"], data["Has_Hypertension"])
# print(table)

# chi2, p, dof, expected = chi2_contingency(table)
# print("Chi2:", chi2)
# print("p-value:", p)
# print("Degrees of freedom:", dof)
# print("Expected values:\n", expected)


# Plot heatmap
# plt.figure(figsize=(6,4))
# sns.heatmap(table, annot=True, fmt="d", cmap="Blues")
# plt.title("Heatmap: Smoking Status vs Hypertension")
# plt.xlabel("Has Hypertension")
# plt.ylabel("Smoking Status")
# plt.show()

# barchart
# table.plot(kind="bar", figsize=(7,5))
# plt.title("Bar Chart: Smoking Status vs Hypertension")
# plt.xlabel("Smoking Status")
# plt.ylabel("Count")
# plt.xticks(rotation=0)
# plt.show()