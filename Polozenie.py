import math


class Polozenie:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def equals(self, p):
        return p.x == self.x and p.y == self.y

    def set(self, p):
        self.x = p.x
        self.y = p.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def get_distance(self, p2):
        return math.sqrt(pow(abs(self.x - p2.x), 2) + pow(abs(self.y - p2.y), 2))

    def subtract(self, p2):
        return Polozenie(self.x - p2.x, self.y - p2.y)

    def add(self, p2):
        return Polozenie(self.x + p2.x, self.y + p2.y)