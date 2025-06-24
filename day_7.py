list1=[1,2,3,4,5]
result=[list1.pop(0) for i in list1]
print(result)

# 0. 1  1. 2  2.3 

list2=[1,2,3,4,5]
result =[list2.pop(0)* i for i in list2]
print(result)

# 1*1  2*3 3*5

class MyClass:
    def __init__(self):
        pass
class Customer:
    def __init__(self,name,birthdate,rank):
        self.name=name
        self.birthdate=birthdate
        self.rank=rank    
customer1=Customer("eugene","6.30","student")
print(customer1.name, customer1.birthdate, customer1.rank)     

class Animal:
    def __init__(self):
        pass
    def bark(self):
        print("grrrrrr")
class Animal2:
    def __init__(self):
        pass
    def bark(self):
        print("ggggggrrrrrr")
class Dog(Animal,Animal2):
    def __init__(self, name):
        self.name=name
    def run(self):
        print("running")

# Dog(Animal, Animal2)에서 가장 왼쪽것인 Animal이 실행된다        

animal1=Animal()
animal1.bark()      
dog1=Dog("보더콜리")
dog1.bark()
dog1.run()