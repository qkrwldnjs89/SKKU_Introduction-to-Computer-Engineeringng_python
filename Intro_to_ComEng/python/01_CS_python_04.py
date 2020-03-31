# tuple
# 리스트와 비슷하지만 구성요소가 변경될 수 없고, 콤마로 표현되어야하고, 소괄호를 사용한다

a = (1, 2, 3)
print(a)
print(a[:2])
print(a[0:1])

# p is int // q,r,s is tuple
p = (10)
q = (10, 2)
r = (10,)
s = 10, 2
print(s)

c = a + s
print(c)
# a[0] = 2 <<Error cuz tuple is immutable

'''
mutable object = list,dic,set
immutable object:int,float,str,tuple.
int float str은 바꾸는 게 아니고 새로운 값을 들여오는것이다.
'''
