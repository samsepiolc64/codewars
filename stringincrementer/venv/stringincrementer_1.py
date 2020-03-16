

def increment_string(strng):

    if strng == '':
        strng  = str(1)
    else:
        l = ''.join(i for i in strng if i.isalpha())
        n = ''.join(i for i in strng if i.isdigit())

        nn = int(n)+1
        i, j = 0, 0
        while i < len(n):
            j += 1
            if n[i] != '0':
                break
            i += 1
        if n[0] == '0':
            z = '0'
            for i in range(0,j-2):
                z += '0'
        else:
            z = ''
        strng = str(l)+str(z)+str(nn)
    print(strng)

    return strng







string = "michu099"
increment_string(string)