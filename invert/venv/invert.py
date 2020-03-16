
def invert(num):
    num = list(str(num))
    num.sort()
    return int(''.join(num[::-1]))





a = 12345601
invert(a)