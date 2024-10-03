#set --> mutable; but elements of set --> immutable
collection = set ()

collection.add(1)
collection.add(2)
collection.add(3)
collection.add(4)

print(collection)

collection.remove(2)
print(collection)

collection.add((5, 6))
print(collection)

collection.clear()
print(collection)

collection = {'hi', 'bye', 'coding', 'python', 'angular'}
print(collection.pop())
print(collection.pop())

print(collection)

set1 = {1, 2, 3}
set2 = {2, 3, 4}

set3 = set1.intersection(set2)
print(set3)

print(set1.union(set2))
print(set1.intersection(set2))

