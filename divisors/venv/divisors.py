import time
import math
import datetime
import threading
def oblicz(n):
    list = []
    s, sum = 1 ,0
    while (s < n):
        if (n % s == 0): sum += s ** 2
        else: pass
        s += 1
    sum += n ** 2
    sq = math.sqrt(sum)
    if sq.is_integer():
        list.append([int(n),int(sum)])
        #print(list)
        return list
class WatekOblicz(threading.Thread):
    def __init__(self, value):
        threading.Thread.__init__(self)
        self.value = value
    def run(self):
        result = oblicz(self.value)
        return result
def list_squared(n1, n2):
    lista = []
    for n in (range(n1,n2)):
        sr = int((n1+n2)/2)
        n = n / 2
        res1 = WatekOblicz(n).run()
        res2 = WatekOblicz(n+sr).run()

        if res1 != None:
            lista.append(res1)
        if res2 != None:
            lista.append(res2)

        n +=2

    for i in range(0,len(lista)):
        lista[i] = lista[i][0]
    print(lista)
    return lista





list_squared(1,250)