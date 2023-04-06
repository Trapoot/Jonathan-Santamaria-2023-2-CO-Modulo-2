import pygame
from dino_runner.components.cloud import Cloud
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE, DEFAULT_TYPE, GAME_OVER, RESET
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.menu import Menu
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components.counter import Counter

class Game:
    GAME_SPEED = 20
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = self.GAME_SPEED
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.menu = Menu(self.screen)
        self.running = False
        self.score = Counter()
        self.death_count = Counter()
        self.highest_score = Counter()
        self.cloud_group = pygame.sprite.Group()
        self.power_up_manager = PowerUpManager()
        self.life = 1

    def execute(self):
        pygame.mixer.init()
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        self.reset_game()
        cloud = Cloud()
        self.cloud_group.add(cloud)
        pygame.mixer.music.load('C:\\Users\\Usuario\\Documents\\Jala University\\rocket.mp3')
        pygame.mixer.music.set_volume(0.05)
        pygame.mixer.music.play(-1)
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.mixer.music.stop()
        self.show_menu()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self)
        self.score.update()
        self.update_game_speed()
    

    def draw(self):
        self.clock.tick(FPS)
        if self.score.count < 1000:
            self.screen.fill((255, 255, 255)) # white background
        elif self.score.count >= 2000:
            self.screen.fill((255, 255, 255)) # white background
        else:
            self.screen.fill((200, 200, 200)) # gray background
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.cloud_group.update()
        self.power_up_manager.draw(self.screen)
        self.draw_power_up_time()
        self.cloud_group.draw(self.screen)
        self.score.draw(self.screen)
        #pygame.display.flip()
        pygame.display.update()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = -50
        self.x_pos_bg -= self.game_speed
        
    def show_menu(self):
        self.menu.reset_screen_color(self.screen)
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2
        
        if self.death_count.count == 0:
            self.menu.draw(self.screen, 'Press any key to start ...')
        else:
            self.update_highest_score()
            self.menu.draw(self.screen, 'Press any key to restart')
            self.menu.draw(self.screen, f'Your score: {self.score.count}', half_screen_width, 350, )
            self.menu.draw(self.screen, f'Highest score: {self.highest_score.count}', half_screen_width, 400, )
            self.menu.draw(self.screen, f'Total deaths: {self.death_count.count}', half_screen_width, 450, )
            self.screen.blit(GAME_OVER, (half_screen_width - 200, half_screen_height - 220))
            self.menu.update(self)
            self.screen.blit(RESET, (half_screen_width - 50, half_screen_height + 180))
            self.menu.update(self)


        self.screen.blit(ICON, (half_screen_width - 50, half_screen_height - 140))
        
        self.menu.update(self)
        


    def update_game_speed(self):
        if self.score.count % 100 == 0 and self.game_speed < 500:
            self.game_speed += 1

    def update_highest_score(self):
        if self.score.count > self.highest_score.count:
            self.highest_score.set_count(self.score.count)

    def reset_game(self):
        self.obstacle_manager.reset_obstacles()
        self.score.reset()
        self.game_speed = self.GAME_SPEED
        self.player.reset()   
        self.power_up_manager.reset()
        self.life == 1

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_time_up - pygame.time.get_ticks())/ 1000, 2)

            if time_to_show >= 0:
                self.menu.draw(self.screen, f"{self.player.type.capitalize()} enable for {time_to_show} seconds", 550, 50)
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE
