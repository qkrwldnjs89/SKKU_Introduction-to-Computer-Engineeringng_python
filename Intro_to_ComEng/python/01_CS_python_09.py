# 함수 정의하기
def hello() :
    print("Sungkyunkwan University")
hello()

def func(arg) : # arg는 func 의 내용에서 쓰이는 변수
    if arg >= 0 :
        result = arg
    else:
        result = arg * -1
    return result
p = func # 괄호 넣지 않는 것 주의
print(p(-5))

def plus(a,b):
    return a + b
def minus(a,b):
    return a - b

flist = [plus, minus]
print(flist[0](1,5))
print(flist[1](5,3))
