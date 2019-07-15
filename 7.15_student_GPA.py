class student:

    def __init__(self):
        self.name = 'Bob'
        self.age = 15
        self.list_of_grades = []
        self.gpa = 0
        self.graduation_day = 13
        self.graduation_month = 5
        self.graduation_year = 2019

    def find_gpa(self):
        sumn = 0
        for i in range(len(self.list_of_grades)):
            sumn = sumn + i
        self.gpa = sumn/len(self.list_of_grades)
        return self.gpa

    def read_stu(self):
        self.name = input("Please enter the student's name:")
        self.age = int(input("Please enter the student's age:"))
        x = int(input("How many grades from are you gonna enter:"))

        while len(self.list_of_grades) < x:
            self.list_of_grades.append(input("Please enter a grade(1-4):"))

        self.graduation_day = int(input("Please enter the student's graduation day:"))
        self.graduation_month = int(input("Please enter the student's graduation month:"))
        self.graduation_year = int(input("Please enter the student's graduation year:"))

    def print_student(self):
        print("\nName:", self.name)
        print("Age:", self.age)
        print("GPA:", self.gpa)
        print("Graduation date:", self.graduation_month, '/', self.graduation_day, '/', self.graduation_year)


student1 = student()
student.read_stu(student1)
student.find_gpa(student1)
student.print_student(student1)
