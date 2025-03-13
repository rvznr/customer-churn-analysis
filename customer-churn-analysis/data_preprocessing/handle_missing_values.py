import pandas as pd

file_path = "data_preprocessing/17.csv"
data = pd.read_csv(file_path)

missing_values = data.isnull().sum()
missing_percentage = (missing_values / len(data)) * 100

print("Missing Values Per Column:\n", missing_values)
print("\nMissing Percentage Per Column:\n", missing_percentage)

threshold = 30
columns_to_drop = missing_percentage[missing_percentage > threshold].index
data = data.drop(columns=columns_to_drop)

print("\nDropped columns with more than 30% missing values:", list(columns_to_drop))

data = data.fillna(data.median())

data.to_csv("data_preprocessing/cleaned_data.csv", index=False)
print("\n✅ Data saved after handling missing values: data_preprocessing/cleaned_data.csv")