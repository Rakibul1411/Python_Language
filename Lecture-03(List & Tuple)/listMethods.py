list = [2, 1, 3]

list.append(4)
print(list)

list.sort()
print(list)

list.sort(reverse = True)
print(list)

list.reverse()
print(list)

list.insert(3, 6)
print(list)


print("------------------------------------------")

list1 = ['banana', 'pineApple', 'apple', 'mango']

list1.sort(reverse=True)
print(list1)

list1.reverse()
print(list1)

list1.insert(0, 'asian Pear')
print(list1)

list1.sort()
print(list1)

list1.append('apple')

list1.remove('apple')
print(list1)

list1.pop(0)
print(list1)

copy_list = list1.copy()
print(copy_list)
