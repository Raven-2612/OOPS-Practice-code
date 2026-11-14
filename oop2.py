from abc import ABC,abstractmethod

class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def average(self):
      return sum(self.marks) / len(self.marks)

    def grade(self):
       avg=self.average()
       if avg>=90:
          return "A"
       elif avg>=75:
          return "B"
       elif avg>=50:
          return "C"
       else:
          return "Fail"

    def display(self):
       print(f"Name:{self.name}| Roll No:{self.roll_no}| Average:{self.average():.2f}| Grade:{self.grade()}")
          


s1 = Student("Arun", 1, [80, 75, 90])
s2 = Student("Divya", 2, [95, 92, 98])
s3 = Student("Karthik", 3, [40, 35, 50])

s1.display()
s2.display()
s3.display()

