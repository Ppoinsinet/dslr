import random

valMax = 1000

class Feature:

    def __init__(self, name, index) -> None:
        self.name = name
        self.index = index
        self.theta = (random.random() * valMax) - (valMax/2)