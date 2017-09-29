import turtle as t

#t.Screen()
t.speed(1)
t.pu()

# Draw a box with dimensions 120x160px with vertical divisions every 40px
def box(size):
    # Setup
    t.pd()
    x = 90
    t.fd(size * 60)
    # Draw the box
    for i in range(2):
        t.lt(x)
        t.fd(size * 120)
        t.lt(x)
        t.fd(size * 120)
    t.lt(x)
    # Draw each horizontal 40px
    t.fd(size * 40)
    t.lt(x)
    t.fd(size * 120)
    t.rt(x)
    t.fd(size * 40)
    t.rt(x)
    t.fd(size * 120)
    t.lt(x)
    t.bk(80)
    t.rt(90)
    t.bk(60)
    # Reset the pen
    t.pu()


def drawSpace():
    t.rt(360)


def drawA(size):
    # Draws an uppercase A
    a = 26.565
    x = 134.164
    # Setup
    t.pu()
    t.bk(size * 60)
    # Draw first leg
    t.pd()
    t.lt(90 - a)
    t.fd(size * x)
    # Draw second leg
    t.rt(180 - 2 * a)
    t.fd(size * x)
    # Draw center stem
    t.rt(180)
    t.fd(size * (x / 3))
    t.lt(90 - a)
    t.fd(size * 80)
    # Reset from A
    t.pu()
    t.lt(180)
    t.fd(size * 40)
    t.rt(90)
    t.fd(size * 40)
    t.lt(90)


def drawB(size):
    # Draws an uppercase B
    # Draw low horizontal stem
    t.pd()
    t.lt(180)
    t.fd(size * 60)
    # Draw vertical stem
    t.rt(90)
    t.fd(size * 120)
    # Draw high horizontal stem
    t.rt(90)
    t.fd(size * 60)
    # Draw the upper hump
    for i in range(180):
        t.fd(size * 0.524)
        t.rt(1)
    # Draw the lowerhump
    t.rt(180)
    for i in range(180):
        t.fd(size * 0.524)
        t.rt(1)
    # Finalize
    t.rt(180)
    t.pu()


def drawC(size):
    # draws uppercase C
    # go to center right
    t.fd(size * 60)
    t.lt(90)
    t.fd(size * 60)
    t.rt(180)
    # Draw c
    for i in range(360):
        if i < 45 or i > 315:
            t.pu()
        else:
            t.pd()
        t.fd(size * 1.048)
        t.rt(1)
    # finalize
    t.fd(size * 60)
    t.lt(90)
    t.bk(60)


def drawD(size):
    # Draws an uppercase D
    # Go to bottom corner
    t.bk(60)
    # Draw stem of D
    t.lt(90)
    t.pd()
    t.fd(size * 120)
    # Draw D
    t.rt(90)
    t.fd(size * 60)
    for i in range(180):
        t.fd(size * 1.047)
        t.rt(1)
    t.fd(size * 60)
    # Finalize
    t.rt(180)
    t.fd(size * 60)


def drawE(size):
    # Draws an uppercase E
    # Draw bottom stem
    t.pd()
    t.fd(size * 60)
    t.bk(120)
    # Draw middle stem
    t.lt(90)
    t.fd(size * 60)
    t.rt(90)
    t.fd(size * 120)
    t.bk(120)
    # Draw top stem
    t.lt(90)
    t.fd(size * 60)
    t.rt(90)
    t.fd(size * 120)
    # Finalize
    t.pu()
    t.bk(60)
    t.rt(90)
    t.fd(size * 120)
    t.lt(90)


def drawF(size):
    # Draws an uppercase F
    # Go to initial point
    t.bk(size * 60)
    # Draw first stem
    t.pd()
    t.lt(90)
    t.fd(size * 60)
    t.rt(90)
    t.fd(size * 120)
    t.bk(size * 120)
    # Draw top stem
    t.lt(90)
    t.fd(size * 60)
    t.rt(90)
    t.fd(size * 120)
    # Finalize
    t.pu()
    t.bk(size * 60)
    t.rt(90)
    t.fd(size * 120)
    t.lt(90)


