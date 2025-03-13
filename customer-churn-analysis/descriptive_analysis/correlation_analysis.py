import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
file_path = "/Users/ravzanursisik/Desktop/ravza/project/customer-churn-analysis/customer-churn-analysis/data_preprocessing/17.csv"
data = pd.read_csv(file_path)

correlation_matrix = data.corr()

save_dir = "categorical_analysis/visualizations"
os.makedirs(save_dir, exist_ok=True)

plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
plt.title("Correlation Matrix Heatmap")

save_path = f"{save_dir}/correlation_heatmap.png"
plt.savefig(save_path)
plt.show()

print(f"✅ Saved heatmap: {save_path}")