#🐍
import random
import keyboard
import time
from tkinter import *
import PIL
from PIL import Image, ImageTk
import threading

window = Tk()
frame = Frame(background="blue")

refresh = False

def LoadImage():
    global imgBody, imgHead, imgEmpty, imgApple
    imgBody = PhotoImage(file="skin.png")
    imgHead = PhotoImage(file="head.png")
    imgEmpty = PhotoImage(file="empty.png")
    imgApple = PhotoImage(file="apple.png")



def Run():
    global grid, frame, frameTemp, refresh
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
        LoadImage()
        #frameTemp = frame
        #frame.pack_forget()
        #frameTemp.pack()
        #Create()
        #frameTemp.pack_forget()
        frame.pack()
        refresh = True
        time.sleep(.3)
        print("main1")
        loops = 0
        movement = True
        print("main2")
        while movement == True:
            print("main3")
            if keyboard.is_pressed("w") and direction != "s":
                print("main w")
                """
                x = pos[0][0]
                y = pos[0][1]
                y -= 1
                """
                direction = "n"
                movement = False
            print("main3.11")
            if keyboard.is_pressed("s") and direction != "n":
                """
                x = pos[0][0]
                y = pos[0][1]
                y += 1
                """
                direction = "s"
                movement = False
            print("main3.12")
            if keyboard.is_pressed("a") and direction != "e":
                """
                x = pos[0][0]
                y = pos[0][1]
                x -= 1
                """
                direction = "w"
                movement = False
            print("main1.13")
            if keyboard.is_pressed("d") and direction != "w":
                """
                x = pos[0][0]
                y = pos[0][1]
                x += 1
                """
                direction = "e"
                movement = False
            print("main1.14")
            if loops > speed or movement == False:
                print("main3.25")
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
                print("main3.5")
                time.sleep(.1)
            loops += 1
            print("main4")
        print("main5")

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


def row0(x):
    global refresh, imgEmpty, imgBody, imgHead, imgApple, frame
    while True:
        time.sleep(.05)
        refresh0 = refresh
        if refresh0 == True:
            for y in range(10):
                lblBlank = Label(frame, image=imgEmpty)
                lblBody = Label(frame, image=imgBody)
                lblHead = Label(frame, image=imgHead)
                lblApple = Label(frame, image=imgApple)
                SetFeild(lblBlank, lblBody, lblHead, lblApple, x, y)
                refresh = False

def row1(x):
    global refresh, imgEmpty, imgBody, imgHead, imgApple, frame
    while True:
        time.sleep(.05)
        refresh1 = refresh
        if refresh1 == True:
            for y in range(10):
                lblBlank = Label(frame, image=imgEmpty)
                lblBody = Label(frame, image=imgBody)
                lblHead = Label(frame, image=imgHead)
                lblApple = Label(frame, image=imgApple)
                SetFeild(lblBlank, lblBody, lblHead, lblApple, x, y)

def row2(x):
    global refresh, imgEmpty, imgBody, imgHead, imgApple, frame
    while True:
        time.sleep(.05)
        refresh2 = refresh
        if refresh2 == True:
            for y in range(10):
                lblBlank = Label(frame, image=imgEmpty)
                lblBody = Label(frame, image=imgBody)
                lblHead = Label(frame, image=imgHead)
                lblApple = Label(frame, image=imgApple)
                SetFeild(lblBlank, lblBody, lblHead, lblApple, x, y)

def row3(x):
    global refresh, imgEmpty, imgBody, imgHead, imgApple, frame
    while True:
        time.sleep(.05)
        refresh3 = refresh
        if refresh3 == True:
            for y in range(10):
                lblBlank = Label(frame, image=imgEmpty)
                lblBody = Label(frame, image=imgBody)
                lblHead = Label(frame, image=imgHead)
                lblApple = Label(frame, image=imgApple)
                SetFeild(lblBlank, lblBody, lblHead, lblApple, x, y)

def row4(x):
    global refresh, imgEmpty, imgBody, imgHead, imgApple, frame
    while True:
        time.sleep(.05)
        refresh4 = refresh
        if refresh4 == True:
            for y in range(10):
                lblBlank = Label(frame, image=imgEmpty)
                lblBody = Label(frame, image=imgBody)
                lblHead = Label(frame, image=imgHead)
                lblApple = Label(frame, image=imgApple)
                SetFeild(lblBlank, lblBody, lblHead, lblApple, x, y)

