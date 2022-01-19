class Guesser:
    def __init__(self, number, lives):
        self.number = number
        self.lives = lives
        self.tmp = self.lives
    def guess(self, n):
        print(self.number,n,self.lives)
        if self.number == n:
            self.lives = self.tmp
            return True
        else:
            if self.lives > 1:
                self.lives -= 1
                return False
            else:
                self.lives = self.tmp
                return 'Omae wa mo shindeiru'






guesser = Guesser(10, 5)
print(guesser.guess(5))
print(guesser.guess(13))
print(guesser.guess(13))
print(guesser.guess(13))
print(guesser.guess(13))
print(guesser.guess(10))
print(guesser.guess(6))
print(guesser.guess(10))
print(guesser.guess(10))
