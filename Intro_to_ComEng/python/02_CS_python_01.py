# id에 관해

# 리스트
print("case list.1")
a = 3
b = 4
c = 5
d1 = [a, b, c]
d2 = d1 # d1과 d2 사이의 연관이 생김
d1[0] = -1
print(a,d1[0],d2[0])
print(id(a),id(d1[0]),id(d2[0]))
# 첫번째 id != 두번째 = 세번째
print("case list.2")
a = ["abc", "abc"]
b = ["abc", "abc"]
print(id(a), id(b))
print(id(a[0]), id(b[0])) # "abc" 라는 object는 한번만 생성된 것. 또 만들기보다는 메모리에서 가져와 쓴다

# 튜플
print("case tuple.1")
d = ([3, 4], [5, 8])
print(id(d[0]), id(d[1])) # 두개의 id는 다르다.
d[0][1] = -2
print(d)
print(id(d[0]), id(d[1])) # 위와 id는 그대로(object가 생기는게 아니고 값이 바뀜)
