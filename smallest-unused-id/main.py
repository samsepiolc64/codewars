def next_id(arr):
    min_id = 0 if not arr else min(set(list(range(0, max(arr) + 2))) - set(arr))
    return min_id
print(next_id([0,1,3,4,5,6]))