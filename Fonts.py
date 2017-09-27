import turtle as t
t.Screen()
t.speed(1)
t.pu()

#Draw a box with dimensions 120x160px with vertical divisions every 40px
def box():
        #Setup
        t.reset()
        x = 90
        t.fd(60)
        t.rt(x)
        t.fd(40)
        #Draw the box
        for i in range(2):
                t.rt(x)
                t.fd(120)
                t.rt(x)
                t.fd(160)
        t.rt(180)
        #Draw each horizontal 40px
        for i in range(2):
                t.fd(40)
                t.lt(x)
                t.fd(120)
                t.rt(x)
                t.fd(40)
                t.rt(x)
                t.fd(120)
                t.lt(x)
        #Reset the pen
        t.pu()
        t.setx(0)
        t.sety(0)
        t.rt(x)


def drawA():
        #Draws an uppercase A
        x = 26.565
        d = 134.164
        #Setup
        t.pu()
        t.lt(180)
        t.fd(60)
        #Draw first leg
        t.pd()
        t.rt(180)
        t.lt(90-x)
        t.fd(d)
        #Draw second leg
        t.rt(180-2*x)
        t.fd(d)
        #Draw center stem
        t.rt(180)
        t.fd(d/3)
        t.lt(90-x)
        t.fd(80)
        #Reset from A
        t.pu()
        t.lt(180)
        t.fd(40)
        t.rt(90)
        t.fd(40)
        t.lt(90)


def drawB():
        #Draws an uppercase B
        #Draw low horizontal stem
        t.pd()
        t.lt(180)
        t.fd(60)
        #Draw vertical stem
        t.rt(90)
        t.fd(120)
        #Draw high horizontal stem
        t.rt(90)
        t.fd(60)
        #Draw the upper hump
        for i in range(180):
                t.fd(0.524)
                t.rt(1)
        #Draw the lowerhump
        t.rt(180)
        for i in range(180):
                t.fd(0.524)
                t.rt(1)
        #Finalize
        t.rt(180)
        t.pu()


def drawC():
    #draws uppercase C
    #go to center right
    t.fd(60)
    t.lt(90)
    t.fd(60)
    t.rt(180)
    #Draw c
    for i in range(360):
        if i < 45 or i > 315:
            t.pu()
        else:
            t.pd()
        t.fd(1.048)
        t.rt(1)
    #finalize
    t.fd(60)
    t.lt(90)
    t.bk(60)


def drawD():
        #Draws an uppercase D
        #Go to bottom corner
        t.bk(60)
        #Draw stem of D
        t.lt(90)
        t.pd()
        t.fd(120)
        #Draw D
        t.rt(90)
        t.fd(60)
        for i in range(180):
                t.fd(1.047)
                t.rt(1)
        t.fd(60)
        #Finalize
        t.rt(180)
        t.fd(60)


def drawE():
    #Draws an uppercase E
    #Draw bottom stem
    t.pd()
    t.fd(60)
    t.bk(120)
    #Draw middle stem
    t.lt(90)
    t.fd(60)
    t.rt(90)
    t.fd(120)
    t.bk(120)
    #Draw top stem
    t.lt(90)
    t.fd(60)
    t.rt(90)
    t.fd(120)
    #Finalize
    t.pu()
    t.bk(60)
    t.rt(90)
    t.fd(120)
    t.lt(90)


def drawF():
    #Draws an uppercase F
    #Go to initial point
    t.bk(60)
    #Draw first stem
    t.pd()
    t.lt(90)
    t.fd(60)
    t.rt(90)
    t.fd(120)
    t.bk(120)
    #Draw top stem
    t.lt(90)
    t.fd(60)
    t.rt(90)
    t.fd(120)
    #Finalize
    t.pu()
    t.bk(60)
    t.rt(90)
    t.fd(120)
    t.lt(90)


def drawG():
    #Draws an uppercase G
    #Go to initial point
    t.fd(60)
    t.lt(90)
    t.fd(120)
    t.lt(90)
    #Draw the circle
    t.pd()
    t.fd(60)
    for i in range(270):
        t.fd(1.048)
        t.lt(1)
    #Draw stem
    t.lt(90)
    t.fd(60)
    #Finalize
    t.pu()
    t.lt(90)
    t.fd(60)
    t.lt(90)


def drawH():
    #Draws an uppercase H
    #Go to initial point
    t.bk(60)
    t.lt(90)
    #Draw first vertical
    t.pd()
    t.fd(120)
    t.bk(60)
    #Draw center
    t.rt(90)
    t.fd(120)
    #Draw second vertical
    t.lt(90)
    t.fd(60)
    t.bk(120)
    #Finalize
    t.pu()
    t.rt(90)
    t.bk(60)


def drawI():
    #You get the pattern
    #Draw first horizontal
    t.pd()
    t.fd(60)
    t.bk(120)
    t.fd(60)
    #Draw center
    t.rt(90)
    t.fd(120)
    #Draw second horizontal
    t.lt(90)
    t.fd(60)
    t.bk(120)
    #Finalize
    t.pu()
    t.fd(60)


