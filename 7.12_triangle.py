class triangle:

    def __init__(self):
        self.side1 = 0
        self.side2 = 0
        self.side3 = 0

    def read_triangle(self):
        self.side1 = int(input("Enter the length of side 1:"))
        self.side2 = int(input("Enter the length of side 2:"))
        self.side3 = int(input("Enter the length of side 3:"))

    def is_triangle(self):
        my_list = [self.side1, self.side2, self.side3]
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


triangle1 = triangle()
triangle.read_triangle(triangle1)
triangle.is_triangle(triangle1)
