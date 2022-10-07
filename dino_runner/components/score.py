import pygame

from dino_runner.utils.constants import FONT_STYLE
from dino_runner.utils.constants import HEART


class Score:
    def __init__(self):
        self.score = 0

    def update(self, game):
        self.score += 1
        if self.score % 100 == 0:
            game.game_speed += 2

        if self.score % 1000 == 0:
            game.heart_manager.increase_heart()
            
    def draw(self, screen, game):
        game.draw_message(f"Points: {self.score}", 1000, 50, 22)
        game.draw_message("1000 points = ", 950, 550, 22)
        screen.blit(HEART, (1025, 537))

    def reset_score(self):
        self.score = 0
        