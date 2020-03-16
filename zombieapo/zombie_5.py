import itertools

def survivor(zombies):
    hero = list(range(19))

    for n in range(len(hero)):
        checkzombie(n,zombies, hero)
    print('hero = '+str(max(hero)))

def checkzombie(n,m, hero):
    for i in range(1,n+1):
        l = list(itertools.product(m,repeat = i))
        for j in range(len(l)):
            k = sum(int(x) for x in l[j])
            if k == n and n in hero:
                hero.remove(n)
    return hero

horde = [3,4]
survivor(horde)