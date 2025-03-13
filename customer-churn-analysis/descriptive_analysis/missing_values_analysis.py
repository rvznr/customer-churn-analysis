import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "/Users/ravzanursisik/Desktop/ravza/project/customer-churn-analysis/customer-churn-analysis/data_preprocessing/17.csv"

data = pd.read_csv(file_path)

save_dir = "categorical_analysis/visualizations"
os.makedirs(save_dir, exist_ok=True)

plt.figure(figsize=(12, 8))
sns.heatmap(data.isnull(), cbar=False, cmap="viridis")
plt.title("Missing Values Heatmap")

save_path = f"{save_dir}/missing_values_heatmap.png"
plt.savefig(save_path)
plt.show()

print(f"✅ Saved heatmap: {save_path}")