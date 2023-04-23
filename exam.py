class Worker():
    """ Работник """
    __hours : int()
    __salary : float()
    
    
    # Constructor
    def __init__(self,Hours,Salary):
        try:
            if (Hours<30 or Hours>=50):
                raise ValueError("incorrect hours for a worker")
        except ValueError:
            print('incorrect hours for a worker')
        else:
            try:
                if (Salary<500 or Salary>=1500):
                    raise ValueError("incorect salary value")
            except ValueError:
                print('incorrect salary value')
            else:
                self.__hours = Hours
                self.__salary = Salary
                
    def set_hours (self, Hours):
        try:
            if (Hours<30 or Hours>=50):
                raise ValueError("incorrect hours for a worker")
        except ValueError:
            print('incorrect hours for a woker')
        else:
            self.__hours = Hours
            
    def set_salary (self, Salary):
        try:
            if (Salary<500 or Salary>=1500):
                raise ValueError("incorect salary value")
        except ValueError:
            print('incorrect salary value')
        else:
            self.__salary = Salary
            
    def get_total_salary(self):
        return (self.__hours * self.__salary * 4)
    
    def get_hours(self):
        return self.__hours
    
    def get_salary(self):
        return self.__salary
    
    def prints(self):
        try:
            a = self.__hours
        except AttributeError:
            print("incorrect object Woker = NULL")
        else:
            print ("I'am worker. I work ",{self.__hours}, " per week and earn ", {self.__salary}, " per hour")
    
class Leader(Worker):
    """ Начальник """
    __list_worker : list()
    __salary_per_week : float()
    
    # Constructor
    def __init__(self, List=[]):
        self.__list_worker = list()
        self.__salary_per_week = 0
        salary_total_temp = 0
        for li in List:
            self.__list_worker.append(li)
            s = li.get_salary
            h = li.get_hours
            salary_total_temp = (li.get_hours() * li.get_salary()) + salary_total_temp
        self.__salary_per_week =  salary_total_temp / 2


    def add(self, worker):
        self.__list_worker.append(worker)

 
        self.__salary_per_week = self.__salary_per_week + (((worker.get_hours())*(worker.get_salary()))/2)
        
    def delete_right (self):
        self.__list_worker.pop()
        salary_total_temp = 0
        for li in self.__list_worker:
            salary_total_temp = (li.get_hours() * li.get_salary()) + salary_total_temp
        self.__salary_per_week =  salary_total_temp / 2

    def delete_left (self):
        del self.__list_worker[0]
        salary_total_temp = 0
        for li in self.__list_worker:
            salary_total_temp = (li.get_hours() * li.get_salary()) + salary_total_temp
        self.__salary_per_week =  salary_total_temp / 2

    def prints(self):
        try:
            a = self.__salary_per_week
        except AttributeError:
            print("incorrect object Leader = NULL")
        else:
            print ("I'm Leader. I have ",{len(self.__list_worker)}, " workers in my team and i earn", {self.__salary_per_week}, " per week ")



import random
from array import array

i = 0
array_worker = []

while (i<5):
    try:
        
        random_hours = random.randint(20, 54)
        random_salary = random.randint(350, 1699)
    
        temp_worker = Worker(random_hours,random_salary)
        if (random_hours<30 or random_hours>=50 or random_salary<500 or random_salary>=1500):
            raise ValueError("incorrect object = null ")
    except ValueError:
        print("incorrect object = null")
    else:
        print ("New Worker was created successfully with stats")
        temp_worker.prints()
        array_worker.append(temp_worker)
        i = i+1

print("===")   
ld01 = Leader()
ld01.prints()

print("===")    
ld01.add(array_worker[4])
ld01.prints()
array_worker[4].prints()


print("===")
list_2_3_4 =  [array_worker[1], array_worker[2], array_worker[3]]
ld02 = Leader(list_2_3_4)
ld02.prints()
array_worker[1].prints()
array_worker[2].prints()
array_worker[3].prints()

print("===") 
ld02.delete_right()
ld02.prints()
array_worker[1].prints()
array_worker[2].prints()

print("===") 
ld01.add(array_worker[4])
ld02.prints()
array_worker[1].prints()
array_worker[2].prints()
array_worker[4].prints()

print("===")
ld01.delete_left()
ld02.prints()
array_worker[2].prints()
array_worker[4].prints()
