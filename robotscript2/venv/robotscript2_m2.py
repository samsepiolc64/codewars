def execute(code):
    w, h = (80, 80)
    x,y = (int(w/2),int(h/2))

    #x,y = (0,0)

    xmin, xmax = x, x
    ymin, ymax = y, y

    xy = [["0" for l in range(w)] for m in range(h)]

    #arr = [[0 for i in range(cols)] for j in range(rows)]
    #xy = [[0] * h] * w


    senw = [0, 1, 0, 0]
    xy[y][x] = "*"



    code = list(code)
    for i in range(0,len(code)):
        print("znak:" + str(code[i]))
        test = int(code[i],36)
        if test == 15 or test == 21 or test == 27 or test == 25: test=999
        print("test:" + str(test))

        if i < len(code)-1:
            test2 = int(code[i + 1], 36)

            if test <= 9 and test2 <= 9:
                test = test * 10 + test2
                code[i+1] = "P"
        if test != 999:
            dupf = ""
            for j in range(0,test-1):
                dupf += code[i-1]
            code[i] = dupf
            print("po:" + str(code[i]))
            i += 1

        print("---")
    code = "".join(code)
    code = list(code)





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
    com = ""
    for i in range(0,len(wz)):
        for j in range(0,len(list(zip(*wz)))):
            if wz[i][j] == 0:
                com +=" "
            else: com += str(wz[i][j])
        if  i != len(wz)-1:
            com +="\r\n" #to rysuje sciezke
            #com += "/" + "r" + "/" + "n"

    for row in xy:
        print(row)
    print("---------")

    print(com)


#code = "LF2RF2RF"
#code = "FFLFFLFFFFLFFFF"
code = "F29LF3RF"
#code = "LF5RF3RF3RF7"

#code = "F3L2F6R2F3LF3R2F8"
#code = "FFFFFLFFFFFLFFFFFLFFFFFL"
#code = "FFFFLFFFFRFFFFRFFFFLFFFFLFFFFRFFFFRFFFFLFFFFLFFFFRFFFFRFFFF"
#code = "F4LF3LF4LF5LF6LF7LF9LF9LF10"

execute(code)

