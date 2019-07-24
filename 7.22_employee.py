class employee:
    def __init__(self, fname='', lname='', id=0, dur=0, sal=0):
        self.first_name = fname
        self.last_name = lname
        self.eID = id
        self.e_duration = int(dur)
        self.salary = int(sal)

    def __str__(self):
        return "\nName:%s%s\nID:%08d\nDuration:%ddays\nSalary(per day):$%d" % \
               (self.first_name, self.last_name, self.eID, self.e_duration, self.salary)

    def money(self):
        m = self.e_duration * self.salary
        return int(m)


file = open("7.22_input.txt", 'r')
afile = open("7.22_output.txt", 'w')
my_list = []
employee_list = []
for i in file:
    lists = i.split(',')
    namel = lists[0]
    namef = lists[1]
    eid = int(lists[2])
    edur = int(lists[3])
    esal = int(lists[4])
    emp = employee(namef, namel, eid, edur, esal)
    d = emp.money()
    my_list.append(d)
    employee_list.append(emp)
    afile.write(namel)
    afile.write(",")
    afile.write(namef)
    afile.write(", ")
    afile.write(str(eid))
    afile.write(", ")
    afile.write(str(edur))
    afile.write(", ")
    afile.write(str(esal))
    afile.write(", ")
    afile.write(str(d))
    afile.write("\n")
afile.write("The company has paid all of it's employees $")
afile.write(str(sum(my_list)))
afile.close()
file.close()
nfile = open('7.22_output.txt', 'r')
for n in employee_list:
    print(n)

print("\n")
for l in nfile:
    print(l)
nfile.close()

