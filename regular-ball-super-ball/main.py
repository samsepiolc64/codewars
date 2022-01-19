class Ball:
    def __init__(self, type = "regural"):
        self.ball_type = type

ball1 = Ball()
ball2 = Ball("super")

print(ball1.ball_type)
print(ball2.ball_type)