import numpy as np

class Missile:
    def __init__(self, x: float, y: float, speed: float, heading: float):
        self.x = x
        self.y = y
        self.speed = speed
        self.heading = heading
        self.trajectory = [(x, y)]

    def update_position(self, new_x: float, new_y: float):
        self.x = new_x
        self.y = new_y
        self.trajectory.append((new_x, new_y))

    def get_trajectory(self):
        return np.array(self.trajectory)


class Target:
    def __init__(self, x: float, y: float, speed: float):
        self.x = x
        self.y = y
        self.speed = speed
        self.predicted_x = x
        self.predicted_y = y