def row5(x):
    global refresh, imgEmpty, imgBody, imgHead, imgApple, frame
    while True:
        time.sleep(.05)
        refresh5 = refresh
        if refresh5 == True:
            for y in range(10):
                lblBlank = Label(frame, image=imgEmpty)
                lblBody = Label(frame, image=imgBody)
                lblHead = Label(frame, image=imgHead)
                lblApple = Label(frame, image=imgApple)
                SetFeild(lblBlank, lblBody, lblHead, lblApple, x, y)

def row6(x):
    global refresh, imgEmpty, imgBody, imgHead, imgApple, frame
    while True:
        time.sleep(.05)
        refresh6 = refresh
        if refresh6 == True:
            for y in range(10):
                lblBlank = Label(frame, image=imgEmpty)
                lblBody = Label(frame, image=imgBody)
                lblHead = Label(frame, image=imgHead)
                lblApple = Label(frame, image=imgApple)
                SetFeild(lblBlank, lblBody, lblHead, lblApple, x, y)


def row7(x):
    global refresh, imgEmpty, imgBody, imgHead, imgApple, frame
    while True:
        time.sleep(.05)
        refresh7 = refresh
        if refresh7 == True:
            for y in range(10):
                lblBlank = Label(frame, image=imgEmpty)
                lblBody = Label(frame, image=imgBody)
                lblHead = Label(frame, image=imgHead)
                lblApple = Label(frame, image=imgApple)
                SetFeild(lblBlank, lblBody, lblHead, lblApple, x, y)

def row8(x):
    global refresh, imgEmpty, imgBody, imgHead, imgApple, frame
    while True:
        time.sleep(.05)
        refresh8 = refresh
        if refresh8 == True:
            for y in range(10):
                lblBlank = Label(frame, image=imgEmpty)
                lblBody = Label(frame, image=imgBody)
                lblHead = Label(frame, image=imgHead)
                lblApple = Label(frame, image=imgApple)
                SetFeild(lblBlank, lblBody, lblHead, lblApple, x, y)

def row9(x):
    global refresh, imgEmpty, imgBody, imgHead, imgApple, frame
    while True:
        time.sleep(.05)
        refresh9 = refresh
        if refresh9 == True:
            for y in range(10):
                lblBlank = Label(frame, image=imgEmpty)
                lblBody = Label(frame, image=imgBody)
                lblHead = Label(frame, image=imgHead)
                lblApple = Label(frame, image=imgApple)
                SetFeild(lblBlank, lblBody, lblHead, lblApple, x, y)


def Create():
    global imgEmpty, imgBody, imgHead, imgApple, frame
    print("remove me later maybe")

def SetFeild(lblBlank, lblBody, lblHead, lblApple,x,y):
    global imgEmpty, imgBody, imgHead, imgApple, grid
    print("refresh")
    if grid[x][y] == "⬜":
        lblBlank.grid(row=x,column=y)
    elif grid[x][y] == "🟩":
        lblBody.grid(row=x,column=y)
    elif grid[x][y] == "⬛":
        lblHead.grid(row=x,column=y)
    elif grid[x][y] == "🍎":
        lblApple.grid(row=x,column=y)


def Window():
    global window
    window.mainloop()


if __name__ == "__main__":
    t1 = threading.Thread(target=Run)
    #t2 = threading.Thread(target=Window)

    t1.start()
    #t2.start()


if __name__ == "__main__":
    tx1 = threading.Thread(target=row0, args=(0,))
    tx2 = threading.Thread(target=row1, args=(1,))
    tx3 = threading.Thread(target=row2, args=(2,))
    tx4 = threading.Thread(target=row3, args=(3,))
    tx5 = threading.Thread(target=row4, args=(4,))
    tx6 = threading.Thread(target=row5, args=(5,))
    tx7 = threading.Thread(target=row6, args=(6,))
    tx8 = threading.Thread(target=row7, args=(7,))
    tx9 = threading.Thread(target=row8, args=(8,))
    tx10 = threading.Thread(target=row9, args=(9,))

    tx1.start()
    tx2.start()
    tx3.start()
    tx4.start()
    tx5.start()
    tx6.start()
    tx7.start()
    tx8.start()
    tx9.start()
    tx10.start()

window.mainloop()