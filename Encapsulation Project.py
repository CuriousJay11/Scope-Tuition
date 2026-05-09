class Student:
    def __init__(self, name):
        self.name = name
        self.__marks = 0

    def set_grade(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Grade must be between 0-100")

    def get_grade(self):
        return self.__marks

    def get_info(self):
        return f"Name: {self.name}, marks: {self.__marks}"


s1 = Student("Alice")

s1.set_grade(85)

print(s1.get_grade())   
print(s1.get_info())  

#Homework



        