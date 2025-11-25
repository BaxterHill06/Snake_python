#🐍
import random
pos = [[0, 0], [], [], [], []]
apPos = []
empAr = []
while True:

    grid = [["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "],["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "],["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "],["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "],["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "],["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "],["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "],["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "],["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "],["  ","  ","  ","  ","  ","  ","  ","  ","  ","  "]]

    for b in pos:
        try:
            y = b[0]
            x = b[1]
            grid[x][y] = "🐍"
        except:
            pass


    if apPos == []:
        xAp = random.randint(0,9)
        yAp = random.randint(0,9)
        apPos = [xAp,yAp]

        addApple = False
        while addApple == False:
            if grid[xAp][yAp] != "🐍":
                addApple = True

    grid[yAp][xAp] = "🍎"
    for i in range(len(grid)):
        print(grid[i])

    move = input(":")
    if move == "w":
        x = pos[0][0]
        y = pos[0][1]
        y -= 1
        direction = "n"
    elif move == "s":
        x = pos[0][0]
        y = pos[0][1]
        y += 1
        direction = "s"
    elif move == "a":
        x = pos[0][0]
        y = pos[0][1]
        x -= 1
        direction = "w"
    elif move == "d":
        x = pos[0][0]
        y = pos[0][1]
        x += 1
        direction = "e"
    else:
        if direction == "n":
            x = pos[0][0]
            y = pos[0][1]
            y -= 1
        elif direction == "e":
            x = pos[0][0]
            y = pos[0][1]
            x += 1
            direction = "e"
        elif direction == "s":
            x = pos[0][0]
            y = pos[0][1]
            y += 1
        elif direction == "w":
            x = pos[0][0]
            y = pos[0][1]
            x -= 1

    print(apPos, [x,y])
    if apPos == [x,y]:
        print("in")
        pos.append(empAr)
        apPos = []

    for a in range(len(pos)):
        print("1")
        a = len(pos) - a -1
        if a > 0:
            pos[a] = pos[a-1]
        else:
            if [x,y] in pos:
                print("END OF GAME")
                exit()
            if x < 0 or x > 9 or y < 0 or y > 9:
                print("END OF GAME")
                exit()
            else:
                pos[0] = [x,y]

    print(pos)