class rectangle:

    def __init__(self):
        self.width = 0
        self.length = 0
        self.value = ()

    def __str__(self):
        return "\nThis is a rectangle.\n\nWidth:%d\nLength:%d\nArea:%d\nPerimeter:%d" % \
               (self.width, self.length, self.value[0], self.value[1])

    def get_value(self):
        x = self.width * self.length
        y = 2 * (self.width + self.length)
        self.value = (x, y)

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
            rec1.get_value()
            my_list.append(rec1)
            print(rec1)

        except ValueError as excpt:
            print(excpt)
            print('Could not calculate rectangle value')
            user_input = input('Enter any key ("q" to quit\n)')
        user_input = 'q'


if my_list[0] == my_list[1]:
    print("\nThe two rectangles are the same")
else:
    print("\nThe two rectangles are not the same")