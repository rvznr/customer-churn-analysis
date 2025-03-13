import pandas as pd

file_path = "/Users/ravzanursisik/Desktop/ravza/project/customer-churn-analysis/customer-churn-analysis/data_preprocessing/17.csv"
data = pd.read_csv(file_path)

categorical_columns = data.select_dtypes(include=['object', 'category']).columns

print("Categorical columns detected:", categorical_columns)
print(data.dtypes)

if len(categorical_columns) == 0:
    print("Categorical analysis was skipped as no categorical variables were detected.")