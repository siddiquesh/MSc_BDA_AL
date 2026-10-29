"""
================================================================================
PRACTICAL 7: LOGISTIC REGRESSION & CLASSIFICATION
================================================================================
FULL QUESTIONS:

Question 1: (Customer Churn Prediction with Logistic Regression)
    Load the customer churn prediction dataset ('scikit-learn/churn-prediction').
    1. Use 'tenure' and 'MonthlyCharges' as predictors to predict binary 'Churn' (No=0, Yes=1).
    2. Split data into training (80%) and testing (20%) sets using stratified sampling.
    3. Fit a Logistic Regression model on the training set.
    4. Predict on the test set and evaluate using:
       - Confusion Matrix
       - Accuracy, Precision, Recall, F1-Score
       - Classification Report
    5. Compute predicted probabilities, generate the ROC curve, and calculate the AUC score.

Question 2: (Binary Classification Pipeline on Palmer Penguins)
    Load the Palmer Penguins dataset and filter for species 'Adelie' and 'Gentoo'.
    1. Use four features: bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g.
    2. Encode target species: Adelie=0, Gentoo=1.
    3. Build a Machine Learning Pipeline consisting of:
       - StandardScaler()
       - LogisticRegression(max_iter=1000)
    4. Train on 80% train split and evaluate on 20% test split.
    5. Output Confusion Matrix, Accuracy, Precision, Recall, F1-Score,
       Classification Report, and ROC Curve with AUC score.
================================================================================
"""

from datasets import load_dataset
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

# Load dataset
dataset = load_dataset("scikit-learn/churn-prediction")
df = dataset["train"].to_pandas()

# Select predictors and target
X = df[["tenure", "MonthlyCharges"]]
y = df["Churn"].map({"No": 0, "Yes": 1})

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state = 42,
    stratify = y
)

# Fit logistic regression
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Confusion Matrix
print("Confusion Matix:")
print(confusion_matrix(y_test,y_pred))

# Performance metrics
print("\nPerfomance Metrics")
print("---------------------")
print("Accuracy:", accuracy_score(y_test,y_pred))
print("Precision:", precision_score(y_test,y_pred))
print("Recall:", recall_score(y_test,y_pred))
print("F1-score:", f1_score(y_test,y_pred))

# Complete classification report
print("\nClassification Report:")
print(classification_report(y_test,y_pred))

from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt

# Predicted probabilities for churn
y_prob = model.predict_proba(X_test)[:,1]

# ROC curve
fpr, tpr, thresholds = roc_curve(y_test, y_prob)

# AUC
auc = roc_auc_score(y_test, y_prob)
print("AUC:", auc)

# Plot ROC curve
plt.plot(fpr, tpr, label=f"ROC curve (AUC = {auc:.3f})")
plt.plot([0, 1], [0,1], linestyle="--")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve - Customer Churn")
plt.legend()
plt.show()

# Question 2: Palmer Penguins Dataset (Adelie vs Gentoo)
import seaborn as sns
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

# Load dataset
dataset = sns.load_dataset("penguins")
df = dataset.copy()
df = dataset[dataset["species"].isin(["Adelie", "Gentoo"])].copy()

features = [
    "bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"
]

df = df[features + ["species"]].dropna()

X = df[features]
y = (df["species"] == "Gentoo").astype(int)

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size = 0.2,
    random_state=42,
    stratify=y
)

# Standardize and fit logistic regression
model = Pipeline([
    ("scaler", StandardScaler()),
    ("logistic", LogisticRegression(max_iter=1000))
])

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

# Confusion matrix
print(f"Confusion Matrix: \n{confusion_matrix(y_test, y_pred)}")

# Performance metrics
print(f"\nPerformance Metrics: \nAccuracy: {accuracy_score(y_test, y_pred)}")
print(f"Precision: {precision_score(y_test, y_pred)}")
print(f"Recall: {recall_score(y_test, y_pred)}")
print(f"F1 Score: {f1_score(y_test, y_pred)}")

# Classification report
print(f"\nClassification Report: \n{classification_report(y_test, y_pred)}\n")
print(f"\nInterpretation: \nThus, the model is correct 100% of times.")

# ROC curve
fpr, tpr, thresholds = roc_curve(y_test, y_prob)

# AUC
auc = roc_auc_score(y_test, y_prob)
print("AUC: ", auc)

# Plot ROC curve
plt.plot(fpr, tpr, label=f"ROC Curve (AUC = {auc: .3f})")
plt.plot([0, 1], [0, 1], linestyle="--")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve - Adelie/Gentoo")
plt.legend()
plt.show()