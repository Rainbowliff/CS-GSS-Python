import math
print ("This is a program which solves ax^2+bx+c=0 problems")
print ("Please enter the number for 'a'")
a = input()

print ("Please enter the number for 'b'")
b = input()

print ("Please enter the number for 'c'")
c = input()

down = 2 * a
delta = (b ** 2) - (4 * a * c)

if delta > 0:
    sr = math.sqrt(delta)
    answer1 = (-b + sr)/down
    answer2 = (-b - sr)/down
    print "x =", answer1, "and", answer2

elif delta == 0:
    answer = -b/down
    print "x =", answer

elif delta < 0:
    print "x = no solution"
