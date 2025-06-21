import sys
import os
import pickle
import pandas as pd
import numpy as np

sys.path.append("..")
from Dev.utils.SanityCheck import SanityCheck
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Import data
df = pd.read_csv("./data/data.csv")
#print(df.columns)

# Selecting columns:
cols = ['holiday','weekday', 'workingday', 'weathersit', 'temp', 'atemp', 'hum','windspeed', 'casual', 'registered', 'cnt']
df = df[cols]
print(df.head())

# Sanity Check:
print(SanityCheck(df).missing_values_summary())
print(SanityCheck(df).column_distribution_summary())
print(df.info())

# Dividing into training and test:
X = df.iloc[:,:-1]
y = df.iloc[:,1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Trianing model:
model = AdaBoostRegressor(random_state=0)
model.fit(X_train, y_train)

# Make predictions on the test set
predictions = model.predict(X_test)

# Calculate the metrics
mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, predictions)

print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"R-squared (R2 Score): {r2:.2f}")

# Save model into pickle (future artifact):
filename = 'artifact/trained_model_2.pkl'
with open(filename, 'wb') as file:
        pickle.dump(model, file)
print("model saved!")
