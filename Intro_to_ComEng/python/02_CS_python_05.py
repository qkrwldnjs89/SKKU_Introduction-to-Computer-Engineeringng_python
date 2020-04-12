# Argument passing_1 : mutable, immutable
print("case 1")
def dataCalc1(data):
    data += 1
def dataCalc2(data):
    data[0] += 1

data1 = 1
data2 = [1]

dataCalc1(data1)
print(data1) # 1이 출력, data1의 int는 update 되지 않음 local

dataCalc2(data2)
print(data2) # [2]가 출력, list의 구성요소는 변경

# Argument passing_2 : mutable, immutable
print("case 2")
def dataCalc1(data):
    print(id(data1), id(data))
    data += 1
    print(id(data1), id(data)) # 두 id는 다르다. local assignment 가 새 variable을 만들었음.
def dataCalc2(data):
    print(id(data2), id(data))
    data[0] += 1
    print(id(data2), id(data))

data1 = 1
data2 = [1]

dataCalc1(data1)
print(data1)

dataCalc2(data2)
print(data2)
