import pygame
import random
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def generate_obstacle(self):
        if random.random() < 0.2:
            obstacle = Bird(BIRD)
        else:
            if random.random() < 0.5:
                obstacle = Cactus(LARGE_CACTUS)
                obstacle.rect.y = 300
            else:
                obstacle = Cactus(SMALL_CACTUS)
        return obstacle

    def update(self, game):
        if len(self.obstacles) == 0:
            obstacle = self.generate_obstacle()
            self.obstacles.append(obstacle)

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                print("Colission")
                pygame.time.delay(1000)
                game.death_count +=1
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []