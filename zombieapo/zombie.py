from math import *
def survivor(a):
    print(a)
    if a == [1]:
        return 0
    else:
        if len(a) < 2 or nwd(*a) > 1:
            return -1
        if max(residue_table(sorted(a))) == 0:
            return 0
        else:
            return max(residue_table(sorted(a))) - min(a)

def nwd(a, *r):
    for b in r:
        a = gcd(a, b)
    return a

def residue_table(a):
    n = [0] + [None] * (a[0] - 1)
    for i in range(1, len(a)):
        d = nwd(a[0], a[i])
        for r in range(d):
            try:
                nn = min(n[q] for q in range(r, a[0], d) if n[q] != None)
            except:
                continue
            if nn != None:
                for c in range(a[0] // d):
                    nn += a[i]
                    p = nn % a[0]
                    nn = min(nn, n[p]) if n[p] != None else nn
                    n[p] = nn
    return n


print(survivor([2,10]))
#print(survivor([1]))
#print(survivor([1,7,15]))
#print(survivor([687,829,998]))