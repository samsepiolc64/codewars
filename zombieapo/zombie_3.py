a = 1

for a in range(13):
    l = [3, 4]
    k = []

    i = 0
    l.sort(reverse=True)

    def addk(l,a,k):
        for i in l:
            if i <= a:
                a = a - i
                if 0 <= a:
                    k.append(i)

    while i<a:
        if sum(k)<a:
            addk(l,a-sum(k),k)
        i += 1

    print(a)
    print(k)

    """
    if sum(k) == a:
        print(k)
        print(a)
    """

