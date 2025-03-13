import os
import pandas as pd
import matplotlib.pyplot as plt

file_path = "/Users/ravzanursisik/Desktop/ravza/project/customer-churn-analysis/customer-churn-analysis/data_preprocessing/17.csv"
data = pd.read_csv(file_path)

categorical_columns = data.select_dtypes(include=['object', 'category']).columns

save_dir = "categorical_analysis/visualizations/categorical_distributions"
os.makedirs(save_dir, exist_ok=True)

for column in categorical_columns:
    print(f"\nValue counts for {column}:")
    print(data[column].value_counts())

    plt.figure(figsize=(8, 5))
    data[column].value_counts().plot(kind='bar', color='teal', alpha=0.8)
    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    save_path = f"{save_dir}/{column}_distribution.png"
    plt.savefig(save_path)
    plt.show()

    print(f"✅ Saved plot: {save_path}")
    