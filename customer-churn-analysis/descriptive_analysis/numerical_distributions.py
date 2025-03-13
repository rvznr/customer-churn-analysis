import os
import pandas as pd
import matplotlib.pyplot as plt

file_path = "/Users/ravzanursisik/Desktop/ravza/project/customer-churn-analysis/customer-churn-analysis/data_preprocessing/17.csv"

data = pd.read_csv(file_path)

numerical_columns = data.select_dtypes(include=['float64', 'int64']).columns

save_dir = "categorical_analysis/visualizations/numerical_distributions"
os.makedirs(save_dir, exist_ok=True)

for column in numerical_columns:
    plt.figure(figsize=(8, 5))
    plt.hist(data[column].dropna(), bins=30, color='blue', alpha=0.7, edgecolor='black')
    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    save_path = f"{save_dir}/{column}_distribution.png"
    plt.savefig(save_path)
    plt.close()

    print(f"✅ Saved histogram: {save_path}")