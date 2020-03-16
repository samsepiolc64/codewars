def execute(code):
    code = list(code)
    for i in range(0,len(code)):
        #print(type(code[i]) is int)
        if i > 0:
            test = int(code[i],36)
            if test != 15 and test != 21 and test!= 27:
                dupf = ""
                for j in range(0,test-1):
                    dupf += "F"
                code[i] = dupf
            #print(isinstance(code[i],int))
            #print(code[i])
    code = ''.join(code)


    w, h = 20, 20
    x,y = int(w/2),int(h/2)
    xmin, xmax = x, x
    ymin, ymax = y, y
    xy = [[0 for x in range(w)] for y in range(h)]
    senw = [0, 1, 0, 0]
    xy[y][x] = "*"
    for i in range(0,len(code)):
        if senw[0] == 1 and code[i] == "L": senw = [0, 1, 0, 0]
        elif senw[0] == 1 and code[i] == "R": senw = [0, 0, 0, 1]
        elif senw[1] == 1 and code[i] == "L": senw = [0, 0, 1, 0]
        elif senw[1] == 1 and code[i] == "R": senw = [1, 0, 0, 0]
        elif senw[2] == 1 and code[i] == "L": senw = [0, 0, 0, 1]
        elif senw[2] == 1 and code[i] == "R": senw = [0, 1, 0, 0]
        elif senw[3] == 1 and code[i] == "L": senw = [1, 0, 0, 0]
        elif senw[3] == 1 and code[i] == "R": senw = [0, 0, 1, 0]
        if code[i] == "F":
            if senw[0] == 1: y += 1
            elif senw[1] == 1: x += 1
            elif senw[2] == 1: y -= 1
            elif senw[3] == 1: x -= 1
        if x < xmin: xmin = x
        if x > xmax: xmax = x
        if y < ymin: ymin = y
        if y > ymax: ymax = y
        xy[y][x] = "*"
    wz_w = xmax - xmin + 1
    wz_h = ymax - ymin + 1
    wz = [[0 for x in range(wz_w)] for y in range(wz_h)]
    for y in range(ymin, ymax + 1):
        for x in range(xmin, xmax + 1):
            wz[y-ymin][x-xmin] = xy[y][x]
    print(wz)
    com = ""
    for i in range(0,len(wz)):
        for j in range(0,len(list(zip(*wz)))):
            if wz[i][j] == 0:
                com +=" "
            else: com += str(wz[i][j])
        if  i != len(wz)-1:
            com +="\r\n"
    return(com)



#code = "LF2RF2RF"
#code = "FFLFFLFFFFLFFFF"
#code = "FFFFFFF"
#code = "LF5RF3RF3RF7"
#trans(code)
execute(code)