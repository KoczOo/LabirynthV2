import os, sys, curses, getch

q = 1

# Pozycja pionka(startowa)
heigth = 16
width = 3

# Pole gry
realrows=[]

for i in range (19):
    realrows.append([" "]*62)

board1 = [(0,0,60), (18,0,61), (0,0,18), (0,60,18), (14,0,40), (10,15,30), (2,25,13), (7,12,32), (3,15,30), (5,0,20), (8,3,18)]

#Funkcja rysujaca poziome sciany
def wall_horizontal(x,y,z):
    for i in range (z):
        length = i
        row = x
        column = y + i
        realrows[row][column] = "%"

#Funkcja rysujaca pionowe sciany
def wall_vertical(x,y,z):
    for i in range (z):
        length = i
        row = x + i
        column = y
        realrows[row][column] = "%"

# Funkcja odpowiadjaca za czyszczenie ekranu
def clear_screen():
        os.system('clear')


# Funkcja odpowiadajaca za ruch pionka
def move_player_in_direction(action,direction):
    clear_screen()
    global heigth
    global width
    realrows[heigth][width] = " "
    if action is "move" and direction is "right":
        width += 1
    elif action is "move" and direction is "left":
        width -= 1
    elif action is "move" and direction is "down":
        heigth += 1
    elif action is "move" and direction is "up":
        heigth -= 1
    if realrows[heigth][width] != "%":
        realrows[heigth][width] = "⛄"
    else:
        if action is "move" and direction is "right":
            width -= 1
        elif action is "move" and direction is "left":
            width += 1
        elif action is "move" and direction is "down":
            heigth -= 1
        elif action is "move" and direction is "up":
            heigth += 1
        realrows[heigth][width] = "⛄"

# Funkcja rysujaca plansze gry
def board(arg):
        wall_horizontal(*arg[0])
        wall_horizontal(*arg[1])
        wall_vertical(*arg[2])
        wall_vertical(*arg[3])
        wall_horizontal(*arg[4])
        wall_horizontal(*arg[5])
        wall_vertical(*arg[6])
        wall_horizontal(*arg[7])
        wall_horizontal(*arg[8])
        wall_horizontal(*arg[9])
        wall_horizontal(*arg[10])
        realrows[12][10] = "☯"
        for s in realrows:
                print(*s, sep = "")

# Funkcja zakonczenia gry
def game_over():
    clear_screen()
    print(
        """
         _____      ___       ___  ___   _______
        /  ___|    /   |     /   |/   | |   ____|
        | |       /    |    / /|   /| | |  |__
        | |  _   /  /| |   / / |__/ | | |   __|
        | |_| | /  ___ |  / /       | | |  |____
        \_____//_/   |_| /_/        |_| |_______|



         _____    __    __  ______   _____
        /  _  \  | |   / / | _____| |  _  |
        | | | |  | |  / /  | |__    | |_| |
        | | | |  | | / /   |  __|   |  _  /
        | |_| |  | |/ /    | |____  | | |
        \_____/  |___/     |______| |_|  \_

        """
    )


while q:
        user_input = getch.getch()
        user_input = user_input.lower()
        if user_input == "d":
            move_player_in_direction("move","right")
        if user_input == "a":
            move_player_in_direction("move", "left")
        if user_input == "w":
            move_player_in_direction("move", "up")
        if user_input == "s":
            move_player_in_direction("move", "down")
        if realrows[12][10] == "⛄":
            q = 0
            break

        else:
                clear_screen()

        board(board1)




if not q:
    game_over()











