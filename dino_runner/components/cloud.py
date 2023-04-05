import random
import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, CLOUD

class Cloud(Sprite):
    GAME_SPEED = 20
    def __init__(self):
        super().__init__() 
        self.image = CLOUD
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.rect.y = random.randint(50, 100)
        self.width = self.image.get_width()
        self.game_speed = self.GAME_SPEED

    def update(self):
        self.rect.x -= self.game_speed
        if self.rect.right < 0:
            self.rect.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.rect.y = random.randint(50, 100)

    def draw(self, screen):
        screen.blit(self.image, self.rect)