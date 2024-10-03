class Student:
    # Default constructors
    def __init__(self):
        pass
        
    # Parameterized constructors
    def __init__(self, name, marks):
        self.name = name # Object attributes > class attributes (precedence)
        self.marks = marks
        print("Adding new student in DataBase.")


s1 = Student("Hasan Ali", 80)
print(s1.name)  
print(s1.marks)

s2 = Student("Rony Biswas", 70)
print(s2.name)
print(s2.marks)



class Car:
    color = "Blue"
    brand = "mercedes"

car1 = Car()
print(car1.color)
print(car1.brand)  


class Bike:
    color = "Black"
    