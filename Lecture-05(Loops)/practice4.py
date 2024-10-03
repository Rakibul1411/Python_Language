search = 81

nums = (1, 4, 16, 25, 36, 49, 81, 100)

i = 0
while i < len(nums):
    if(nums[i] == search):
      print('Find the number: ', search)  
      break
    else:
      print('Finding...') 
    i += 1     

j = 0
while j <= 5:
  if(j == 3):
    j += 1
    continue
  print(j)
  j += 1    