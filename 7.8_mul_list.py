def mul(num, c):
    list_d = []
    for i in c:
        list_d.append(num * i)
    print("List D:", list_d)
    return


def sum_lists(a, b):
    list_c = []
    for y in range(0, len(a)):
        list_c.append(a[y] + b[y])
    print("List C:", list_c)
    return list_c


x = int(input("Please enter the number for X:"))
list_a = [1, 2, 3, 4, 5, 6]
list_b = [7, 8, 9, 10, 11, 12]

print("List A:", list_a)
print("List B:", list_b)
C = sum_lists(list_a, list_b)
mul(x, C)

