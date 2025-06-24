for i in range(4):
    print(i)

print("hi")

for i in range(2,10):
    print(i)    

print("hi")

i=0
while i<3:
    print(i)    
    i=i+1

list=["apple", "banana", "strawberry"]
for e in list:
    print(e)


for t in range(2,10):
    print(t)
    for T in range(1,10):
        print(f"t*T={t*T}")       

print("hi")


#sorted use (simply type)
numbers=[2,22,54,7,9,4,23,5,78,4,23455346534,43342,43567]
sorted_numbers = sorted(numbers)
for num in sorted_numbers:
    print(num)

numbers = [2, 22, 54, 7, 9, 4, 23, 5, 78, 4, 23455346534, 43342, 43567]
for i in range(len(numbers) - 1):
    for j in range(len(numbers)-i -1):
        if numbers[j]>numbers[j+1]:
            numbers[j], numbers[j+1]=numbers[j+1], numbers[j]
for num in numbers:
    print(num)


def print_hello():
    print("안녕하세요!")
print_hello()    

def mod(a,b):
    return a/b
    return a%b
print(mod(7777,3))  

 
 
 
  
    
