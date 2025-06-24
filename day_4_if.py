if(True):
    print(f"조건문이 true 라서 여기가 실행 되었네요")
if False:
    print(f"조건문이 False라서 여기는 실행이 안되었네요")

a=""
if(a):
    print(f"a:{a}")

a=""
print(f"a:{a}")

#if문에서 None, null, "", 0 = False

x=10
if x:
    print(f"x:{x}")
    print(x)

def dummyFunc():
    return True
if dummyFunc():
    print(dummyFunc)    

"""
my_typing=input("숫자를 입력하시오:")
print(f"my_typing: {my_typing}")
print(f"my_typing type: {type(my_typing)}")
my_number=int(my_typing)
if my_number % 2 ==0:
    print("짝수입니다")
else :
    print("홀수입니다")
"""
# else = if my_number % 2 !=0, % 2 > 0 , int는 모든 숫자형태를 정수로 만든다
"""
my_score=int(input("성적을 입력하시오:"))
if my_score  >= 90:
    print("학점 A 입니다")
elif my_score >= 80:
    print("학점 B 입니다")
elif my_score >= 70:
    print("학점 c 입니다")
elif my_score >= 60:
    print("학점 D 입니다")
else:
    print("학점 F 입니다")

"""    


num1 = float(input("첫 번째 숫자를 입력하세요: "))
operator = input("연산자 (+, -, *, /) 입력: ")
num2 = float(input("두 번째 숫자를 입력하세요: "))

if operator == "+":
    print(f"결과: {num1 + num2}")
elif operator == "-":
    print(f"결과: {num1 - num2}")
elif operator == "*":
    print(f"결과: {num1 * num2}")
elif operator == "/":
    if num2 != 0:  
        print(f"결과: {num1 / num2}")
    else:
        print("❌ 0으로 나눌 수 없습니다!")
else:
    print("❌ 잘못된 연산자입니다!")

# int는 정수를, float는 소수점을 포함한 숫자를 처리한다
                