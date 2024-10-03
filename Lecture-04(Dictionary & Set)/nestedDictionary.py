student = {
  'name' : 'musa',
  'subjects' : {
    'phy' : 97,
    'chem' : 98,
    'math' : 95
  }
} 

print(student)
print(student['subjects'])
print(student['subjects']['chem'])

print('---------------------------')

print(student.keys())
print(list(student.keys()))
print(tuple(student.keys()))

print(len(student))
print(len(list(student.keys())))
print(len(tuple(student.keys())))

print('-------------------')

print(student.values())
print(list(student.values()))

print('-----------------')

print(student.items())
print(list(student.items()))
pairs = list(student.items())
print(pairs[0])

print('----------------------')

print(student['name']) #error
print(student.get('name')) # return---> None

print('-----------------------')

student.update({'city' : 'Dhaka'})
print(student)

new_dict = {'University': 'DU', 'Subject': 'Software Engineering'}
student.update(new_dict)
print(student)
