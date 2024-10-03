my_list = [1, 2, 3, 4, 5]

def print_list(list, index):
  if index == len(list):
    return
  
  print(list[index], end=" ")
  print_list(list, index+1)


print_list(my_list, 0)

print()