def drawJ():
    #go to initial point
    t.bk(60)
    t.lt(90)
    t.fd(120)
    t.rt(90)
    #draw the straight parts
    t.pd()
    t.fd(120)
    t.rt(90)
    t.fd(60)
    #draw the curve
    for i in range(180):
        t.fd(1.048)
        t.rt(1)
    #finalize
    t.pu()
    t.bk(60)
    t.rt(90)
    t.fd(60)
    

def drawK():
    x = 26.565
    d = 134.164
    #go to initial
    t.fd(60)
    #draw diagonals
    t.pd()
    t.rt(180+x)
    t.fd(d)
    t.rt(180-2*x)
    t.fd(d)
    #get to stem
    t.lt(180)
    t.fd(d)
    t.lt(90-x)
    t.fd(60)
    t.bk(120)
    #finalize
    t.pu()
    t.fd(120)
    t.lt(90)
    t.fd(60)


def drawL():
        #draw bottom stem
        t.pd()
        t.fd(60)
        t.bk(120)
        #draw vertical stem
        t.lt(90)
        t.fd(120)
        #finalize
        t.bk(120)
        t.rt(90)
        t.fd(60)
        t.pu()


def drawM():
        x = 72.111
        b = 33.69
        #go to initial
        t.bk(60)
        t.pd()
        #draw left stem
        t.lt(90)
        t.fd(120)
        #draw center stem 1
        t.rt(90+b)
        t.fd(x)
        #draw center stem 2
        t.lt(2*b)
        t.fd(x)
        #draw right stem
        t.rt(b+90)
        t.fd(120)
        #finalize
        t.pu()
        t.lt(90)
        t.bk(60)

def drawN():
        x = 169.706
        #go to initial
        t.bk(60)
        #draw first stem
        t.pd()
        t.lt(90)
        t.fd(120)
        #draw center stem
        t.rt(90+45)
        t.fd(x)
        #draw final stem
        t.lt(90+45)
        t.fd(120)
        #finalize
        t.pu()
        t.bk(120)
        t.rt(90)
        t.bk(60)


def drawO():
        #draw o
        t.pd()
        for i in range(360):
                t.fd(1.048)
                t.lt(1)
        t.pu()

def drawP():
                #Draws an uppercase B
        #Draw low horizontal stem
        t.lt(180)
        t.fd(60)
        #Draw vertical stem
        t.pd()
        t.rt(90)
        t.fd(120)
        #Draw high horizontal stem
        t.rt(90)
        t.fd(60)
        #Draw the upper hump
        for i in range(180):
                t.fd(0.524)
                t.rt(1)
        t.fd(60)
        #finalize
        t.pu()
        t.lt(90)
        t.fd(60)
        t.lt(90)
        t.fd(60)

def drawQ():
        x = 84.853
        #draw o
        t.pd()
        for i in range(360):
                t.fd(1.048)
                t.lt(1)
        #draw stem
        t.pu()
        t.fd(60)
        t.pd()
        t.lt(180-45)
        t.fd(x)
        #finalize
        t.pu()
        t.rt(45)
        t.bk(60)
        t.rt(90)

def drawR():
        x = 84.853
        #go to initial
        t.lt(180)
        t.fd(60)
        #Draw vertical stem
        t.pd()
        t.rt(90)
        t.fd(120)
        #Draw high horizontal stem
        t.rt(90)
        t.fd(30)
        #Draw the hump
        for i in range(180):
                t.fd(0.524)
                t.rt(1)
        t.fd(30)
        #draw the diagonal stem
        t.rt(180)
        #t.fd(30)
        t.rt(45)
        t.fd(x)
        #finalize
        t.pu()
        t.lt(45)

def drawS():
        x = 0.524
        #initial position
        t.fd(60)
        t.lt(90)
        t.fd(120)
        t.fd(30)
        t.pd()
        #draw top bar
        t.lt(90)
        t.fd(30)
        #draw first hump
        for i in range(180):
                t.fd(x)
                t.lt(1)
        #draw second hump
        for i in range(180):
                t.fd(x)
                t.rt(1)
        t.fd(30)
        #finalize
        t.pu()
        t.rt(180)
        t.fd(30)

def drawT():
        #draw t
        t.pd()
        t.lt(90)
        t.fd(120)
        t.rt(90)
        t.fd(60)
        t.bk(120)
        #finalize
        t.pu()
        t.fd(60)
        t.rt(90)
        t.fd(120)
        t.lt(90)

def drawU():
        x = 1.048
        #go to initial
        t.bk(60)
        t.rt(90)
        t.bk(60)
        #draw vertical stem
        t.pd()
        t.bk(60)
        #draw curve
        t.fd(60)
        for i in range(180):
                t.fd(x)
                t.lt(1)
        #draw vertical stem
        t.fd(60)
        #finalize
        t.pu()
        t.bk(120)
        t.rt(90)
        t.bk(60)

def drawV():
    #Draws an uppercase A
        a = 26.565
        d = 134.164
        #Draw first leg
        t.pd()
        t.lt(90-a)
        t.fd(d)
        #Draw second leg
        t.lt(180)
        t.fd(d)
        #Draw center stem
        t.rt(180-2*a)
        t.fd(d)
        #finalize
        t.pu()
        t.rt(180)
        t.fd(d)
        t.rt(a-90)
