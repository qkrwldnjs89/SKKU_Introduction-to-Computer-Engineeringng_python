# global, local variable _1
print("case 1")
def f():
    print(s)
s = "happy thanksgiving"
f() # global 을 가져다 쓴다.

print("case 2")
def f():
    s = "happy valentine" # s에 대한 assignment가 있는 순간 local으로 인식
    print(s)
s = "happy thanksgiving"
f()
print(s)

'''
print("case 3_1")
def f():
    s = s + "and happy valentine"

    s는 local 인데 이 이전에 s 가
    assignment가 되지 않았으므로 error

    print(s)
s = "happy thanksgiving"
f()
print(s)
'''
'''
case 3_2
x = 5
def my_function():
    print(x)
    x += 5
    x는 local 인데 assignment 되지 않았으므로 error
    print(x)
my_function()
'''
