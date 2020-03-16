def letter_count(s):
    s2 = list(set(s))
    print(s2)
    co = {}
    for i in range(0,len(s)):
        l = s.count(s[i])
        co[s[i]] = l
    cosort = dict(sorted(co.items(), key=lambda x: x[0]))
    print (cosort)
    return cosort


strng = 'activity'
letter_count(strng)