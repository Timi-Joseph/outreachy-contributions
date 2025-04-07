import pandas as pd
import numpy as np

from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    roc_curve,
    confusion_matrix,
)

import matplotlib.pyplot as plt
import seaborn as sns

DATASET_NAME = "dili"

data = pd.read_csv(f"./data/{DATASET_NAME}/{DATASET_NAME}_ccsign_features.csv")
X = data.drop(columns=["SMILES", "Label"])
y = data["Label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Training

xgb = XGBClassifier(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=5,
    random_state=42,
    scale_pos_weight=0.82,
)
xgb.fit(X_train, y_train)


y_pred = xgb.predict(X_test)
y_prob = xgb.predict_proba(X_test)[:, 1]


accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")


# ROC - AUC
fpr, tpr, _ = roc_curve(y_test, y_prob)
plt.figure()
plt.plot(
    fpr, tpr, label=f"ROC Curve (AUC = {np.trapz(tpr, fpr):.2f})"
)  #  trapezoid(tpr, fpr)
plt.plot([0, 1], [0, 1], "k--")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve - hERG XGBoost")
plt.legend()
plt.savefig(f"./figures/{DATASET_NAME}/{DATASET_NAME}_xgb_roc_curve.png")
plt.close()


# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure()
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False)
plt.xlabel("Predicted")
plt.ylabel("True")
plt.title("Confusion Matrix - hERG XGBoost")
plt.savefig(f"./figures/{DATASET_NAME}/{DATASET_NAME}_xgb_confusion_matrix.png")
plt.close()
