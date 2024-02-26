# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
Main_Column = [1, 2, 3, 4, 5, 6, 7]
global rep1, rep2, rep3, rep4, rep5, rep6, rep7
rep1 = 0
rep2 = 0
rep3 = 0
rep4 = 0
rep5 = 0
rep6 = 0
rep7 = 0
mag = 0
player_one_and_player_two = [[], [], [], [], [], []]
player_one = [[], [], [], [], [], []]
player_two = [[], [], [], [], [], []]
Q = 0


def checker_input_player_one():
    global x
    print()
    while True:
        x = input("Player one, choose a number from the list: ")
        print()
        try:
            x = int(x)
            if x in Main_Column:
                break
            else:
                print(
                    "Invalid choice. The number is not valid.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def checker_input_player_two():
    global y
    print()
    while True:
        y = input("Player Two, choose a number from the list: ")
        print()
        try:
            y = int(y)
            if y in Main_Column:
                break
            else:
                print(
                    "Invalid choice. The number is not valid.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def connect_4_paly_board():
    print("   1       2      3      4      5      6      7")
    for i in range(7):
        print("=======" * 7 + "==")
        if i == 6:
            break
        m = "|"
        b = ""
        z = "      "
        print((m + z) * 8)
        print((m + z) * 8)
        print((m + z) * 8)


def how_to_print(mul):
    print("   1       2      3      4      5      6      7")
    for i in range(5, -1, -1):
        if len(player_one_and_player_two[i]) >= 1:
            pro = i + 1
            xox = i
            break
    mag = 0

    for i in range(7):
        print("=======" * 7 + "==")
        if i == 6:
            break
        m = "|"
        z = "      "
        R = "   X  "
        Nop = "   O  "
        dig = 0
        if i == (6 - pro):
            print((m + z) * 8)
            if len(player_one_and_player_two[xox]) >= 2:
                player_one_and_player_two[xox].sort()
                for i in player_one_and_player_two[xox]:
                    if i in player_one[xox]:
                        if i == player_one_and_player_two[xox][0]:
                            good = i - 1
                            print(((m + z) * (good)), end="")
                            print((m + R), end="")
                            mag += 1

                        else:
                            good = i - player_one_and_player_two[xox][dig] - 1
                            print(((m + z) * (good)), end="")
                            print((m + R), end="")
                            dig += 1
                            mag += 1
                    else:
                        if i == player_one_and_player_two[xox][0]:
                            good = i - 1
                            print(((m + z) * (good)), end="")
                            print((m + Nop), end="")
                            mag += 1
                        else:
                            good = i - player_one_and_player_two[xox][dig] - 1
                            print(((m + z) * (good)), end="")
                            print((m + Nop), end="")
                            dig += 1
                            mag += 1

                print((m + z) * (8 - player_one_and_player_two[xox][-1]))
                print((m + z) * 8)
                if Q > 0:
                    pro -= 1
                    xox -= 1
                continue
            else:
                print(((m + z) * (-1 + player_one_and_player_two[xox][0])), end="")
                if (player_one_and_player_two[xox][0]) in player_one[xox]:
                    print((m + R), end="")
                    print((m + z) * (8 - player_one[xox][0]))
                else:
                    print((m + Nop), end="")
                    print((m + z) * (8 - player_two[xox][0]))
            print((m + z) * 8)
            if Q > 0:
                pro -= 1
                xox -= 1
            continue
        print((m + z) * 8)
        print((m + z) * 8)
        print((m + z) * 8)


def win_checker_one():
    # H_W
    for i in range(6):
        if len(player_one[i]) >= 4:
            for j in range(len(player_one[i])):
                player_one[i].sort()
                try:
                    if (player_one[i][j] + 1) == (player_one[i][j + 1]):
                        if (player_one[i][j + 1] + 1) == (player_one[i][j + 2]):
                            if (player_one[i][j + 2] + 1) == (player_one[i][j + 3]):
                                print("Player one wins!")
                                quit()
                except IndexError:
                    continue
    # V_W
    for i in range(1, 8):
        for j in range(6):
            if j < 3:
                if (len(player_one[j]) > 0) and (i in player_one[j]):
                    if (len(player_one[j + 1]) > 0) and (i in player_one[j + 1]):
                        if (len(player_one[j + 2]) > 0) and (i in player_one[j + 2]):
                            if (len(player_one[j + 3]) > 0) and (i in player_one[j + 3]):
                                print("Player one wins!")
                                quit()
    # D_W
    for i in range(1, 8):
        for j in range(6):
            if j < 3:
                if i < 5:
                    if i in player_one[j]:
                        if (i + 1) in player_one[j + 1]:
                            if (i + 2) in player_one[j + 2]:
                                if (i + 3) in player_one[j + 3]:
                                    print("Player one wins!")
                                    quit()
        for j in range(5, -1, -1):
            if j >= 3:
                if i >= 4:
                    if i in player_one[j]:
                        if (i + 1) in player_one[j - 1]:
                            if (i + 2) in player_one[j - 2]:
                                if (i + 3) in player_one[j - 3]:
                                    print("Player one wins!")
                                    quit()


def win_checker_two():
    # H_w
    for i in range(6):
        if len(player_two[i]) >= 4:
            for j in range(len(player_two[i])):
                player_two[i].sort()
                try:
                    if (player_two[i][j] + 1) == (player_two[i][j + 1]):
                        if (player_two[i][j + 1] + 1) == (player_two[i][j + 2]):
                            if (player_two[i][j + 2] + 1) == (player_two[i][j + 3]):
                                print("Player Two wins!")
                                quit()
                except IndexError:
                    continue
    # V_W
    for i in range(1, 8):
        for j in range(6):
            if (len(player_two[j]) > 0) and (i in player_two[j]):
                if (len(player_two[j + 1]) > 0) and (i in player_two[j + 1]):
                    if (len(player_two[j + 2]) > 0) and (i in player_two[j + 2]):
                        if (len(player_two[j + 3]) > 0) and (i in player_two[j + 3]):
                            print("Player two wins!")
                            quit()
    # D_W
    for i in range(1, 8):
        for j in range(6):
            if j < 3:
                if i < 5:
                    if i in player_two[j]:
                        if (i + 1) in player_two[j + 1]:
                            if (i + 2) in player_two[j + 2]:
                                if (i + 3) in player_two[j + 3]:
                                    print("Player two wins!")
                                    quit()
        for j in range(5, -1, -1):
            if j >= 3:
                if i >= 4:
                    if i in player_two[j]:
                        if (i + 1) in player_two[j - 1]:
                            if (i + 2) in player_two[j - 2]:
                                if (i + 3) in player_two[j - 3]:
                                    print("Player two wins!")
                                    quit()


def player_one_reco(u1, inp):
    global Q
    if u1 == 1:
        rpg = 0
        player_one_and_player_two[rpg].append(inp)
        if inp == x:
            player_one[rpg].append(inp)
        else:
            player_two[rpg].append(inp)
        how_to_print(inp)
    else:
        if u1 < 7:
            Q = u1 - 1
            player_one_and_player_two[Q].append(inp)
            if inp == x:
                player_one[Q].append(inp)
            else:
                player_two[Q].append(inp)
            how_to_print(inp)
        else:
            pass


connect_4_paly_board()
while True:
    checker_input_player_one()
    if x == 1:
        rep1 += 1
        player_one_reco(rep1, x)
        x = 0
    elif x == 2:
        rep2 += 1
        player_one_reco(rep2, x)
        x = 0

    elif x == 3:
        rep3 += 1
        player_one_reco(rep3, x)
        x = 0

    elif x == 4:
        rep4 += 1
        player_one_reco(rep4, x)
        x = 0

    elif x == 5:
        rep5 += 1
        player_one_reco(rep5, x)
        x = 0

    elif x == 6:
        rep6 += 1
        player_one_reco(rep6, x)
        x = 0

    elif x == 7:
        rep7 += 1
        player_one_reco(rep7, x)
        x = 0
    win_checker_one()
    checker_input_player_two()
    if y == 1:
        rep1 += 1
        player_one_reco(rep1, y)
        y = 0

    elif y == 2:
        rep2 += 1
        player_one_reco(rep2, y)
        y = 0

    elif y == 3:
        rep3 += 1
        player_one_reco(rep3, y)
        y = 0

    elif y == 4:
        rep4 += 1
        player_one_reco(rep4, y)
        y = 0

    elif y == 5:
        rep5 += 1
        player_one_reco(rep5, y)
        y = 0

    elif y == 6:
        rep6 += 1
        player_one_reco(rep6, y)
        y = 0

    elif y == 7:
        rep7 += 1
        player_one_reco(rep7, y)
        y = 0
    win_checker_two()