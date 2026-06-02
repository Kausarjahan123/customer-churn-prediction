import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import pickle

# ---------------- LOAD DATA ---------------- #
df = pd.read_csv("data.csv")

# ---------------- BASIC CLEANING ---------------- #
df = df.dropna()

# ---------------- ENCODING ---------------- #
le = LabelEncoder()

for col in df.select_dtypes(include='object'):
    df[col] = le.fit_transform(df[col])

# ---------------- SPLIT DATA ---------------- #
X = df.drop("Churn", axis=1)   # make sure column name is Churn
y = df["Churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---------------- MODEL ---------------- #
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# ---------------- PREDICTION ---------------- #
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nReport:\n", classification_report(y_test, y_pred))

# ---------------- SAVE MODEL ---------------- #
pickle.dump(model, open("model.pkl", "wb"))

print("Model saved successfully!")
