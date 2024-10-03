f = open("demo.txt", "r")
data = f.read()
print(data)
print(type (data))
f.close()

f = open("demo.txt", "r")
data = f.read(5) #reads first five characters only
print(data)
f.close()

f = open("demo.txt", "r")
line1 = f.readline() #reads one line at a time
print(line1)
f.close()


