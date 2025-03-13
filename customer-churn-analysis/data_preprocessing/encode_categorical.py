import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

file_path = "data_preprocessing/cleaned_data.csv"
data = pd.read_csv(file_path)

categorical_columns = data.select_dtypes(include=['object', 'category']).columns

for column in categorical_columns:
    if data[column].nunique() > 2:
        data = pd.get_dummies(data, columns=[column], drop_first=True)
    else:
        label_encoder = LabelEncoder()
        data[column] = label_encoder.fit_transform(data[column])

data.to_csv("data_preprocessing/encoded_data.csv", index=False)
print("\n✅ Data saved after encoding: data_preprocessing/encoded_data.csv")