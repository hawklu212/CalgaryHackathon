class ThrowingBear:
    """This is a throwing bear class where the bear throws the curling stone"""

    def __init__(self, xposition):
        # Class attribute
        size = 100

        self.xposition = xposition


class SweepingBear:
    """This is a sweeping bear class where the bear sweeps the ice"""

    def __init__(self, xposition, yposition, speed):
        # Class attribute
        size = 100

        self.xposition = xposition
        self.yposition = yposition
        self.speed = speed


class Stone:
    """This is a curling stone class"""

    def __init__(self, xposition, yposition, speed, angle,radius,acc):
        radius = 20

        self.xposition = xposition
        self.yposition = yposition
        self.angle = angle
        self.speed = speed
        self.radius = radius
        self.acc = acc

    def stoneCollison(self, stone, radius):
        if self.calculateDistance(stone) >= (radius * 2) ** 2:
            return True;
            return False

    def calculateDistance(self, stone1, stone2):
        ((stone1.xposition - stone2.xposition) ** 2) + ((stone1.yposition - stone2.yposition) ** 2)
        # a^2 + b^2


class Scoreboard:
    """This is a scoreboard class"""

    def __init__(self, score):
        self.score = score