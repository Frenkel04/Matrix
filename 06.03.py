"""import genericpath
import random

class Person:
    marks = []
    subjects = 0
    def __init__(self, name, sex, age, subjects = int):
        self.name = name
        self.sex = sex
        self.age = age
        self.subjects = subjects
        if 1 <= subjects <= 10:
            self.subjects = subjects
        else:
            raise ArgumentException("wrong num of subjects")

    def __str__(self):
         return f"My name is {self.name}. I’m {self.age}. I have {self.subjects} subjects"
    
    def grades(self, marks,):
        if type(marks) == str:
            marks = ''.join(marks.split(';'))
            marks = [int (i) for i in marks.split()]
        if not len(marks) == self.subjects:
            raise ValueError("wrong num of marks")
        for mark in marks:
          if not 0 <= mark <= 10:
              raise ValueError("wrong type of marks")

        self.marks = marks

def main():
    a = Person("Masha", 0, 12, 3)
    a.grades([-1, 2, 3])""'
    
    
