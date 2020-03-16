import math
def list_squared(n1,n2):
    list = []
    for n in (range(n1,n2)):
        s, sum = 1 ,0
        while (s < n):
            if (n % s == 0): sum += s ** 2
            else: pass
            s += 1
        sum += n ** 2
        sq = math.sqrt(sum)
        if sq.is_integer():
            list.append([n,sum])
    return list


list_squared(1,250)