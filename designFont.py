import turtle as t
t.Screen()

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
        #Draws an uppercase C
        #Go to top corner
        t.fd(60)
        t.lt(90)
        t.fd(120)
        #Draw C
        t.lt(90)
        for i in range(180):
                t.fd(1.047)
                t.lt(1)
        #Finalize
        t.bd(60)
