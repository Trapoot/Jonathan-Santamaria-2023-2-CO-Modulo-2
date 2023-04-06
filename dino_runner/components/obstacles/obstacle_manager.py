import pygame
import random
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD
from dino_runner.utils.constants import SHIELD_TYPE

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.game_over_sound = None
     

    def generate_obstacle(self, obstacle_type):
        if obstacle_type == 0:
            cactus_type = 'SMALL'
            obstacle = Cactus(cactus_type)
        elif obstacle_type == 1:
            cactus_type = 'LARGE'
            obstacle = Cactus(cactus_type)
        else:
            obstacle = Bird()
        return obstacle

    def update(self, game):
        if len(self.obstacles) == 0:
            obstacle_type = random.randint(0,2)
            obstacle = self.generate_obstacle(obstacle_type)
            self.obstacles.append(obstacle)

        to_remove = -1 
        for i, obstacle in enumerate(self.obstacles):
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect) and game.life > 1:
                game.life -= 1
                to_remove = i 
            elif game.player.dino_rect.colliderect(obstacle.rect):
                if game.player.type != SHIELD_TYPE:
                    game.life -=1
                    if game.life == 0:
                        pygame.time.delay(1000)
                        game.death_count.update()
                        game.playing = False
                        self.game_over_sound = pygame.mixer.Sound('C:\\Users\\Usuario\\Documents\\Jala University\\desaparecer.mp3')
                        self.game_over_sound.set_volume(0.05)
                        self.game_over_sound.play()
                    break
                else:
                    to_remove = i
        if to_remove != -1:
            self.obstacles.pop(to_remove)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []
        if self.game_over_sound is not None:
            self.game_over_sound.stop()