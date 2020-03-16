def increment_string(strng):

    l = ''.join(i for i in strng if i.isalpha())
    n = [int(x) for x in strng if x.isdigit()]

    if not n:
        if strng == '':
            strng = str(1)
            nn = ''
        else:
            strng = l
            nn = 1
        strng = strng+ str(nn)
    else:
        m = n.copy()
        m.reverse()
        d, nn = 1 ,0
        for i in range(0, len(m)):
            nn += m[i] * d
            d *= 10
        nn +=1


        i, j = 0, 0
        while i < len(n):
            j += 1
            if n[i] != 0:
                break
            i += 1


        if n[0] == 0 and nn < 99:
            z = '0'
            for i in range(0, j - 2):
                z += '0'
        else:
            z = ''
        strng = str(l) + str(z) + str(nn)


    print(strng)
    return strng


#i.isdigit()

#x.isdecimal()



string = "michu"
increment_string(string)