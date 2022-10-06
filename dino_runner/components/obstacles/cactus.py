import random

from dino_runner.utils.constants import SMALL_CACTUS
from .obstacle import Obstacle

class Cactus(Obstacle):
    def __init__(self, images):
        type = random.randint(0, 2)
        super().__init__(images, type)
        if images == SMALL_CACTUS:
            self.rect.y = 325
        else:
            self.rect.y = 300