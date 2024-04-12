list1 = [1,2,3,4]
print(list1, sep= " ")
list1.insert(len(list1), 5)
print(list1)
list1.append(6)
print(list1)
list1.extend([7,8,9])
print(list1)
list1.pop(4)
print(list1)
del list1[3]
print(list1)
for x in list1:
    print('value', x)