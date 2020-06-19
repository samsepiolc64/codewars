import numpy as np
import string
import math as mt
def distance (p1,p2):
    x1, y1, x2, y2 = p1[0], p1[1], p2[0], p2[1]
    return mt.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))
def collinear(p1,p2,p3):
    x1,y1,x2,y2,x3,y3 = p1[0],p1[1],p2[0],p2[1],p3[0],p3[1]
    return (y1 - y2) * (x1 - x3) == (y1 - y3) * (x1 - x2);
def coordinates(point,arr):
    res = np.where(arr == point)
    return list(zip(res[0], res[1]))[0]
def count_patterns_from(firstPoint, length):
    arr = np.asarray([[string.ascii_uppercase[i] for i in range(9)][r * 3:(r + 1) * 3] for r in range(0, 3)])
    allMove, oldSteps, stepVal = [], [], []
    nextPath = 1
    while True:
        arrCollin = []
        for j in arr:
            for i in range(3):
                coord = coordinates(j[i],arr)
                coordFirst = coordinates(firstPoint,arr)
                collin = 8
                dist = round(distance(coordFirst, coord),1)
                for k in arr:
                    for l in range(3):
                        coordTmp = coordinates(k[l], arr)
                        collinTmp = collinear(coord, coordFirst, coordTmp)
                        if not collinTmp and coord != coordFirst != coordTmp and  dist in (1.0, 2.2, 1.4):
                            collin -= 1
                        elif collinTmp and coord != coordFirst != coordTmp and  dist in (2.8, 2.0) and k[l] in oldSteps:
                            collin -= 1
                arrCollin.append(collin)
        arrCollin = np.asarray(arrCollin)
        arrOneDim = arr.flatten()
        arrSteps = []
        steps = {}
        rugElem = firstPoint
        oldSteps.append(rugElem)
        for i in range(9):
            if arrCollin[i] < 8 and arrOneDim[i] not in oldSteps:
                    arrSteps.append(arrOneDim[i])
        steps[firstPoint] = arrSteps
        allMove.append(steps)
        print(allMove)
        l = len(arrSteps)
        lk = len(list(allMove[0].values())[0])

        if nextPath == lk and l == 0:
            stepVal.append(len(allMove))
            ok = 0
            for i in stepVal:
                if i > length and length > 0: ok +=1
            if length == 1: ok = 1
            print(stepVal)
            return ok
        elif l == 0:
            stepVal.append(len(allMove))
            tmp = allMove[0]
            allMove = []
            tmpOldStep = oldSteps[0]
            oldSteps = []
            oldSteps.append(tmpOldStep)
            allMove.append(tmp)
            kl = list(allMove[0].values())
            firstPoint = kl[0][nextPath]
            nextPath += 1
        else:
            firstPoint = arrSteps[0]



print(count_patterns_from('E', 4))