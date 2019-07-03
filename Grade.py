
print ("Please enter your grade:")
x = input()

if x > 100:
    print ("Please enter a VALID grade (0-100)")
    x = input()

if 100 >= x >= 91:
    print ("Congratulations!,you got an 'A'!")

elif 90 >= x >= 81:
    print ("You got a 'B'!")

elif 80 >= x >= 71:
    print ("You got a 'C'!")

elif 70 >= x >= 61:
    print ("You got a 'D'! Gotta work harder now!")

elif x <= 60:
    print ("Uh no! It looks like you failed! You got a 'F'!")
