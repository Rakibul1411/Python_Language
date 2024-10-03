# Static methods work at Class Level

class Student:
  def __init__(self, name, marks):
    self.name = name
    self.marks = marks
  
  @staticmethod #decorator
  def hello():
    print("Hello there!")
  
  def get_avg(self):
    sum = 0
    for val in self.marks:
      sum += val
    print("Hi", self.name, "your avg score is:", sum / 3)

s1 = Student("Ali", [89, 78, 56])
s1.get_avg()
