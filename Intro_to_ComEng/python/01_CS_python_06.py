# Dictionary

dic = {'jack': 4098, 'john': 4139, 'josh': 4127}
print(dic['jack']) # dict 에서의 indexing은 key값으로
print(list(dic.keys())) # key 값들의 list
print(list(dic.values())) # value 값들의 list

for k,v in dic.items() :
    print(k,v)
