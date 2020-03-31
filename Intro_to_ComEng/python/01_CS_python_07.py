# key,value 가 없는 dict

a1 = set()
a2 = {1, 3, 5, 7}
a3 = set([1, 3, 5, 7])
a4 = set([1, 3, 3, 7]) # 중복 사라짐
a5 = set([x * 2 for x in range(1,10)]) # x * 2의 집합
a6 = set("abac") # 하나하나로 나뉜 다음 dic으로
print(a1)
print(a2)
print(a3)
print(a4)
print(a5)
print(a6)

a = {1, 2, 4}
b = {1, 3, 5}

print(a.intersection(b)) # = a & b >>교집합
print(a.difference(b)) # = a - b >> 차집합
print(a.union(b))
print(a.symmetric_difference(b)) # = a ^ b >> 서로다른것들
