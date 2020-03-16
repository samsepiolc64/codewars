import itertools
def survivor(zombies):

    n = 11


    print(checkzombie(n,zombies))

    #print list(product([1,2,3],repeat = 2))

def checkzombie(n,m):
    for i in range(1,n+1):
        l = list(itertools.product(m,repeat = i))

        #l = ["".join(item) for item in itertools.product([2,3], repeat=i)]
        print(l)
        for j in range(len(l)):
            k = sum(int(x) for x in l[j])

            if k == n:
                pass
                #print(n)



horde = [7, 10]

survivor(horde)