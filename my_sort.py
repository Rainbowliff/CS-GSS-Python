my_list = [21, 7, 12, 25]
my_list2 = []
print(my_list)
print("Sorting...")
ln = len(my_list)


while len(my_list2) < ln:
    x = min(my_list)
    my_list2.append(x)
    my_list.remove(x)


print(my_list2)

