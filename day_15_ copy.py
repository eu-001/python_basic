
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

df=pd.read_csv("car_gasoline.csv") #내가 찾던 어떤 줄인말인지 머시기...

x=df[["weight","engine_size"]].values
y=df["fuel_efficiency"].values
print(x)

model=LinearRegression()
model.fit(x,y)

weight_input=1500
engine_input=2.0

x_input=np.array([weight_input,engine_input]).reshape(1,-1)
predicted_fuel=model.predict(x_input)[0]
print(f"예상 연비: 1리터로 {predicted_fuel}km 갈 수 있습니다")





