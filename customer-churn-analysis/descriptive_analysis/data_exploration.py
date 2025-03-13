import pandas as pd

file_path = "/Users/ravzanursisik/Desktop/ravza/project/customer-churn-analysis/customer-churn-analysis/data_preprocessing/17.csv"
data = pd.read_csv(file_path)

print(data.head())
print(f"The dataset has {data.shape[0]} rows and {data.shape[1]} columns.\n")

print("Column names and data types:")
print(data.dtypes)
print("\n")

print("Summary statistics for numerical columns:")
print(data.describe())

print("Missing values in each column:")
print(data.isnull().sum())

missing_percentage = (data.isnull().sum() / len(data)) * 100
print("\nPercentage of missing values in each column:")
print(missing_percentage)

threshold = 30
print(f"\nColumns with more than {threshold}% missing values:")
significant_missing = missing_percentage[missing_percentage > threshold]
print(significant_missing)