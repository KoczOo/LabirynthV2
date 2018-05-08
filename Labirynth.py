import os, sys, curses, getch

q = 1

# Pozycja pionka(startowa)
heigth = 16
width = 3

row1 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ']
row2 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ']
row3 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ']
row4 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ']
row5 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ']
row6 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ']
row7 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ']
row8 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ']
row9 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ']
row10 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ']
row11 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ']
row12 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ']
row13 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ']
row14 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ']
row15 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ']
row16 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ']
row17 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ']
row18 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ']
row19 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ']

# Pole gry

realrows = [row1, row2, row3, row4, row5, row6, row7, row8, row9, row10, row11, row12, row13, row14, row15, row16, row17, row18, row19]

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
def move_player_in_direction(x,y):
    clear_screen()
    global heigth
    global width
    realrows[heigth][width] = " "
    if x is "move" and y is "right":
        width += 1
    elif x is "move" and y is "left":
        width -= 1
    elif x is "move" and y is "down":
        heigth += 1
    elif x is "move" and y is "up":
        heigth -= 1
    realrows[heigth][width] = "#"`

# Funkcja rysujaca plansze gry
def board():
        wall_horizontal(0,0,30)
        wall_horizontal(18,0,31)
        wall_vertical(0,0,18)
        wall_vertical(0,30,18)
        wall_horizontal(14,0,20)
        wall_horizontal(10,15,15)
        wall_vertical(2,12,13)
        wall_horizontal(7,12,16)
        wall_horizontal(3,15,15)
        wall_horizontal(5,0,10)
        wall_horizontal(8,3,9)
        realrows[12][10] = "0"
        for s in realrows:
                print(*s)

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
        if realrows[12][10] == "#":
            q = 0
            break

        else:
                clear_screen()

        board()




if not q:
    game_over()











