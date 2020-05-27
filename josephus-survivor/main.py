from collections import deque
def josephus_survivor(n,k):
    elems = deque(list(range(1,n+1)))
    print(elems)
    while len(elems)>1:
        elems.rotate(-k)
        elems.pop()
    return elems.pop()



n = 7
step = 3
print(josephus_survivor(n,step))

1,2,3,4,5,6,7