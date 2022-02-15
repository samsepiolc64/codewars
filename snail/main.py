import numpy as np
def snail(a):
    a = np.array(a)
    new_a = []
    end_a = []
    len_start = len(a.flatten())
    while len(a)>0:
        w = a.shape[0]
        h = a.shape[1]
        new_a.append(a[0:1,0:h].flatten())
        new_a.append(a[1:w, h-1:h].flatten())
        new_a.append(a[w-1:w, 0:h-1][0][::-1].flatten())
        new_a.append(a[1:w-1, 0:1][::-1].flatten())
        a = np.delete(a,0,0)
        h = a.shape[1]
        if h>0: a = np.delete(a, h-1, 1)
        w = a.shape[0]
        if w>0:a = np.delete(a, w-1, 0)
        w = a.shape[0]
        if w>0:a = np.delete(a, 0, 1)
        end_a = []
        for i in new_a:
            for j in i:
                end_a.append(j)
        len_stop = len(end_a)
    if len_start < len_stop:end_a.pop()
    return end_a

if __name__ == '__main__':

    array = [[1,2,3,4],[1,2,3,4]]

    print(snail(array))

    array = [[1, 2],
                   [5, 6],
                   [9, 10],
                   [13, 14]]

    print(snail(array))

    array = [[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12],
                   [13, 14, 15, 16]]

    print(snail(array))

    array = [[1, 2, 3, 4, 5],
                   [6, 7, 8, 9, 10],
                   [11, 12, 13, 14, 15],
                   [16, 17, 18, 19, 20]]

    print(snail(array))

    array = [[1, 2, 3, 4, 5, 6],
                   [7, 8, 9, 10, 11, 12],
                   [13, 14, 15, 16, 17, 18],
                   [19, 20, 21, 22, 23, 24],
                   [25, 26, 27, 28, 29, 30]]

    print(snail(array))
