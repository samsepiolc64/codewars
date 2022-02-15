import numpy

def mm_fib(n):
    return (numpy.matrix([[2,1],[1,1]])**(n//2))[0,(n+1)%2]

def perimeter(n):
    arr = 4*sum([mm_fib(i) for i in range(n+2)][1:])
    return arr

if __name__ == '__main__':
    x = perimeter(5)
    print(x)

