class Student:
    def __init__(self,Name,age,mark):
        self.name = Name
        self.age = age
        self.mark = mark
    def get_details(self):
        print("the Student name is",self.name,"mark",self.mark)

s1 = Student("sowntharya",18,100)
s2 = Student("jo",18,100)
s1.get_details()
s2.get_details()