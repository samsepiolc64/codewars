def unique_in_order(iterable):


    #print(sorted(set(list(li))))



    iterable = list(iterable)
    dl = len(iterable)
    new = []
    i = 0
    j = 1
    while j <= dl:
        tmp = iterable[i]
        if j < dl:
            if (tmp != iterable[j]) :
                new.append(tmp)
                i = j
        else:
            new.append(tmp)
        j += 1
    print(new)




    #result = []
    #prev = None
    #for char in iterable[0:]:
    #    if char != prev:
    #        result.append(char)
    #        prev = char
    #print(result)








order = "AAAABBBCCDAABBB"
unique_in_order(order)