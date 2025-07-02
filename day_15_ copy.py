import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

df=pd.read_csv("car_gasoline.csv")
print(df)

x=df[["weight","engine_size"]].values
y=df["fuel_efficiency"].values
print(x)