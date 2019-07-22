class rectangle:

    def __init__(self):
        self.width = 0
        self.length = 0

    def __str__(self):
        return "\nThis is a rectangle.\n\nWidth:%d\nLength:%d\n" % \
               (self.width, self.length)

    def get_value(self):
        x = int(self.width * self.length)
        y = int(2 * (self.width + self.length))
        return (x, y)

    def get_width(self):
        self.width = int(input('Enter width:'))
        if self.width <= 0:
            raise ValueError('Invalid width.')

    def get_length(self):
        self.length = int(input('Enter length:'))
        if self.length <= 0:
            raise ValueError('Invalid length.')

    def __eq__(self, other):
        if self.width == other.width and self.length == other.length:
            return True
        else:
            return False


my_list = []
user_input = ''
while user_input != 'q':
    for i in range(2):
        try:
            rec1 = rectangle()
            rec1.get_width()
            rec1.get_length()
            v = rec1.get_value()
            my_list.append(rec1)
            print(rec1)
            print("Area:", v[0], "\nPerimeter:", v[1], "\n")

        except ValueError as excpt:
            print(excpt)
            print('Could not calculate rectangle value')
            user_input = input('Enter any key ("q" to quit\n)')
        user_input = 'q'


if my_list[0] == my_list[1]:
    print("\nThe two rectangles are the same")
else:
    print("\nThe two rectangles are not the same")
