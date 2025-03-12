# pyright: reportMissingImports=false
import pygame, sys
from settings import *
from level import Level
import os

class Game:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))

        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Adventure Game')
        self.clock = pygame.time.Clock()

        self.level = Level()

        main_sound = pygame.mixer.Sound(os.path.join(base_dir, 'audio', 'titled.ogg'))
        main_sound.set_volume(0.1)
        main_sound.play(loops = -1)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()
            
            self.screen.fill(WATER_COLOR)
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()