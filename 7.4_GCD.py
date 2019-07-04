x = int(input("Enter the first number:"))
y = int(input("Enter the second number:"))

if x > y:
    s = y
else:
    s = x

for i in range(1, s + 1):
    if (x % i == 0) and (y % i == 0):
        gcd = i

print("The GCD is:", gcd)
