class Animal:
    def __init__(self, name):
        self.name = name
    def move(self):
        print("move")
    def speak(self):
        pass
# Animal 이라는 클래스를 만든다.
class Dog (Animal):
    def speak(self):
        print("bark")
# Animal 이라는 클래스를 parent 로 갖는 child class.
class Duck (Animal):
    def speak(self):
        print("quack")
# Animal 이라는 클래스를 parent 로 갖는 child class.

# child class 는 parent class 의 메소드를 가져와 쓸 수 있다.

a = Animal("mydog")
b = Dog("mydog2")
c = Duck("myduck")

a.move()
b.move()
c.move()

b.speak()
c.speak()
a.speak()

print("__________________________________________")
animals = [Dog('doggy'), Duck('duck'), Duck('duck2')]
for a in animals:
    a.speak()
