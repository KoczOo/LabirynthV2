import os, sys, curses, getch

q = 0

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

#pole gry

realrows = [row1, row2, row3, row4, row5, row6, row7, row8, row9, row10, row11, row12, row13, row14, row15, row16, row17, row18, row19]

#poziome sciany
def wall_hor(x,y,z):
    for i in range (z):
        length = i
        row = x
        column = y + i
        realrows[row][column] = "%"

#pionowe sciany
def wall_vert(x,y,z):
    for i in range (z):
        length = i
        row = x + i
        column = y
        realrows[row][column] = "%"



# Pozycja pionka
heigth = 16
width = 3

def clr():
        os.system('clear')


def board():
        wall_hor(0,0,30)
        wall_hor(18,0,31)
        wall_vert(0,0,18)
        wall_vert(0,30,18)
        wall_hor(14,0,20)
        wall_hor(10,15,15)
        wall_vert(2,12,13)
        wall_hor(7,12,16)
        wall_hor(3,15,15)
        wall_hor(5,0,10)
        wall_hor(8,3,9)
        realrows[12][10] = "0"
        for s in realrows:
                print(*s)


def game_over():
    clr()
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


while q == 0:
        user_input = getch.getch()
        user_input = user_input.lower()
        if user_input == "d":
                clr()
                realrows[heigth][width] = " "
                width += 1
                realrows[heigth][width] = "#"


        if user_input == "a":
                clr()
                realrows[heigth][width] = " "
                width -= 1
                realrows[heigth][width] = "#"


        if user_input == "w":
                clr()
                realrows[heigth][width] = " "
                heigth -= 1
                realrows[heigth][width] = "#"


        if user_input == "s":
                clr()
                realrows[heigth][width] = " "
                heigth += 1
                realrows[heigth][width] = "#"

        if realrows[12][10] == "#":
            q += 1
            break

        else:
                clr()

        board()



if q == 1:
    game_over()













