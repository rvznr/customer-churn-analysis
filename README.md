# Customer Churn Analysis

This project focuses on analyzing customer churn using machine learning models. The goal is to predict whether a customer will churn based on historical data using algorithms like Logistic Regression and Random Forest.  
Churn prediction is a critical task for businesses, especially in industries like telecommunications, banking, and retail. By identifying customers who are likely to churn, companies can take proactive steps to retain them, 
such as offering personalized incentives, improving customer support, or addressing specific pain points that lead to dissatisfaction.

## Project Overview

The project involves the following steps:
1. **Data Preprocessing**: Handling missing values, encoding categorical variables, and normalizing numerical features.
2. **Model Training**: Training Logistic Regression and Random Forest models.
3. **Model Evaluation**: Evaluating the models' performance using metrics like accuracy, precision, recall, and F1-score.
4. **Saving the Best Model**: Saving the best-performing model (Random Forest) using `joblib`.

## Project Structure
customer-churn-analysis/
│
├── data_preprocessing/
│   ├── 17.csv
│   ├── cleaned_data.csv
│   ├── encode_categorical.py
│   ├── encoded_data.csv
│   ├── handle_missing_values.py
│   ├── normalize_numerical.py
│   └── scaled_data.csv
│
├── model/
│   ├── best_model_.pkl  # The saved model (with a unique timestamp)
│   ├── train_model.py
└── README.md

## Requirements

To run this project, you'll need to install the following Python packages:

- `pandas`
- `numpy`
- `scikit-learn`
- `imbalanced-learn`
- `joblib`

You can install them using `pip`:
pip install pandas numpy scikit-learn imbalanced-learn joblib

## Model Evaluation

After training, the models' performance is evaluated using the following metrics:

- **Accuracy**: Proportion of correct predictions.
- **Precision**: How many of the positive predictions were actually correct.
- **Recall**: How many of the actual positives were correctly predicted.
- **F1-score**: The harmonic mean of precision and recall.

## Next Steps

- Experiment with other machine learning models and compare their performance.
- Explore hyperparameter tuning for the Random Forest model to improve performance.
- Use the saved model (`best_model.pkl`) to make predictions on new data.
