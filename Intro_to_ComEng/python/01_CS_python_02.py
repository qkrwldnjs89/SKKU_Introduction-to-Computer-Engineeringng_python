# input, print, format

a = input("input a number: ")
print("input a number: ")
b = input()
# input 시 최초형태는 str 형태이다.
result = int(a) * int(b)
# printI("(자릿수) * (자릿수) = (자릿수)".format(첫값,둘째값,셋째값))
print("{0} * {1} = {2}".format(a, b, result))
