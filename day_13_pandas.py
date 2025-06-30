import pandas


'''
dictionary: 무조건 {} 나오고 안에 {'키'} 나오고 {'키': 값 } 이런형태를 가지고 있다
값은 무조건 list여야 한다. 각 리스트 갯수도 서로 같아야한다.
이 자료구조 법칙을 어기면 함수 작동을 안한다


mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

# dictoionary를  pandas로 읽는 건, 무조건  pandas.DataFrame(mydataset)이 코드로 정해져 있다.

myvar = pandas.DataFrame(mydataset)

print(myvar)

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df) 

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

data1 = {
    "집값" : [30, 15, 7]
}

dt1 = pd.DataFrame (data1, index = [2022, 2017, 2010])

print(dt1)

'''

import pandas as pd
df4 = pd.read_csv('data11.csv')
print(df4)

df= pd.read_csv('test1.csv')
df=df[['LIMIT_BAL','SEX','EDUCATION','MARRIAGE','AGE']]
df = df[
  (df['SEX'].isin([1, 2])) &
  (df['EDUCATION'].isin([1,2,3,4])) &
  (df['MARRIAGE'].isin([1,2]))
]
print(df)

max_limit_bal_id = df['LIMIT_BAL'].idxmax()
max_limit_bal = df.loc[max_limit_bal_id]
print(max_limit_bal)

min_limit_bal_id = df['LIMIT_BAL'].idxmin()
min_limit_bal = df.loc[min_limit_bal_id]
print(min_limit_bal)

