"""
================================================================================
PRACTICAL 7: CLASSIFICATION (LOGISTIC REGRESSION: CHURN & PENGUINS)
================================================================================
FULL QUESTIONS:

Q1) Customer Churn Prediction using Logistic Regression:
    1. Load 'scikit-learn/churn-prediction' using datasets.load_dataset.
    2. Select predictors: tenure, MonthlyCharges.
    3. Target: Churn mapped to binary (No: 0, Yes: 1).
    4. Split into train/test sets (80/20, random_state=42, stratify=y).
    5. Fit LogisticRegression model.
    6. Evaluate: Confusion Matrix, Accuracy, Precision, Recall, F1 Score, Classification Report.
    7. Plot ROC curve and report AUC score.

Q2) Penguin Species Classification using Logistic Regression (Raw):
    1. Load 'penguins' dataset from seaborn.
    2. Filter for Adelie and Gentoo species.
    3. Features: bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g. Target: Gentoo (1) vs Adelie (0).
    4. Fit LogisticRegression(max_iter=1000) and evaluate metrics & ROC curve.

Q3) Penguin Species Classification using Pipeline with StandardScaler:
    1. Build a Pipeline([('scaler', StandardScaler()), ('model', LogisticRegression(max_iter=1000))]).
    2. Fit on training data and predict on test set.
    3. Evaluate Confusion Matrix, Performance Metrics, and plot ROC curve with AUC.
================================================================================
"""

# ------------------------------------------------------------------------------
# Q1: Customer Churn Prediction
# ------------------------------------------------------------------------------
from datasets import load_dataset
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    confusion_matrix, accuracy_score, precision_score, recall_score,
    f1_score, classification_report, roc_curve, roc_auc_score
)
import matplotlib.pyplot as plt

print("--- Q1: Customer Churn Prediction ---")
dataset = load_dataset("scikit-learn/churn-prediction")
df = dataset['train'].to_pandas()

# Selection predictors and target
x = df[["tenure", "MonthlyCharges"]]
y = df["Churn"].map({"No": 0, "Yes": 1})

# Train-test split
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42, stratify=y
)

# Fit Logistic Regression
model = LogisticRegression()
model.fit(x_train, y_train)

# Predict
y_pred = model.predict(x_test)

# Confusion Matrix
print("Confusion Matrix: ")
print(confusion_matrix(y_test, y_pred))

# Performance Metrics
print("\n Performance Metrics")
print("---------------------")
print("Accuracy: ", accuracy_score(y_test, y_pred))
print("Precision: ", precision_score(y_test, y_pred))
print("Recall: ", recall_score(y_test, y_pred))
print("F1-score: ", f1_score(y_test, y_pred))

# Complete classification report
print("\n Classification Report")
print("-----------------------")
print(classification_report(y_test, y_pred))

"""
Interpretation:
The misclassified value is 319 (sum of off-diagonal elements in confusion matrix).
"""

# Predicted probabilities for churn
y_pred_prob = model.predict_proba(x_test)[:, 1]

# ROC curve and AUC
fpr, tpr, threshold = roc_curve(y_test, y_pred_prob)
auc = roc_auc_score(y_test, y_pred_prob)
print("AUC:", auc)

# Plot ROC curve
plt.figure(figsize=(7, 5))
plt.plot(fpr, tpr, label=f"ROC curve (AUC={auc:.3f})")
plt.plot([0, 1], [0, 1], 'r--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve - Customer Churn")
plt.legend()
plt.show()

# ------------------------------------------------------------------------------
# Q2: Penguin Species Classification (Raw Logistic Regression)
# ------------------------------------------------------------------------------
import seaborn as sns

print("\n--- Q2: Penguin Classification (Raw Features) ---")
df_pen = sns.load_dataset("penguins")

# Filter for Adelie and Gentoo species, select features, and drop NaNs
df1 = df_pen[df_pen['species'].isin(['Adelie', 'Gentoo'])].copy()
features = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']
df1 = df1[features + ['species']].dropna()

# Selection predictors and target
x_pen = df1[features]
y_pen = (df1["species"] == "Gentoo").astype(int)

# Train-test split
x_train_p, x_test_p, y_train_p, y_test_p = train_test_split(
    x_pen, y_pen, test_size=0.2, random_state=42, stratify=y_pen
)

# Fit Logistic Regression
model1 = LogisticRegression(max_iter=1000)
model1.fit(x_train_p, y_train_p)

# Predict
y_pred_p = model1.predict(x_test_p)

# Confusion Matrix
print("Confusion Matrix: ")
print(confusion_matrix(y_test_p, y_pred_p))

# Performance Metrics
print("\n Performance Metrics")
print("---------------------")
print("Accuracy: ", accuracy_score(y_test_p, y_pred_p))
print("Precision: ", precision_score(y_test_p, y_pred_p))
print("Recall: ", recall_score(y_test_p, y_pred_p))
print("F1-score: ", f1_score(y_test_p, y_pred_p))

# Complete classification report
print("\n Classification Report")
print("-----------------------")
print(classification_report(y_test_p, y_pred_p))

# ROC curve and AUC
y_pred_prob_p = model1.predict_proba(x_test_p)[:, 1]
fpr_p, tpr_p, threshold_p = roc_curve(y_test_p, y_pred_prob_p)
auc_p = roc_auc_score(y_test_p, y_pred_prob_p)
print("AUC:", auc_p)

plt.figure(figsize=(7, 5))
plt.plot(fpr_p, tpr_p, label=f"ROC curve (AUC={auc_p:.3f})")
plt.plot([0, 1], [0, 1], 'r--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve - Penguin Classification (Raw)")
plt.legend()
plt.show()

# ------------------------------------------------------------------------------
# Q3: Penguin Classification with StandardScaler Pipeline
# ------------------------------------------------------------------------------
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

print("\n--- Q3: Penguin Classification (StandardScaler Pipeline) ---")
# Standardize and fit logistic regression
model2 = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression(max_iter=1000))
])
model2.fit(x_train_p, y_train_p)

# Predict
y_pred_pipe = model2.predict(x_test_p)
y_pred_prob_pipe = model2.predict_proba(x_test_p)[:, 1]

# Evaluation Metrics
print("Confusion Matrix: ")
print(confusion_matrix(y_test_p, y_pred_pipe))

print("\n Performance Metrics")
print("---------------------")
print("Accuracy: ", accuracy_score(y_test_p, y_pred_pipe))
print("Precision: ", precision_score(y_test_p, y_pred_pipe))
print("Recall: ", recall_score(y_test_p, y_pred_pipe))
print("F1-score: ", f1_score(y_test_p, y_pred_pipe))

fpr_pipe, tpr_pipe, threshold_pipe = roc_curve(y_test_p, y_pred_prob_pipe)
auc_pipe = roc_auc_score(y_test_p, y_pred_prob_pipe)
print("AUC:", auc_pipe)

plt.figure(figsize=(7, 5))
plt.plot(fpr_pipe, tpr_pipe, label=f"ROC curve (AUC={auc_pipe:.3f})")
plt.plot([0, 1], [0, 1], 'r--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve - Penguin Classification (Pipeline)")
plt.legend()
plt.show()