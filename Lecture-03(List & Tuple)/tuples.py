##immutable; just like string

tup = (2, 1, 3, 1)
print(type(tup))
print(tup[0])

# tup[0] = 4; Not allowed

tup1 = (1)
print(type(tup1)) # output integer

tup1 = (1,)
print(type(tup1)) # output tuple

print(tup[1: 2])

tup1 = tup
print(tup1)