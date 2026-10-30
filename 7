"""
================================================================================
PRACTICAL 7: LOGISTIC REGRESSION & CLASSIFICATION METRICS
================================================================================
FULL QUESTIONS:

Q1) Customer Churn Prediction using Logistic Regression:
    1. Load dataset 'scikit-learn/churn-prediction'.
    2. Select predictors 'tenure' and 'MonthlyCharges', target 'Churn' (No=0, Yes=1).
    3. Split into train and test sets (80-20 stratified split).
    4. Fit Logistic Regression model and predict on test set.
    5. Evaluate model with Confusion Matrix, Accuracy, Precision, Recall, F1-Score,
       and complete Classification Report.
    6. Plot ROC Curve and compute AUC score.

Q2) Penguin Species Classification using Logistic Regression:
    1. Load Palmer Penguins dataset and filter for species 'Adelie' and 'Gentoo'.
    2. Use predictors: bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g.
    3. Standardize and fit Logistic Regression within an ML Pipeline.
    4. Evaluate model with Confusion Matrix, Performance Metrics, Classification Report,
       and ROC Curve with AUC score.
================================================================================
"""

# ------------------------------------------------------------------------------
# Q1: Customer Churn Prediction
# ------------------------------------------------------------------------------
from datasets import load_dataset
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, confusion_matrix, classification_report,
    roc_curve, roc_auc_score
)
import matplotlib.pyplot as plt

# Load dataset
dataset = load_dataset("scikit-learn/churn-prediction")
df = dataset["train"].to_pandas()

# Select predictors and target
X = df[["tenure", "MonthlyCharges"]]
y = df["Churn"].map({"No": 0, "Yes": 1})

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Fit Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Confusion Matrix
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Performance Metrics
print("
Performance Metrics:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1 Score:", f1_score(y_test, y_pred))

# Classification Report
print("
Classification Report:")
print(classification_report(y_test, y_pred))

# ROC Curve and AUC
y_prob = model.predict_proba(X_test)[:, 1]
fpr, tpr, thresholds = roc_curve(y_test, y_prob)
auc = roc_auc_score(y_test, y_prob)
print("AUC:", auc)

plt.plot(fpr, tpr, label=f"ROC Curve (AUC={auc:.3f})")
plt.plot([0, 1], [0, 1], linestyle="--")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve - Customer Churn")
plt.legend()
plt.show()

# ------------------------------------------------------------------------------
# Q2: Penguin Species Classification Pipeline
# ------------------------------------------------------------------------------
import seaborn as sns
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

# Load dataset
df_peng = sns.load_dataset("penguins")

# Select Adelie and Gentoo species
df_peng = df_peng[df_peng["species"].isin(["Adelie", "Gentoo"])].copy()

# Select predictors
features = [
    "bill_length_mm", "bill_depth_mm",
    "flipper_length_mm", "body_mass_g"
]
df_peng = df_peng[features + ["species"]].dropna()
X = df_peng[features]
y = (df_peng["species"] == "Gentoo").astype(int)
print("
Dataset Shape:", df_peng.shape)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Standardize and fit Logistic Regression
modelb = Pipeline([
    ("scaler", StandardScaler()),
    ("logistic", LogisticRegression(max_iter=1000))
])
modelb.fit(X_train, y_train)

# Make predictions
y_pred = modelb.predict(X_test)

# Confusion Matrix & Performance Metrics
print("
Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("
Performance Metrics:")
print("--------------------")
print("Accuracy:", round(accuracy_score(y_test, y_pred), 4))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1 Score:", f1_score(y_test, y_pred))

print("
Classification Report:")
print(classification_report(y_test, y_pred))

# ROC Curve and AUC
y_prob = modelb.predict_proba(X_test)[:, 1]
fpr, tpr, thresholds = roc_curve(y_test, y_prob)
auc = roc_auc_score(y_test, y_prob)
print("AUC:", auc)

plt.plot(fpr, tpr, label=f"ROC Curve (AUC={auc:.3f})")
plt.plot([0, 1], [0, 1], linestyle="--")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve - Penguin Species Classification")
plt.legend()
plt.show()
