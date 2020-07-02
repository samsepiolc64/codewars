class Ball:
    def __init__(self, *type):
        try:
            self.ball_type = type[0]
        except:
            self.ball_type = "regular"
    def ball_type(self):
        return self.ball_type


ball1 = Ball()
ball2 = Ball("super")

print(ball1.ball_type)
print(ball2.ball_type)