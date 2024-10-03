def cal_sum(a, b):
  sum = a + b
  print(sum)
  return sum


cal_sum(2, 4)

cal_sum(3, 8)

cal_sum(4, 10)  


def multi(a, b):
  return a * b

mul = multi(3, 8)
print(mul)

def hi():
  print("hi hi")

output = hi()
print(output)  

print('------------------')

def cal_p(a, b = 2): #cal_p(a=2, b) not allowed
   print(a * b)
   return a * b

cal_p(8) 
