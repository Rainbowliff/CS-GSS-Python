print("What is your name?")
name = input()

print ("How many seconds would you like to convert? Please enter")
second = input()

z = int(second/60)
hour = int(z/60)
minutes = int(z - hour*60)
remaining = second - z*60

print ("Hi", name, second, "seconds is equal to", hour, 'hour(s)', minutes, 'minute(s) and', remaining, 'seconds')
