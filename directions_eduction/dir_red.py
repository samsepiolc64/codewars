def dirReduc(arr):
    d = len(arr)
    i = 0
    e = ['NORTHSOUTH', 'SOUTHNORTH', 'EASTWEST', 'WESTEAST']
    while i < d:
        try:
            s = arr[i] + arr[i+1]
            if s in e:
                del arr[i:i+2]
                dirReduc(arr)
            else:
                i += 1
        except:
            break
    print(arr)
    return arr


#a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
#dirReduc(a) #['WEST'])
u=["NORTH", "WEST", "SOUTH", "EAST"]
dirReduc(u), #["NORTH", "WEST", "SOUTH", "EAST"])