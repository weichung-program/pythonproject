"""請撰寫一個 Subject 類別，內部包涵：
name: 科目名稱
grade: 成績
Teacher: 授課教師
內部可以使用的函式(有三個)：
print_Subject()：會回傳(return)格式化的資料
例如：
Subject: {name}
Grade: {grade}
Teacher: {teacher}

update_grade(new_grade)：會更新成績。

is_passed()：判斷是否通過，若 grade >= 60，回傳 True；否則回傳 False。"""

class Subject:
    def __init__(self,name,grade,Teacher):
        self.name=name
        self.grade=grade
        self.Teacher=Teacher
    def print_Subject(self):
        return (f"Subject: {self.name}\n"
                f"Grade: {self.grade}\n"
                f"Teacher: {self.Teacher}")
    def update_grade(self,newgrade):
        self.grade=newgrade
    def is_passed(self):
        if self.grade>=60:
            return True
        else:
            return False
        
sub = Subject("Math", 50, "Mr. Smith")
print(sub.print_Subject())