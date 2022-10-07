from random import randint
import random

import pygame
from .cloud import Cloud
from .shield import Shield


class PowerUpManager:
    list_of_power_ups = [Cloud(), Shield()]

    def __init__(self):
        self.power_ups = []
        self.when_appears = 0

    def generate_power_up(self, score):
        if len(self.power_ups) == 0 and self.when_appears == score:
            self.power_ups.append(random.choice(self.list_of_power_ups))
            self.when_appears += randint(200, 300)

    def update(self, game_speed, player, score):
        self.generate_power_up(score)
        for power_up in self.power_ups:
            if power_up == self.list_of_power_ups[1]:
                power_up.update(game_speed, self.power_ups)
                if player.dino_rect.colliderect(power_up.rect):
                    power_up.start_time = pygame.time.get_ticks()
                    player.on_pick_power_up_shield(power_up.start_time, power_up.duration, power_up.type)
                    self.power_ups.remove(power_up)
            elif power_up == self.list_of_power_ups[0]:
                power_up.update(game_speed, self.power_ups)
                if player.dino_rect.colliderect(power_up.rect):
                    power_up.start_time = pygame.time.get_ticks()
                    player.on_pick_power_up_cloud(power_up.start_time, 10, power_up.type)
                    self.power_ups.remove(power_up)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = randint(300, 400)
