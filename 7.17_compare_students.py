class student:

    def __init__(self, fname, lname, age, grades, student_id):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.list_of_grades = grades
        self.gpa = sum(grades)/len(grades)
        self.student_id = student_id

    def __str__(self):
        return "\nName:%s %s\nAge:%d\nStudent ID:%09d\nGPA:%d" % \
               (self.fname, self.lname, self.age, self.student_id, self.gpa)

    def __eq__(self, other):
        if self.fname == other.fname and self.lname == other.lname and self.student_id == other.student_id:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.gpa > other.gpa:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.gpa < other.gpa:
            return True
        else:
            return False


stu1 = input("What is the student's first name:")
stu1_5 = input("What is the student's last name:")
stu2 = int(input("What is the student's age:"))
stu3 = int(input("What is the student's id:"))
stu4 = []
x = int(input("How many grades from are you gonna enter:"))
while len(stu4) < x:
    stu4.append(float(input("Please enter a grade(1-4):")))

sstu1 = input("What is the student's name:")
sstu1_5 = input("What is the student's last name:")
sstu2 = int(input("What is the student's age:"))
sstu3 = int(input("What is the student's id:"))
sstu4 = []
x = int(input("How many grades from are you gonna enter:"))
while len(sstu4) < x:
    sstu4.append(float(input("Please enter a grade(1-4):")))

student1 = student(stu1, stu1_5, stu2, stu4, stu3)
student2 = student(sstu1, sstu1_5, sstu2, sstu4, sstu3)

print(student1)
print(student2)

if student1 == student2:
    print("\nThe students are similar")

if student1 > student2 and student2 < student1:
    print("\n", stu1, stu1_5, "is a better student than", sstu1, sstu1_5)
elif student2 > student1 and student1 < student2:
    print("\n", sstu1, sstu1_5, "is a better student than", stu1, stu1_5)
