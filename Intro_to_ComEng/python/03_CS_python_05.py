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

a = Rect(10, 20) # a 가 self 가 된다.
print(a.calcArea())
# Rect.calcArea() >>> self 파라미터가 없어서 traceback 이 뜬다.
print(Rect.calcArea(a)) # a 가 self 가 된다. 14행과 같은 의미를 가지는 줄
# self 가 되는것은 첫번째 parameter.
print("_________________________")
print(type(Rect.calcArea)) # funtion
print(type(a.calcArea)) # method
'''
두 가지가 다른 이유는 a 는 instance 이고 20행에서는 a의 method로 나옴
instantiation이 되어있는 상태가 아니므로 19행의 Rect.calcArea 는
funtion 이다.
'''
