# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LinearRegression

from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error

import numpy as np


# Step 1: Load Dataset

data = pd.read_csv("housing_data.csv")

print("First 5 Rows:")
print(data.head())


# Step 2: Convert Location Text to Numbers

encoder = LabelEncoder()

data["Location"] = encoder.fit_transform(data["Location"])

print("\nEncoded Dataset:")
print(data.head())

# Step 3: Features and Target

X = data[["Size", "Bedrooms", "Location"]]

y = data["Price"]

# Step 4: Feature Scaling

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

# Step 5: Split Dataset

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.2,
    random_state=42
)

# Step 6: Train Model

model = LinearRegression()

model.fit(X_train, y_train)

# Step 7: Predictions

predictions = model.predict(X_test)

# Step 8: Evaluation

mae = mean_absolute_error(y_test, predictions)

rmse = np.sqrt(mean_squared_error(y_test, predictions))

print("\nMean Absolute Error:", mae)

print("\nRoot Mean Squared Error:", rmse)

# Step 9: Comparison Table

comparison = pd.DataFrame({
    "Actual Price": y_test.values,
    "Predicted Price": predictions
})

print("\nActual vs Predicted:")
print(comparison)

# Step 10: Visualization

plt.figure(figsize=(10,6))

plt.plot(y_test.values, label="Actual Prices")
plt.plot(predictions, label="Predicted Prices")

plt.title("Actual vs Predicted House Prices")

plt.xlabel("Houses")

plt.ylabel("Price")

plt.legend()

plt.show()