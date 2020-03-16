import string
from itertools import *
import itertools
def tongues(code):
    code = list(code)
    v, nv = ['a', 'i', 'y', 'e', 'o', 'u'], ['b', 'k', 'x', 'z', 'n', 'h', 'd', 'c', 'w', 'g', 'p', 'v', 'j', 'q', 't', 's', 'r', 'l', 'm', 'f']
    j = 0
    for i in code:
        if i in string.ascii_uppercase:
            up = True
            i = i.lower()
        if i in v: code[j]=list(itertools.islice(cycle(v), v.index(i)+3, v.index(i)+4, 1))[0]
        elif i in nv: code[j] = list(itertools.islice(cycle(nv), nv.index(i) + 10, nv.index(i) + 11, 1))[0]
        if up: code[j] = code[j].upper()
        j += 1
        up = False
    #return ''.join(code)
    print(''.join(code))



fraza = 'Ita dotf ni dyca nsaw ecc.' #One ring to rule them all.
tongues(fraza)