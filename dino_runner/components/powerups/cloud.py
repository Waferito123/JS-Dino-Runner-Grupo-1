from dino_runner.components.powerups.powerup import PowerUp
from dino_runner.utils.constants import CLOUD, DEFAULT_TYPE


class Cloud(PowerUp):
    def __init__(self):
        super().__init__(CLOUD, DEFAULT_TYPE)
