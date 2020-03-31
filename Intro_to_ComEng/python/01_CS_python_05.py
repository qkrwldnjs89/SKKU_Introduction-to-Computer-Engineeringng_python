# id() function returns "identity" of the object.
# identity is guaranteed to be unique and constant
# for this object during its lifetime

# immutable > id 가 바뀜 > object 가 바뀜
a = 42
print(id(a))
a = 21
print(id(a))
a += 3
print(id(a))
print(a)

# mutable > id 가 바뀌지 않음 > object 가 바뀌지 않음
b = [1, 2, 3]
print(id(b))
b += [6]
print(id(b))
print(id(b[0]))
print(id(b[1]))
print(id(b[0:1]))
print(id(b[:])) # 21열과 22열의 id값은 같다.
