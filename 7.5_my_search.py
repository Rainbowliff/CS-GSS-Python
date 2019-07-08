my_list = [3, 15, 1, 8, 20, 7, 21, 25, 86, 198, 75, 46, 52]


def search():
    x = int(input("What is the number you're searching for:"))

    for number in my_list:
        if x == number:
            print("The index of your number is", my_list.index(x))
            e = 0
            return 0
            break
        else:
            e = -1

    if e == -1:
        return -1
        print("The item is not found")


search()


