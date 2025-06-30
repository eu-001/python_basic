import pandas

'''
dictionary: 무조건 {} 나오고 안에 {'키'} 나오고 {'키': 값 } 이런형태를 가지고 있디
'''

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)