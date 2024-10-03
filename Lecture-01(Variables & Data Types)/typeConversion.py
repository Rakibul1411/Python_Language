#type conversion ---> python compiler handle implicitly
a = 2
b = 4.25

sum = a + b #2.0 + 4.25 => 6.25
print(type(a))
print(sum)

#type casting

c = float("2")
d = int(4)

print(type(c))
print(c + d)
print(type(d))


t = 3.14
t = str(t)

print(type(t))