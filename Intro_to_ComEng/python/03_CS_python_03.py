a = "cookie1"
a_width = 3
a_height = 5
a_area = a_width * a_height
print("{0} area is {1}".format(a, a_area))

b = "cookie2"
b_width = 4
b_height = 6
b_area = b_width * b_height
print("{0} area is {1}".format(b, b_area))

class Rect:
    c = 0
    def __init__(self, name, width, height): # method
    # __init__은 메모리가 새 object 에 할당될 때 자동적으로 불러지는 method 이다.
        self.name = name
        self.width = width        # 24행과 25행은 instance variable
        self.height = height
        Rect.c += 1

    def calcArea(self):
        area = self.width * self.height
        return area

r1 = Rect("cookie1", 3, 5) # r1 이 self 로 들어간다.
print(r1.calcArea())
r2 = Rect("cookie2", 4, 6) # r2 가 self 로 들어간다.
print(r2.calcArea())
