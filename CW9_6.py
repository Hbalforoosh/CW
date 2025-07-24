class Robot:
    Robots = 0

    def __init__(self, name):
        self.name = name
        Robot.Robots += 1

    @classmethod
    def all_robots(cls):
        return cls.Robots


robot1 = Robot("Smart1")
robot2 = Robot("Smart2")
robot3 = Robot("Smart3")

print("number of robots: ", Robot.all_robots())
