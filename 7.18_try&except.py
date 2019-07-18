class student:

    def __init__(self):
        self.fname = ''
        self.lname = ''
        self.student_id = 0
        self.gpa = 0.0

    def __str__(self):
        return "\nName:%s %s\nStudent ID:%09d\nGPA:%d" % (self.fname, self.lname, self.student_id, self.gpa)


    def get_info(self):
        self.fname = input("Please enter the student's first name:")
        self.lname = input("Please enter the student's last name:")
        self.student_id = int(input("Please enter the student's student ID:"))
        self.gpa = float(input("Please enter the student's GPA:"))


user = ''
while user != 'q':
    try:
        stu1 = student()
        stu1.get_info()
    except:
        print("Something went wrong")
        print("Enter any key('q' to quit)")
        user = input()