def drawG(size):
    # Draws an uppercase G
    # Go to initial point
    t.fd(size * 60)
    t.lt(90)
    t.fd(size * 120)
    t.lt(90)
    # Draw the circle
    t.pd()
    t.fd(size * 60)
    for i in range(270):
        t.fd(size * 1.048)
        t.lt(1)
    # Draw stem
    t.lt(90)
    t.fd(size * 60)
    # Finalize
    t.pu()
    t.lt(90)
    t.fd(size * 60)
    t.lt(size * 90)


def drawH(size):
    # Draws an uppercase H
    # Go to initial point
    t.bk(size * 60)
    t.lt(90)
    # Draw first vertical
    t.pd()
    t.fd(size * 120)
    t.bk(size * 60)
    # Draw center
    t.rt(90)
    t.fd(size * 120)
    # Draw second vertical
    t.lt(90)
    t.fd(size * 60)
    t.bk(size * 120)
    # Finalize
    t.pu()
    t.rt(90)
    t.bk(size * 60)
    t.rt(180)


def drawI(size):
    # You get the pattern
    # Draw first horizontal
    t.pd()
    t.fd(size * 60)
    t.bk(size * 120)
    t.fd(size * 60)
    # Draw center
    t.rt(90)
    t.fd(size * 120)
    # Draw second horizontal
    t.lt(90)
    t.fd(size * 60)
    t.bk(size * 120)
    # Finalize
    t.pu()
    t.fd(size * 60)


def drawJ(size):
    # go to initial point
    t.bk(size * 60)
    t.lt(90)
    t.fd(size * 120)
    t.rt(90)
    # draw the straight parts
    t.pd()
    t.fd(size * 120)
    t.rt(90)
    t.fd(size * 60)
    # draw the curve
    for i in range(180):
        t.fd(size * 1.048)
        t.rt(1)
    # finalize
    t.pu()
    t.bk(size * 60)
    t.rt(90)
    t.fd(size * 60)


def drawK(size):
    x = 26.565
    d = 134.164
    # go to initial
    t.fd(size * 60)
    # draw diagonals
    t.pd()
    t.rt(180 + x)
    t.fd(size * d)
    t.rt(180 - 2 * x)
    t.fd(size * d)
    # get to stem
    t.lt(180)
    t.fd(size * d)
    t.lt(90 - x)
    t.fd(size * 60)
    t.bk(size * 120)
    # finalize
    t.pu()
    t.fd(size * 120)
    t.lt(90)
    t.fd(size * 60)


def drawL(size):
    # draw bottom stem
    t.pd()
    t.fd(size * 60)
    t.bk(size * 120)
    # draw vertical stem
    t.lt(90)
    t.fd(size * 120)
    # finalize
    t.bk(size * 120)
    t.rt(90)
    t.fd(size * 60)
    t.pu()


def drawM(size):
    x = 72.111
    b = 33.69
    # go to initial
    t.bk(size * 60)
    t.pd()
    # draw left stem
    t.lt(90)
    t.fd(size * 120)
    # draw center stem 1
    t.rt(90 + b)
    t.fd(size * x)
    # draw center stem 2
    t.lt(2 * b)
    t.fd(size * x)
    # draw right stem
    t.rt(b + 90)
    t.fd(size * 120)
    # finalize
    t.pu()
    t.lt(90)
    t.bk(size * 60)


def drawN(size):
    x = 169.706
    # go to initial
    t.bk(size * 60)
    # draw first stem
    t.pd()
    t.lt(90)
    t.fd(size * 120)
    # draw center stem
    t.rt(90 + 45)
    t.fd(size * x)
    # draw final stem
    t.lt(90 + 45)
    t.fd(size * 120)
    # finalize
    t.pu()
    t.bk(size * 120)
    t.rt(90)
    t.bk(size * 60)


def drawO(size):
    # draw o
    t.pd()
    for i in range(360):
        t.fd(size * 1.048)
        t.lt(1)
    t.pu()


def drawP(size):
    # Draws an uppercase B
    # Draw low horizontal stem
    t.lt(180)
    t.fd(size * 60)
    # Draw vertical stem
    t.pd()
    t.rt(90)
    t.fd(size * 120)
    # Draw high horizontal stem
    t.rt(90)
    t.fd(size * 60)
    # Draw the upper hump
    for i in range(180):
        t.fd(size * 0.524)
        t.rt(1)
    t.fd(size * 60)
    # finalize
    t.pu()
    t.lt(90)
    t.fd(size * 60)
    t.lt(90)
    t.fd(size * 60)


