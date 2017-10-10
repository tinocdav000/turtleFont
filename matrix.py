def matrixgen(xlen, ylen, message):
    formMess = message.upper()
    # formMess += ' '
    leng = len(formMess)
    finlis = []

    # Optimize for spaces
    leng = len(formMess)
    styleMess = []
    for i in range(0,leng):
        if i%xlen == 0 and formMess[i] == ' ':
            pass
        else:
            styleMess.append(formMess[i])
    formMess = styleMess
    
    
    # Add characters to the message so that it is the right length
    leng = len(formMess)
    divx = 1
    while divx != 0:
        formMess += ' '
        leng  = len(formMess)
        divx = (leng-1) % xlen
    #print(divx)

    # Generate the rows of the final message
    templis = []
    for i in range(0,leng):
        if (i % xlen == 0 and i !=0) or i == leng-1:
            finlis.append(templis)
            templis = []
        templis.append(formMess[i])
#    print(finlis)
#    print(len(finlis))

    return finlis

#mess = input("message\n")
#print(matrixgen(4,4,mess))

def inputs():
    # Input the message and format it
    mess = str(input("Please input your desired message\n"))
    mess = mess.upper()
    mes = ''
    for s in mess:
        if ord(s) in range(65,91) or s == ' ':
            mes += s
        else:
            pass
    mess = mes
    #print(mess)
    
    # input the size of the lettering
    fin = False
    while not fin:
        size = input("How large should the letters be? 1-100 \n50 is recommended\n")
        fin = True
        for i in size:
            if ord(i) in range(48,58):
                pass
            else:
                fin = False
        if not fin or len(size) == 0:
            print("Please only input an integer value")
            fin = False
    size = int(size)/100
    #print(size)
    letSize = (120 * size) + (size * 5)
    #print(letSize)
    
    # Input the thickness of the lettering
    fin = False
    while not fin:
        thick = input("How thick should the letters be? 1-10? \nKeep in mind that the smaller the letters, the harder this will be to read, 3 is recommended\n")
        fin = True
        for i in thick:
            if ord(i) in range(48,58):
                pass
            else:
                fin = False
        if not fin or len(thick) == 0:
            print("Please only input an integer value")
            fin = false
    thick = int(thick)
    #print(thick)

    # input the text color
    fin = False
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'black']
    while not fin:
        print("Your choices are:")
        for i in colors:
            print(i)
        col = input('What color would you like the text to be?\n')
        col = col.upper()
        z = col[0]
        fin = True
        if z == 'R':
            col = colors[0]
        elif z == 'O':
            col = colors[1]
        elif z == 'Y':
            col = colors[2]
        elif z == 'G':
            col = colors[3]
        elif z == "B" and 'U' in col:
            col = colors[4]
        elif z == 'P':
            col = col = colors[5]
        elif z == 'B' and 'A' in col:
            col = colors[6]
        else:
            print("Please input a color from the list")
            fin = False
        #print(col)

    # Create output
    out = [mess,letSize,thick,col]
    return out    
