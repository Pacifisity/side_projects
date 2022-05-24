import pygame
from pygame.locals import *
import pygame_menu
import time
import random
class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((1800, 900))
        self.window.fill((255, 255, 255))
        pygame.display.flip()
        time.sleep(5)
    
    def run(self):
        running = True

        while running:
            for event in pygame.event.get(): 
                if event.type == KEYDOWN:
                    if event.key == K_w:
                        pass

                    elif event.key == K_s:
                        pass
                        
                    elif event.key == K_a:
                        pass
                        
                    elif event.key == K_d:
                        pass
                        
                    elif event.key == K_RETURN:
                        running = False

                    elif event.key == K_ESCAPE:
                        running = False

                if event.type == QUIT:
                    running = False

            self.play()
        
    def play(self):
        pygame.display.flip()

        time.sleep(0.3)

game = Game()
game.run()