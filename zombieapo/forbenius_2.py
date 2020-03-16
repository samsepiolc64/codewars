def nwd(a, b):
    while (a != 0):
        c = a
        a = b % a
        b = c
    return b;

def forbenius(X, Y):
    if (nwd(X, Y) != 1):
        return 0
    hero = (X * Y) - (X + Y)
    return hero

X = 1
Y = 10

print(forbenius(X, Y))
