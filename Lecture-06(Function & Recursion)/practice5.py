num = int(input("Enter the number: "))

def sum(n):
  if n <= 1:
    return n
  
  return n + sum(n - 1)


result = sum(num)
print(f"The sum of the first {num} natural numbers is: {result}")

print()