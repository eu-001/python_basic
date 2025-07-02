
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# df=pd.read_csv("car_gasoline.csv") #내가 찾던 어떤 줄인말인지 머시기...

# x=df[["weight","engine_size"]].values
# y=df["fuel_efficiency"].values
# print(x)

# model=LinearRegression()
# model.fit(x,y)

# weight_input=1500
# engine_input=2.0

# x_input=np.array([weight_input,engine_input]).reshape(1,-1)
# predicted_fuel=model.predict(x_input)[0]
# print(f"예상 연비: 1리터로 {predicted_fuel}km 갈 수 있습니다")

house_size=np.array([30, 40, 50, 60, 70, 80, 90, 100])
np.random.seed(42) 
price = house_size * 50 + np.random.randint(-200, 200, size=house_size.shape)

print("집 크기:", house_size)
print("가격:", price)

model=LinearRegression()
model.fit(house_size.reshape(-1, 1), price)

my_houze_size=33

x_input = np.array([[33]])
predicted = model.predict(x_input)[0]
print(f"내 집 가격:{predicted}")