def drawQ(size):
    x = 84.853
    # draw o
    t.pd()
    for i in range(360):
        t.fd(size * 1.048)
        t.lt(1)
    # draw stem
    t.pu()
    t.fd(size * 60)
    t.pd()
    t.lt(180 - 45)
    t.fd(size * x)
    # finalize
    t.pu()
    t.rt(45)
    t.bk(size * 60)
    t.rt(90)


def drawR(size):
    x = 84.853
    # go to initial
    t.lt(180)
    t.fd(size * 60)
    # Draw vertical stem
    t.pd()
    t.rt(90)
    t.fd(size * 120)
    # Draw high horizontal stem
    t.rt(90)
    t.fd(size * 30)
    # Draw the hump
    for i in range(180):
        t.fd(size * 0.524)
        t.rt(1)
    t.fd(size * 30)
    # draw the diagonal stem
    t.rt(180)
    t.rt(45)
    t.fd(size * x)
    # finalize
    t.pu()
    t.lt(45)


def drawS(size):
    x = 0.524
    # initial position
    t.fd(size * 60)
    t.lt(90)
    t.fd(size * 120)
    t.fd(size * 30)
    t.pd()
    # draw top bar
    t.lt(90)
    t.fd(size * 30)
    # draw first hump
    for i in range(180):
        t.fd(size * x)
        t.lt(1)
    # draw second hump
    for i in range(180):
        t.fd(size * x)
        t.rt(1)
    t.fd(size * 30)
    # finalize
    t.pu()
    t.rt(180)
    t.fd(size * 30)
    


def drawT(size):
    # draw t
    t.pd()
    t.lt(90)
    t.fd(size * 120)
    t.rt(90)
    t.fd(size * 60)
    t.bk(size * 120)
    # finalize
    t.pu()
    t.fd(size * 60)
    t.rt(90)
    t.fd(size * 120)
    t.lt(90)


def drawU(size):
    x = 1.048
    # go to initial
    t.bk(size * 60)
    t.rt(90)
    t.bk(size * 60)
    # draw vertical stem
    t.pd()
    t.bk(size * 60)
    # draw curve
    t.fd(size * 60)
    for i in range(180):
        t.fd(size * x)
        t.lt(1)
    # draw vertical stem
    t.fd(size * 60)
    # finalize
    t.pu()
    t.bk(size * 120)
    t.rt(90)
    t.bk(size * 60)


def drawV(size):
    # Draws an uppercase A
    a = 26.565
    d = 134.164
    # Draw first leg
    t.pd()
    t.lt(90 - a)
    t.fd(size * d)
    # Draw second leg
    t.lt(180)
    t.fd(size * d)
    # Draw center stem
    t.rt(180 - 2 * a)
    t.fd(size * d)
    # finalize
    t.pu()
    t.rt(180)
    t.fd(size * d)
    t.rt(a - 90)

def drawW():
    print('Sam')

def drawX():
    print('Sam')

def drawY():
    print('Sam')

def drawZ():
    print('Sam')


def Draw(size, letter):
    let = str(letter)
    if (ord(let) < 65 or ord(let) >90) and ord(let) != 32:
        print("That is not a valid letter")
    else:
        if let == "A":
            drawA(size)
        if let == "B":
            drawB(size)
        if let == "C":
            drawC(size)
        if let == "D":
            drawD(size)
        if let == "E":
            drawE(size)
        if let == "F":
            drawF(size)
        if let == "G":
            drawG(size)
        if let == "H":
            drawH(size)
        if let == "I":
            drawI(size)
        if let == "J":
            drawJ(size)
        if let == "K":
            drawK(size)
        if let == "L":
            drawL(size)
        if let == "M":
            drawM(size)
        if let == "N":
            drawN(size)
        if let == "O":
            drawO(size)
        if let == "P":
            drawP(size)
        if let == "Q":
            drawQ(size)
        if let == "R":
            drawR(size)
        if let == "S":
            drawS(size)
        if let == "T":
            drawT(size)
        if let == "U":
            drawU(size)
        if let == "V":
            drawV(size)
        if let == "W":
            drawW(size)
        if let == "X":
            drawX(size)
        if let == "Y":
            drawY(size)
        if let == "Z":
            drawZ(size)
        if let == ' ':
            drawSpace()
