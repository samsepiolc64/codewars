def longest(x,y):


    z = list(set(list(s1+s2)))
    z.sort()
    return''.join(z)



a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b)

#a = "abcdefghijklmnopqrstuvwxyz"
#longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"