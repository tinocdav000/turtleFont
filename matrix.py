def matrixgen(xlen, ylen, message):
    formMess = message.upper() + ' '
    leng = len(formMess)
    finlis = []

    # Add characters to the message so that it is the right length
    #fill = leng % xlen
    #for i in range(0, fill):
    #    formMess += ' '

    leng = len(formMess)

#    print(formMess)
#    print(len(formMess))

    # Find and generate the rows in the final message
    divx = leng/xlen
    divy = divx / ylen
    templis = []
    for i in range(0,leng):
        if (i % xlen == 0 and i !=0) or i == leng-1:
            finlis.append(templis)
            templis = []
        templis.append(formMess[i])
#    print(finlis)
#    print(len(finlis))

    return finlis