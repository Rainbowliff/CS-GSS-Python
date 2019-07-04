numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

x = 1
for number1 in numbers1:

    for number in numbers:
        m = number * x
        print(m, ' ', end='')

    print("\n")
    x += 1
