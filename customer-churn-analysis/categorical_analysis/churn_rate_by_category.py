import os
import pandas as pd
import matplotlib.pyplot as plt

file_path = "/Users/ravzanursisik/Desktop/ravza/project/customer-churn-analysis/customer-churn-analysis/data_preprocessing/17.csv"

data = pd.read_csv(file_path)

categorical_columns = data.select_dtypes(include=['object', 'category']).columns

save_dir = "categorical_analysis/visualizations/churn_rate_by_categories"
os.makedirs(save_dir, exist_ok=True)

for column in categorical_columns:
    print(f"\nChurn rate by {column}:")
    churn_rate = data.groupby(column)['churn'].mean()
    print(churn_rate)

    plt.figure(figsize=(8, 5))
    churn_rate.plot(kind='bar', color='coral', alpha=0.8)
    plt.title(f"Churn Rate by {column}")
    plt.xlabel(column)
    plt.ylabel("Churn Rate")
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    save_path = f"{save_dir}/{column}_churn_rate.png"
    plt.savefig(save_path)
    plt.show()

    print(f"✅ Saved plot: {save_path}")