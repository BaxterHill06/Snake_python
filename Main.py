#🐍
import random
import keyboard
import time

pos = [[4, 4], [], [], [], []]
apPos = []
empAr = []
direction = "n"
score = 0
speed = 8000
while True:
    print("\n\n\n\n\n", score)
    grid = [["⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜"],["⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜"],["⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜"],["⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜"],["⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜"],["⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜"],["⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜"],["⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜"],["⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜"],["⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜"]]

    for b in range(len(pos)):
        try:
            if b == 0:
                y = pos[b][0]
                x = pos[b][1]
                grid[x][y] = "⬛"
            else:
                y = pos[b][0]
                x = pos[b][1]
                grid[x][y] = "🟩"
        except:
            pass


    if apPos == []:

        addApple = False
        while addApple == False:
            xAp = random.randint(0, 9)
            yAp = random.randint(0, 9)
            apPos = [xAp, yAp]

            if grid[yAp][xAp] != "🟩" and grid[yAp][xAp] != "🍎" and grid[yAp][xAp] != "⬛":
                addApple = True

    grid[yAp][xAp] = "🍎"
    for i in range(len(grid)):
        print(grid[i])
    time.sleep(.15)

    loops = 0
    movement = True
    while movement == True:
        if keyboard.is_pressed("w"):
            """
            x = pos[0][0]
            y = pos[0][1]
            y -= 1
            """
            direction = "n"
            movement = False
        if keyboard.is_pressed("s"):
            """
            x = pos[0][0]
            y = pos[0][1]
            y += 1
            """
            direction = "s"
            movement = False
        if keyboard.is_pressed("a"):
            """
            x = pos[0][0]
            y = pos[0][1]
            x -= 1
            """
            direction = "w"
            movement = False
        if keyboard.is_pressed("d"):
            """
            x = pos[0][0]
            y = pos[0][1]
            x += 1
            """
            direction = "e"
            movement = False
        if loops > speed or movement == False:
            print("3")
            if direction == "n":
                x = pos[0][0]
                y = pos[0][1]
                y -= 1
                movement = False
            if direction == "e":
                x = pos[0][0]
                y = pos[0][1]
                x += 1
                movement = False
            if direction == "s":
                x = pos[0][0]
                y = pos[0][1]
                y += 1
                movement = False
            if direction == "w":
                x = pos[0][0]
                y = pos[0][1]
                x -= 1
                movement = False
            print("4")
            time.sleep(.1)
        loops += 1



    if apPos == [x,y]:
        pos.append(empAr)
        apPos = []
        score += 1
        speed -= 200

    for a in range(len(pos)):
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
