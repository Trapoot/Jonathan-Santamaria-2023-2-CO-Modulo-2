from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import LIFE_TYPE, HEART

class LifeUp(PowerUp):
    def __init__(self):
        super().__init__(HEART, LIFE_TYPE)

