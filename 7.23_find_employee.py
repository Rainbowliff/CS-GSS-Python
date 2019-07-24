class employee:
    def __init__(self, fname, lname, id, dur, sal):
        self.first_name = fname
        self.last_name = lname
        self.eID = id
        self.e_duration = int(dur)
        self.salary_per_day = int(sal)
        self.earned = self.e_duration * self.salary_per_day

    def __str__(self):
        return "\nName:%s %s\nID:%08d\nDuration:%ddays\nSalary(per day):$%d\nEarned:$%d" % \
               (self.first_name, self.last_name, self.eID, self.e_duration, self.salary_per_day, self.earned)

    def __eq__(self, other):
        if self.last_name == other:
            return True
        else:
            return False


def find_employee(l, x, count):
    try:
        if l[count] == x:
            print(l[count])
            return
        elif l[count] != x:
            find_employee(l, x, count + 1)
    except IndexError:
        print("\nNo results")
        return


file = open("7.23_input.txt", 'r')
my_list = []
for i in file:
    lists = i.split(',')
    namel = lists[0]
    namef = lists[1]
    eid = int(lists[2])
    edur = int(lists[3])
    esal = int(lists[4])
    emp = employee(namef, namel, eid, edur, esal)
    my_list.append(emp)

ln = input("Please enter the last name of the one you're looking for:")
find_employee(my_list, ln, 0)
