from dino_runner.components.hearts.heart import Heart
from dino_runner.utils.constants import HEART_COUNT


class PlayerHeartManager:
    def __init__(self):
        self.heart_count = HEART_COUNT

    def reduce_heart(self):
        self.heart_count -= 1

    def draw(self, screen):
        x_pos =  10
        y_pos = 20
        for counter in range(self.heart_count):
            heart = Heart(x_pos, y_pos)
            heart.draw(screen)
            x_pos += 30

    def reset_hearts(self):
        self.heart_count = HEART_COUNT