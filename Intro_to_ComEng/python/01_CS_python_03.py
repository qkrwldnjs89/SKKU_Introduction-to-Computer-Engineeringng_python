# 리스트

# list
a = [1, 2, 3, 4]

#indexing
print(a)
print(a[1])

# 덮어씌워짐
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# slicing
print(a[:]) # all of list
print(a[0:5]) # [1, 2, 3, 4, 5]
print(a[5:]) # [6, 7, 8, 9, 10] <<5자리부터 9자리
print(a[:3]) # [1, 2, 3] <<0자리부터 2자리

# list 더하기
b = [-1, -5, 10]
print(a + b)

# list 요소 덮어씌우기
b[2] = 11
print(b[2])

# list can be used for stack
stack = [3, 4, 5]
stack.append(6) # push on the last location of the list
print(stack)
stack.pop() # print out the latest one and delete
print(stack)
