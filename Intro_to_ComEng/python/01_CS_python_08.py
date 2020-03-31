# 조건문 loop

#if 문
x = int(input("Please enter an integer: "))

if x < 0 :
    x = 0
    print("Negative changed to Zero")
elif x == 0:
    print("Zero")
elif x == 1:
    print("Single")
else: print("Positive")

# for 문
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

#while 문
i = 1
while i < 5:
    print(i)
    i += 1
