# 클래스에 관해

# 클래스는 새 타입의 object를 정의하는것

a = 3
print(type(a))

b = "x"
print(type(b))

c = [1, 2, "x"]
print(type(c))

def f():
    print("hello world")
print(type(f))

# Class definition

class Rect:
    c = 0
    def __init__(self, width, height): # method
    # __init__은 메모리가 새 object 에 할당될 때 자동적으로 불러지는 method 이다.
        self.width = width        # 24행과 25행은 instance variable
        self.height = height
        Rect.c += 1

    def calcArea(self):
        area = self.width * self.height
        return area

d = Rect(10, 20)
print(d.calcArea())

r1 = Rect(10, 20)
r2 = Rect(20, 40)
'''
r1 과 r2 는 Rect 의 instance(class variable) 이고 .calcArea() 하면
그 클래스의 method 가 실행된다.
Rect(,) 에 넣어주는 값은 instance value이다.
'''
print(r1.calcArea())
print(r2.calcArea())
print(r1.c)
print(r2.c)
print(Rect.c)
'''
c는 instance variable 이 아니고 class variable 이기 떄문에
해당 class 의 모든 instance 에 의해 공유가 된다.
c는 init 이라는 special method 가 call 될때마다
더해지기 떄문에 3으로 나온다
'''
