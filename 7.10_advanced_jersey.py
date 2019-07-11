def jersey_and_rating(c):
    for i in range(1, 6):
        print("Enter player", i, "'s jersey number(0 - 99):")
        x = int(input())
        print("Enter player", i, "'s rating(1 - 9):")
        y = int(input())
        c.update({x: y})
    return c


def get_list(dict1):
    key_list = []
    for key in dict1.keys():
        key_list.append(key)
    return key_list


players = {}
players = jersey_and_rating(players)
player_list = get_list(players)
player_list = sorted(player_list)


def menu():
    print("\nMENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - quit")
    c = input("Choose an option:")
    return c


c = menu()

if c == 'o':
    print("\nROSTER:  \n")
    for a in player_list:
        print("Jersey number:", a, ", Rating:", players[a], " ")
    c = menu()

if c == 'q':
    print("\nOkay")
    print("Quitting...")
