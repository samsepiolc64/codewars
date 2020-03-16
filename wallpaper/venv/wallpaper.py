import math

class howManyWall:
    def __init__(self,l, w, h):
        self.l = l
        self.w = w
        self.h = h
    def wallpaper(self):
        n2w = ['zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty']
        if self.l*self.w*self.h != 0:
            rol = math.ceil(((2*(self.l*self.h)+2*(self.w*self.h))/(0.52*10))+(0.15*((2*(self.l*self.h)+2*(self.w*self.h))/(0.52*10))))
        else:
            rol = 0
        return n2w[rol-1]








#wallpaper(2, 3, 4)
#wallpaper(6.3, 4.5, 3.29)
#wallpaper(6.3, 4.5, 3.29)
#wallpaper(7.8, 2.9, 3.29)
#wallpaper(6.3, 5.8, 3.13)


x = howManyWall(3.1, 6.7, 2.81)
print(x.wallpaper())