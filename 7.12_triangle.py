class triangle:

    def __init__(self):
        self.side1 = 0
        self.side2 = 0
        self.side3 = 0


def read_triangle(y):
    print("Please enter the length of", y, ':')
    x = int(input())
    return x


triangle1 = triangle()
triangle1.side1 = read_triangle('side 1')
triangle1.side2 = read_triangle('side 2')
triangle1.side3 = read_triangle('side 3')


def is_triangle(a, b, c):
    my_list = [a, b, c]
    maxi = [max(my_list)]
    my_list.remove(max(my_list))
    if maxi[0] < my_list[0] + my_list[1]:
        print("This is a triangle")
        return
    elif maxi[0] > my_list[0] + my_list[1]:
        print("This is not a triangle")
        return
    elif maxi[0] == my_list[0] + my_list[1]:
        print("This is not a triangle")
        return


is_triangle(triangle1.side1, triangle1.side2, triangle1.side3)
