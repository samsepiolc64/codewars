import itertools

def survivor(zombies):
    #hero = list(range(149))
    sumlist = []

    sumgen(zombies, sum(zombies), sumlist)
    sumlist.sort(reverse=True)
    hero = checkzombie(sumlist)
    return hero


    """
    for n in range(len(hero)):
        checkzombie(n, hero, sumlist)
    return max(hero)
    """
def sumgen(m,maxhero,sumlist):
    for i in range(1,maxhero+1):
        l = list(itertools.combinations_with_replacement(m, i))
        print(l)
        #l = list(itertools.product(m,repeat = i))
        for j in range(len(l)):
            k = sum(int(x) for x in l[j])
            if k not in sumlist:
                sumlist.append(k)
    return sumlist

def checkzombie(sumlist):
    for i in range(len(sumlist)):
        if sumlist[i]-1 != sumlist[i+1]:
            print(sumlist)
            print (sumlist[i]-1)
            return sumlist[i]-1

horde = [1,7,15]
print('hero = '+str(survivor(horde)))