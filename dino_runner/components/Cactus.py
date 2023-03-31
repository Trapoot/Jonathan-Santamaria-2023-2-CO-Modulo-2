import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS

from dino_runner.utils.constants import SMALL_CACTUS

class Cactus(Sprite):

    def __init__(self):
        self.image = SMALL_CACTUS[0]
        self.cactus_rect = self.image.get_rect()
        self.cactus_rect.x = 700
        self.cactus_rect.y = 322
        self.game_speed = 20
        

    def update(self):
        self.cactus_rect.x -= self.game_speed
        if self.cactus_rect.x < -600:
            self.cactus_rect.x = SCREEN_WIDTH

    def run(self):
        pass

    def jump(self):
        pass

    def duck(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, (self.cactus_rect.x, self.cactus_rect.y))