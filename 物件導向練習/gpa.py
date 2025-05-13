import math
class Student():
    def __init__(self,firsiname,lastname,gender,status,gpa):
        self.firstname=firsiname
        self.lastname=lastname
        self.gender=gender
        self.status=status
        self.gpa=gpa

    def show_myself(self):
        print(f"First Name: {self.firstname}")
        print(f"Last Name: {self.lastname}")
        print(f"Gender: {self.gender}")
        print(f"Status: {self.status}")
        print(f"GPA: {self.gpa:.2f}")

    def study_time(self,study_time):
        if study_time>0:
            self.gpa=self.gpa+math.log(study_time)
            if self.gpa>4.0:
                self.gpa=4.0

student_data =[
    ("Mike", "Barnes", "male", "freshman", 4.0),
    ("Jim", "Nickerson", "male", "sophomore", 3.0),
    ("Jack", "Indabox", "male", "junior", 2.5),
    ("Jane", "Miller", "female", "senior", 3.6),
    ("Mary", "Scott", "female", "senior", 2.7)
]

student_list = []   

for data in student_data:
    student = Student(*data)
    student_list.append(student)


for student in student_list:
    student.show_myself()
    print("-" * 10) 