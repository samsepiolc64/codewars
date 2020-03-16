#walk = ['e','w','e','w','e','w','e','w','e','w']
#walk = ['e','n','w','s','e','n','w','s','e','w']
#walk = ['e','s','e','n','n','w','w','w','s','e']
walk = ['w','s','s','e','n','e','n','n','w','s']
pos_x = 10
pos_y = 10
sum = 0
def tenminuteswalk(walk,pos_x,pos_y,sum):
    pos2_x = pos_x
    pos2_y = pos_y
    for x in walk:
        sum += 1
        if x == 'e':
            pos2_x += 1
        if x == 'w':
            pos2_x -= 1
        if x == 's':
            pos2_y -= 1
        if x == 'n':
            pos2_y += 1
    if sum == 10 and (pos_x == pos2_x) and (pos_y == pos2_y):
        return True
    else:
        return False

out = tenminuteswalk(walk,pos_x,pos_y,sum)
print(out)
