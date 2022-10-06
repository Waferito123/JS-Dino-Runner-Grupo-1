import random
from .obstacle import Obstacle

class Bird(Obstacle):
    def __init__(self, images):
        type = random.randint(0, 1)
        super().__init__(images, type)
        self.rect.y = 260
        