import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING, DEFAULT_TYPE, SHIELD_TYPE, RUNNING_SHIELD, JUMPING_SHIELD, DUCKING_SHIELD, DOUBLE, DOUBLE_TYPE

RUN_IMG ={DEFAULT_TYPE: RUNNING, DOUBLE_TYPE: JUMPING, SHIELD_TYPE: RUNNING_SHIELD}
JUMP_IMG ={DEFAULT_TYPE: JUMPING, DOUBLE_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD}
DUCK_IMG ={DEFAULT_TYPE: DUCKING, DOUBLE_TYPE: JUMPING, SHIELD_TYPE: DUCKING_SHIELD}

class Dinosaur(Sprite):

    X_POS = 80
    Y_POS = 310
    JUMP_SPEED = 8.5
    Y_POS_DUCK = 340


    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0
        self.dino_run = True
        self.dino_jump = False
        self.jump_speed = self.JUMP_SPEED
        self.dino_duck = False
        self.has_power_up = False
        self.power_time_up = 0
        self.can_double_jump = False

    def update(self, user_input):
        if self.dino_run and not self.dino_jump:
            self.run()
        elif self.dino_jump:
            self.jump()

        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_run = False
            self.dino_jump = True        
            if self.can_double_jump:
                self.can_double_jump = False
                self.jump_speed = self.JUMP_SPEED
                self.jump()
        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_run = False
            self.dino_jump = False
            self.dino_duck = True
            self.duck()
        else:
            self.dino_run = True         


        if self.step_index >= 10:
            self.step_index = 0

        if self.has_power_up and self.power_time_up > 0 and self.power_time_up <= 5000: # ajustar el valor de tiempo 
            self.power_time_up -= 1
            if self.power_time_up == 0:
                self.has_power_up = False
                self.can_double_jump = False  # restablecer el atributo al perder el poder correspondiente

    
    def run(self):
        if isinstance(RUN_IMG[self.type], list):
            self.image = RUN_IMG[self.type][self.step_index // 5]
            self.dino_rect = self.image.get_rect()
            self.dino_rect.x = self.X_POS
            self.dino_rect.y  = self.Y_POS
            self.step_index += 1
            self.dino_jump = False

    def jump(self):
        self.image = JUMP_IMG[self.type]
        self.dino_rect.y -= self.jump_speed * 4
        self.jump_speed -= 0.8

        if self.jump_speed < -self.JUMP_SPEED:
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.jump_speed = self.JUMP_SPEED
            #if self.can_double_jump:
                #self.can_double_jump = False
                #self.jump_speed = self.JUMP_SPEED
                #self.jump()

    def duck(self):
        if isinstance(RUN_IMG[self.type], list):
            if len(DUCK_IMG[self.type]) > self.step_index // 5:
                self.image = DUCK_IMG[self.type][self.step_index // 5] 
                self.dino_rect = self.image.get_rect()
                self.dino_rect.x = self.X_POS
                self.dino_rect.y = self.Y_POS + 30
                self.step_index += 1


    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

    def reset(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0
        self.dino_run = True
        self.dino_jump = False
        self.jump_speed = self.JUMP_SPEED
        self.dino_duck = False