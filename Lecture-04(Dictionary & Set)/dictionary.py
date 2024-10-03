#Dictionary is mutable, unordered, not allowed duplicate key

info = {
  "key" : 1,
  'name' : 2,
  'subjects' : ['python', 'c', 'java'],
  'topics' : ('dictionary', 'set'),
  'is_right' : True,
  12.99 : 8,
  True : False 
}

print(type(info))
print(info)

print(info['topics'])
print(info["subjects"])

info['name'] = 'value'
info['firstName'] = 'musa'

print(info)

null_dictionary = { }

print(null_dictionary)