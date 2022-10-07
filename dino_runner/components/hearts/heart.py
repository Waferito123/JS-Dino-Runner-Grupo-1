from dino_runner.utils.constants import HEART


class Heart:
    def __init__(self, x_pos, y_pos):
        self.image = HEART
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos

    def draw(self, screen):
        screen.blit(self.image, self.rect)