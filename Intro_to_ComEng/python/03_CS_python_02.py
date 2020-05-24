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

r1 = Rect(10, 20)
r2 = Rect(20, 40)
r1.c = -1

print(r1.calcArea())
print(r2.calcArea())

print(r1.c)
print(r2.c)
print(Rect.c)
