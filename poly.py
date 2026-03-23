from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, age, salary):
        self.name=name
        self.age=age
        self.salary=salary

    @abstractmethod
    def work(self):
        pass

    def display_info(self):
        return f"Name:{self.name}, Age: {self.age}, Salary:{self.salary}."
        
class Developer (Employee):
    def __init__(self, name, age, salary,programming_language):
        super().__init__(name, age, salary)
        self.programming_language=programming_language

    def display_info(self):
        return super().display_info()
        
    def work(self):
        #return super().work()
        return f"{self.name} пишет код на {self.programming_language}."

class Manager (Employee):
    def __init__(self, name, age, salary,team_size):
        super().__init__(name, age, salary)
        self.team_size=team_size

    def display_info(self):
        return super().display_info()
        
    def work(self):
        #return super().work()
        return f"{self.name} управляет командой из {self.team_size}человек."        

def info(inf):
    print(inf.display_info())

def job(obj):
    print(obj.work())

d1 = Developer("Katya", 40 , 90000, "Python")
m1 = Manager("Aleks",30, 70000, 10)


info(d1)
job(d1)
info(m1)
job(m1)

#d1.display_info()
#d1.work()
#m1.display_info()
#m1.work()