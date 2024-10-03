class Student:
  college_name = "DRMC"
    
  def __init__(self, name, marks):
    self.name = name 
    self.marks = marks
  
  def welcome(self):
    print("Welcome student.")
    
  def get_marks(self):
    return self.marks



s1 = Student("Hasan Ali", 80)
s1.welcome()
print(s1.get_marks())