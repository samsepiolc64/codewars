import itertools

def survivor(zombies):
    hero = list(range(149))
    sumlist = []

    sumgen(zombies, sum(zombies), sumlist)

    for n in range(len(hero)):
        checkzombie(n, hero, sumlist)
    return max(hero)

def sumgen(m,maxhero,sumlist):
    for i in range(1,maxhero+1):
        l = list(itertools.combinations_with_replacement(m, i))
        #l = list(itertools.product(m,repeat = i))
        for j in range(len(l)):
            k = sum(int(x) for x in l[j])
            if k not in sumlist:
                sumlist.append(k)
    return sumlist

def checkzombie(n, hero, sumlist):
    if n in sumlist and n in hero:
        hero.remove(n)
    return hero

horde = [1,7,15]
print('hero = '+str(survivor(horde)))