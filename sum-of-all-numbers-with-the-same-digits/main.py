def permutation(num):
    if type(num) is not list: num = list(str(num))
    if len(num) == 0: return []
    if len(num) == 1: return [num]
    l = []
    for i in range(len(num)):
        m = num[i]
        remLst = num[:i] + num[i + 1:]
        for p in permutation(remLst): l.append([m] + p)
    return l

def sum_arrangements(num):
    p = permutation(num)
    sumall = 0
    for i in p: sumall += int(''.join(i))
    return sumall


print(sum_arrangements(1234567891))