class Car:
    
    is_car = True

    def __init__(self,miles=0) -> None:
        self.miles = miles


    def drive(self,miles) -> None:
        self.miles += miles

    def reverse(self,miles) -> None:
        self.miles -= miles

    def get_miles(self) -> int:
        return self.miles

    def get_report(self) -> str:
        return f"Car has driven: {self.get_miles()} miles"
'''
car = Car()
car.drive(100)
car.reverse(4)
print(car.get_report())
'''

class Student:

    def __init__(self,name,gpa) -> None:
        self.name,self.gpa = name,gpa

    def get_last(self) -> str:
        return self.name.split()[-1]

    def get_first(self) -> str:
        return self.name.split()[0]

    def get_gpa(self) -> int:
        return self.gpa

class Course:
    
    def __init__(self, roster) -> None:
        self.roster = roster

    def get_deans_list(self) -> list:
        return [s for s in self.roster if s.get_gpa() >= 3.5]



# student1 = Student('Craig Tadpole',3.8)
# student2 = Student('Bill Toad',2.5)
# student3 = Student('Another Frog',3.7)
# student4 = Student('Tim Roach',3.5)
# course = Course([student1,student2,student3,student4])
# deans = course.get_deans_list()
# for s in deans:
#     print(f'{s.get_last()}\t{s.get_gpa()}')
