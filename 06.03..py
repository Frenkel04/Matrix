from posixpath import lexists
import genericpath


class Person:
    marks = []
    subjects = 0
    age = 12
    def __init__(self, name, sex, age, subjects = int):
        self.name = name
        self.sex = sex
        self.age = age
        self.subjects = subjects
        if 1 <= subjects <= 10:
            self.subjects = subjects
        else:
            raise ValueError("wrong num of subjects")

    def __str__(self):
        return f"My name is {self.name}. I’m {self.age}. I have {self.subjects} subjects"


class Pupil(Person):
    class_num = 0
    class_let = 'f'
    if 6 <= Person.age <= 18:
        Person.age = 12
    else:
         raise ValueError("wrong age")
    if not class_let.islower():
        class_let = chr
    else: 
        raise ValueError("wrong symbol")
    
def info(self):
    return f"My name is {Person.name}. I’m {Person.age}. I have {Person.subjects} subjects. I’m in {self.class_num} class named {self.class_let}"

st = Pupil("Masha", 0, 12, 5, 4, 'A')
for st in Pupil:
    st.info()
