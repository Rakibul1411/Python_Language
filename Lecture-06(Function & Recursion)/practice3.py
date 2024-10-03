num = int(input("Enter the value: "))

def fact(n):
  result1 = 1
  for i in range(n, 0, -1): # range(1, n+1) also work
    result1 *= i
  return result1  
  
result = fact(num)

print()  