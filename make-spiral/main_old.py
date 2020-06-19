import numpy as np
def partArr(arr,n):
    arr[1, 0] = 0
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            arr[i, n - 2] = 0
            if j == 1 or j == n - 2 or (i == 1 and j > 2):
                arr[j, i] = 0
    print(arr)
    return arr
def spiralize(size):
    n = size
    arr = np.ones(shape=(n,n),dtype=int)
    for i in range(0,n,2):
        if n == 5:
            if i < n/2-1:
                arrTmp = arr[i:n-i,i:n-i]
                arr[i:n-i, i:n-i] = partArr(arrTmp, n-2*i)
        elif n > 5:
            if i < n/2:
                arrTmp = arr[i:n-i,i:n-i]
                arr[i:n-i, i:n-i] = partArr(arrTmp, n-2*i)

    #return arr.tolist()
    return arr

print(spiralize(14))




"""
[
[1, 1, 1, 1, 1, 1], 
[0, 0, 0, 0, 0, 1], 
[1, 1, 1, 1, 0, 1], 
[1, 0, 1, 1, 0, 1], 
[1, 0, 0, 0, 0, 1], 
[1, 1, 1, 1, 1, 1]] 

should equal [
[1, 1, 1, 1, 1, 1], 
[0, 0, 0, 0, 0, 1], 
[1, 1, 1, 1, 0, 1], 
[1, 0, 0, 1, 0, 1], 
[1, 0, 0, 0, 0, 1], 
[1, 1, 1, 1, 1, 1]]

"""