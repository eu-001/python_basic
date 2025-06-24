'''
for i in range(3):
    break
    print("loop")

#for문에서 break은 루프를 종료 시킨다

for i in range(10):
    if i%2==1:
        continue
    print(f"i:{i}")

'''
"""
def fsum(n):
    if n <=1:
        return n
    return n+fsum(n-1)

tsum=fsum(5)
print(tsum)
"""
"""
num = input("숫자를 입력해주세요:")
if num % 2 == 0:
    print("짝수입니다")
else :
    print("홀수입니다")
"""


'''
num = int(input("숫자를 입력하시오:"))
if num < 2:
    print("2이상의 숫자만 확인이 가능합니다")
else:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num}은 소수가 아닙니다")
            break
    else:
        print(f"{num}은 소수입니다")
'''
def count_ones(s):
    if len(s) == 1 :
        return 1 if s == '1' else 0
    mid = len(s) // 2
    return count_ones(s[:mid]) + count_ones(s[mid:])
print(count_ones("101110"))        

'''
def fPrimeNum(a):
    bPrimeNum=True
    for i in range(2,a):
        bPrimeNum=False
        break
    return bPrimeNum
num1=int(input("숫자를 입력하세요:"))
bPrimeNum=fPrimeNum(num1)
if bPrimeNum:
    print(f"{num1} 은 소수 입니다")
else:
    print(f"{num1} 는 소수가 아닙니다")
'''
'''
mytype=""
mytype=input("수학 수식을 넣어주세요:")
result=eval(mytype)
print(f"{mytype}:{result}")
#eval() 문자열로 된 파이썬 표현식을 실제 코드처럼 실행해주는 함수
#but eval()함수는 매우 강력하지만, 보안상 위험할 수도 있다. 그래서 저 함수는 사용을 지양하는 편이고 ast.literal_eval()처럼 안전한 대체 함수를 쓰기도 한다
''' 

from random import shuffle
list1=[]
for i in range(1,46):
    list1.append(i)
shuffle(list1)
print(f"추첨번호: {list1[0:6]}")