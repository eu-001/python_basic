import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

df = pd.read_csv("weather.csv")

# Ensure 'date' is in datetime format and create 'day_number' column
df["date"] = pd.to_datetime(df["date"])
df["day_number"] = (df["date"] - df["date"].min()).dt.days

X = df[["day_number", "humidity", "wind"]]
y = df["temperature"]    

model = LinearRegression()
model.fit(X, y)

predict_date = pd.to_datetime("2025-04-10")
day_number = (predict_date - pd.to_datetime(df["date"].min())).days
humidity_input = 70
wind_input = 3
X_new = np.array([day_number, humidity_input, wind_input]).reshape(1, -1)
predicted_temp = model.predict(X_new)[0]

print(f"예상 기온: {predicted_temp:.2f}도")

import matplotlib.pyplot as plt

# 예측값 추가
df['predicted_temp'] = model.predict(X)

# 그래프 그리기
plt.figure(figsize=(10,5))
plt.plot(df['date'], df['temperature'], label='Actual temperature', marker='o')
plt.plot(df['date'], df['predicted_temp'], label='Predicted temperature', marker='x', linestyle='--')
plt.title('Actual temperature vs Predicted temperature')
plt.xlabel('date')
plt.ylabel('temperature(℃)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
