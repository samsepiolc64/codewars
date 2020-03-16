def split_and_add(numbers, n):
    if n>0:
        numbers_new = []
        h=int(len(numbers)/2)
        numbers_new.append(numbers[0:h:])
        numbers_new.append(numbers[h::])
        numbers = numbers_new
        numbers[0].reverse()
        numbers[1].reverse()
        numbers_new = [y + x for x, y in zip(*numbers)]
        if not len(numbers[0]) >= len(numbers[1]):
            numbers_new += numbers[1][len(numbers[0]):]
        else:
            numbers_new += numbers[0][len(numbers[1]):]
        numbers = numbers_new
        numbers.reverse()
        n -= 1
    return numbers if n<=0 else split_and_add(numbers,n)


tablica = [32,45,43,23,54,23,54,34]
#tablica = [1,2,3,4,5]
n = 0
print(split_and_add(tablica,n))