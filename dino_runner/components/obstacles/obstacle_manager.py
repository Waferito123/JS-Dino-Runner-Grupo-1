import random
import pygame
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS
from .cactus import Cactus


class ObstacleManager:
    list_of_obstacles = [Cactus(SMALL_CACTUS), Cactus(LARGE_CACTUS)]
    random_obstacles = random.randint(0,1)
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(self.list_of_obstacles[self.random_obstacles])

        for obstacle in self.obstacles:            
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
