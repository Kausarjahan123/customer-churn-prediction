import pandas as pd
import numpy as np
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# ---------------- LOAD DATA ---------------- #
df = pd.read_csv("data.csv")

# ---------------- CLEAN DATA ---------------- #
df = df.dropna()

# ---------------- ENCODING ---------------- #
encoders = {}

for col in df.select_dtypes(include='object').columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

# ---------------- SPLIT ---------------- #
X = df.drop("Churn", axis=1)
y = df["Churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---------------- MODEL ---------------- #
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# ---------------- EVALUATION ---------------- #
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# ---------------- SAVE MODEL ---------------- #
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(X.columns, open("features.pkl", "wb"))

print("Model saved successfully!")
