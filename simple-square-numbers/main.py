import math
def solve(n):
    if n % 2 == 0:
        for i in range(int(math.sqrt(n))-1,n):
            if n > i > 0 and math.modf(math.sqrt(n+(i**2)))[0] == 0:
                return i**2
    else:
        print (n/2)
        print(math.floor(n / 2), math.ceil(n / 2))
        print(math.floor(n / 2)**2, math.ceil(n / 2)**2)
        print((math.ceil(n / 2)**2) - (math.floor(n / 2)**2))
        if n > 1:
            return math.floor(n / 2)**2
    return -1

#print(solve(7))
#print(solve(17))
#print(solve(88901))
print(solve(5365384668900))
#print(solve(290101))


"""

17195751194176 should equal 925558929
2289047961600 should equal 304704
5365384668900 should equal 7056
13193385352900 should equal 136375684
18015618959361 should equal 367661535201
"""