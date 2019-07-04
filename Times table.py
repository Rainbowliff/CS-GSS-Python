# SOLUTION 1:
print("\n", " solution 1:", "\n")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = 1
for number1 in numbers1:
    for number in numbers:
        m = number * x
        print(m, end=' ')
    print(" ")
    x += 1


# SOLUTION 2:
print("\n", "solution 2:", "\n")
for n in range(1, 10):
    for n2 in range(1, 10):
        print(n * n2, end=' ')
    print('')


