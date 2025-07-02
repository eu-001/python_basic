import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

gdp = [
    15000, 23000, 32000, 40000, 50000,
    12000, 45000, 38000, 28000, 55000
]

unemployment = [
    4.5, 6.0, 3.2, 8.0, 5.5,
    10.0, 4.0, 7.2, 9.0, 2.5
]

consumption = [
    0.5 * gdp[i] - 2000 * unemployment[i] + 50000 + np.random.normal(0,3000)
    for i in range(len(gdp))
]

X = np.column_stack((gdp, unemployment))
y = np.array(consumption)

model = LinearRegression()
model.fit(X, y)

gdp1 = 1000
unem1 = 4
x_input = np.array([[gdp1, unem1]]) #내가 틀린 부분
predicted = model.predict(x_input)[0]
print(f"gdp지수가 {gdp1}이고 실업률이 {unem1}일때 소비지출은 {predicted:.2f}입니다.")

#ㅈㄴ 간단 버전 - 머신 러닝 없이 직접 계산
GDP = 1000
unemployment1 = 4
noise = np.random.normal(0, 3000)
consumption = 0.5 * GDP - 2000 * unemployment1 + 50000 + noise

print(f"예상 소비지출 (잡음 포함): {consumption:.2f} 원")

