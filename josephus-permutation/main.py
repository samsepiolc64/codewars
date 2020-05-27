from collections import deque
def josephus(items,k):
    elems = deque(items)
    dead = []
    while len(elems)>0:
        elems.rotate(-k)
        dead.append(elems.pop())
    return dead



arr = [1,2,3,4,5,6,7,8,9,10]
step = 1
print(josephus(arr,step))