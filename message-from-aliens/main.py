def decode(m):

    for i in m:
        if ord(i) == 93:
            print('-')
        else:
            print(i, ord(i))
            #print('*'.join(map(str, bytearray(str(ord(i)), 'utf8'))))





decode("]()]|_]|_]][-]|-|]") #hello
#decode('{|^{|{{|_{]3{') #blip