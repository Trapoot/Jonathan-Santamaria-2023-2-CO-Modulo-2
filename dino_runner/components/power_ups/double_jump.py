from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import DOUBLE, DOUBLE_TYPE

class DoubleJump(PowerUp):
    def __init__(self):
        super().__init__(DOUBLE, DOUBLE_TYPE)
