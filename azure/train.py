# train.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Generate synthetic dataset
data = pd.DataFrame({
    "feature1": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    "feature2": [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
    "label":    [0, 0, 0, 1, 1, 1, 1, 1, 0, 0]
})

X = data[["feature1", "feature2"]]
y = data["label"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train simple logistic regression
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)

print(f"Training completed with accuracy: {acc:.2f}")
