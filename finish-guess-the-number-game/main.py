class Guesser:
    def __init__(self, number, lives):
        self.number = number
        self.lives = lives+1
        self.tmp = self.lives
    def guess(self, n):
        print(self.number,n,self.lives)

        if self.lives > 1:
            if self.number == n:
                self.lives = self.tmp
                return True
            else:
                self.lives -= 1
                return False
        else:
            self.lives = self.tmp
            raise ValueError("Arrays must have the same size")





guesser = Guesser(10, 2)
print(guesser.guess(1))
print(guesser.guess(2))
print(guesser.guess(10))


print(guesser.guess(10))
print(guesser.guess(10))
print(guesser.guess(10))
print(guesser.guess(10))




