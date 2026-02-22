# model.py
# House Price Prediction - ML Project
# Author: hitanshi| Roll: 1024170327 | Batch: 2q32

import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
import numpy as np

# Load dataset
df = pd.read_csv('dataset.csv')
print("Dataset loaded successfully!")
print(f"Shape: {df.shape}")
print(df.head())

# Features and target
X = df[['area_sqft', 'bedrooms', 'bathrooms', 'age_years', 'garage', 'neighborhood_score']]
y = df['price']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- Feature Scaling ---
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
print("\nFeature scaling applied using StandardScaler.")

# --- Decision Tree Regressor (Experimental Branch) ---
model = DecisionTreeRegressor(max_depth=5, random_state=42)
model.fit(X_train_scaled, y_train)
print("Decision Tree model trained successfully.")

# Predict and evaluate
y_pred = model.predict(X_test_scaled)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\n--- Decision Tree Regressor Results ---")
print(f"Max Depth : 5")
print(f"MSE       : {mse:.2f}")
print(f"RMSE      : {np.sqrt(mse):.2f}")
print(f"R2 Score (Accuracy): {r2:.4f}")

# Feature importance
feature_names = ['area_sqft', 'bedrooms', 'bathrooms', 'age_years', 'garage', 'neighborhood_score']
importances = model.feature_importances_
print(f"\n--- Feature Importances ---")
for feat, imp in sorted(zip(feature_names, importances), key=lambda x: -x[1]):
    print(f"  {feat}: {imp:.4f}")
