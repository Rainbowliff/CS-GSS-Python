def jersey_and_rating(d):
    for i in range(1, 6):
        print("Enter player", i, "'s jersey number(0 - 99):")
        x = int(input())
        print("Enter player", i, "'s rating(1 - 9):")
        y = int(input())
        d.update({x: y})
    return d


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
    u = input("Choose an option:")
    return u


v = 0
c = menu()

while v != -1:

    if c == 'o':
        print("\nROSTER:  \n")
        for a in player_list:
            print("Jersey number:", a, ", Rating:", players[a], " ")
        c = menu()

    elif c == 'q':
        print("\nOkay")
        print("Quitting...")
        v = -1

    elif c == 'a':
        j = int(input("Enter the player's jersey number:"))
        ra = int(input("Enter player's rating:"))
        players.update({j: ra})
        player_list = get_list(players)
        player_list = sorted(player_list)
        c = menu()

    elif c == 'd':
        de_le = int(input("Enter the player's jersey number that you want to delete:"))
        del players[de_le]
        player_list = get_list(players)
        player_list = sorted(player_list)
        c = menu()

    elif c == 'u':
        up = int(input("Enter the player's jersey number:"))
        date = int(input("Update the player's rating:"))
        players.update({up: date})
        c = menu()

    elif c == 'r':
        limit = int(input("Please enter a rating:"))
        numbers_list = []
        for k in player_list:
            if players[k] > limit:
                numbers_list.append(k)
        numbers_list = sorted(numbers_list)
        for ar in numbers_list:
            print("Jersey number:", ar, ", Rating:", players[ar], " ")
        c = menu()
