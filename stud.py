class Student:
    def __init__(self,name,age,major,courses):
        self.name=name
        self.age=age
        self.major=major
        self.courses=courses
       
    
    def introduce(self):
        print(f"Hello, my name is {self.name}. I study {self.major}.")

    def major1 (self):
        print(f"My major is {self.major}")

    def gpa1 (self,score):
        self.gpa= score / len(self.courses)
        print(f"My gpa is {self.gpa}")

    def course (self):
        print(f"My courses is {self.courses}")

    def add_course(self, course2,score):
        self.new_course=self.courses +course2
        self.score=score
        print(f"It is your full courses {self.new_course}")
        
    def update_gpa(self):
        self.new_gpa=(self.score + self.gpa*len(self.courses)) / len(self.new_course)
        print(f"It is your new gpa: {self.new_gpa}")

    def is_honor(self):
        if self.new_gpa>3.5:
            print("Красный диплом")
        else:
            print("Нет красного диплома")



    

stud1=Student("Aida",20,"Comaputor Science",  ["Math", "Music","IT"])

#stud1.introduce()
#stud1.major1()
stud1.gpa1(4.5 +5.0 +4.5)
stud1.course()
stud1.add_course(["English"],4.7)
stud1.update_gpa()
#stud1.is_honor()

























































































