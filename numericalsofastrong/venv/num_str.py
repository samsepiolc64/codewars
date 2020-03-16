def numericals(s):
    di = {}
    lens = len(s)
    num = ''
    for i in range(lens):
        if s[i] in di:
            di[s[i]] += 1
        else:
            di[s[i]] = 1
        num += str(di[s[i]])



    #num = ''.join(map(str, di.values()))

    print(num)





#strng = "Hello, World!"

strng = "aaaaaaaaaaaa"
numericals(strng)


#1112111121311