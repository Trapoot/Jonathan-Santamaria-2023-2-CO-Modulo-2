import random

from dino_runner.components.obstacles.obstacle import Obstacle

class Cactus(Obstacle):
    def init(self, image):
        self.type = random.randint(0, 2)
        super(). init(image, self.type)
        self.rect.y = 325