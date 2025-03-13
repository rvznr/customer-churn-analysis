import pandas as pd
from sklearn.preprocessing import StandardScaler

file_path = "data_preprocessing/encoded_data.csv"
data = pd.read_csv(file_path)

numerical_columns = data.select_dtypes(include=['int64', 'float64']).columns

if 'churn' in numerical_columns:
    numerical_columns = numerical_columns.drop("churn")

scaler = StandardScaler()
data[numerical_columns] = scaler.fit_transform(data[numerical_columns])

data['churn'] = data['churn'].astype(int)

data.to_csv("data_preprocessing/scaled_data.csv", index=False)
print("\n✅ Data saved after normalization: data_preprocessing/scaled_data.csv")