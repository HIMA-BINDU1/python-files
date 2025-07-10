### Question

Write a Python program to implement a class Student that has the following functionalities:Private Attributes:name (a string representing the student's name)marks (an integer representing the student's marks, ranging from 0 to 100)Methods:A setter method set_name(name) that sets the student's name.A getter method get_name() that returns the student's name.A setter method set_marks(marks) that sets the student's marks (ensuring marks are between 0 and 100).A getter method get_marks() that returns the student's marks.Constraints:Marks should be between 0 and 100 (both inclusive).If invalid marks are entered (like negative values or values above 100), print an error message.

Output:

Student Name: Alice
Student Marks: 85
Error: Marks should be between 0 and 100.

### Solution

class Student:
    def __init__(self, name,marks):
        self.__name = name
        self.__marks = marks
    def set_name(self):
        self.__name = self.__name
    def get_name(self):
        return self.__name 
    def set_marks(self):
        self.__marks = self.__marks
    def get_marks(self):
        if self.__marks>0 and self.__marks<100:
            return self.__marks
        else:
            return "Marks Should be between 0 and 100"

name = input() 
marks = int(input())
res = Student(name,marks)
print("Student name :",res.get_name())
print("Student marks: ",res.get_marks())
