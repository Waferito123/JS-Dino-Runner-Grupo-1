import random
import pygame

from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD
from .cactus import Cactus
from .bird import Bird


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game_speed, player, on_death):
        if len(self.obstacles) == 0:
            list_of_obstacles = [Cactus(SMALL_CACTUS), Cactus(LARGE_CACTUS), Bird(BIRD)]
            # random_obstacles = random.randint(0, 2)
            # self.obstacles.append(list_of_obstacles[random_obstacles])
            self.obstacles.append(random.choice(list_of_obstacles))

        for obstacle in self.obstacles:            
            obstacle.update(game_speed, self.obstacles)
            if player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                on_death()
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []