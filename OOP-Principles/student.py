from datetime import date
from person import Person

class Student(Person):
    def __init__(self, first_name, last_name, birth_date, ID, university: str, grade: int):
        super().__init__(first_name, last_name, birth_date, ID)
        self.university = university
        self.grade = grade
    
    def set_university(self, university: str):
        self.university = university
        
    def set_grade(self, grade: int):
        self.grade = grade
        
    def get_university(self) -> str:
        return self.university
    
    def get_grade(self) -> int:
        return self.grade


student = Student("John", "Doe", date(2000, 10, 20), 123456, "TATU", 3)
print(student.get_full_name())
print(student.get_grade())
print(student.get_id())
