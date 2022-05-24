import pygame
from pygame.locals import *
import random
import time
size = 100
background = (0,0,0)#pygame.image.load("side_projects/magic_resources/background.jpg").convert()

class Game:
    def __init__(self):                                                                                                      # initialization function
        pygame.init()                                                                                                        # initializing pygame wrapper
        self.window = pygame.display.set_mode((1800, 900))                                                                   # set the window size
        self.window.fill((255, 255, 255))                                                                                    # window background color
        self.snake = Snake(self.window, 3)                                                                                   # set the snake's beginning color
        self.snake.draw()                                                                                                    # draw the snake on the screen
        self.orb = Orb(self.window)                                                                                          # WHAT?
        self.orb.draw()                                                                                                      # draw the orb on the screen
    
    def display_score(self):                                                                                                 # score display function
        font = pygame.font.SysFont('arial', 30)                                                                              # font size and type
        score = font.render(f"Score: {self.snake.length - 3}", True, (255, 255, 255))                                        # rendering the font with a string and color
        self.window.blit(score, (1600, 0))                                                                                   # move the score to an x,y coordinate

    def play(self):                                                                                                          # play funtion
        self.orb.draw()                                                                                                      # runs the orb drawing function
        self.snake.walk()                                                                                                    # runs the snake walking function
        self.display_score()                                                                                                 # runs the core displaying function
        pygame.display.flip()                                                                                                # WHAT?

        # Orb Collision
        if self.collision(self.snake.x[0], self.snake.y[0], self.orb.x, self.orb.y):                                         # Orb collision check
            self.snake.grow()                                                                                                # runs the snake growth function
            self.orb.move()                                                                                                  # run the orb relocation function
        
        # Body Collision
        for i in range(3, self.snake.length):                                                                                # Iterates through all of the body parts
            if self.collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):                           # checks if a body part is colliding with the head
                raise "Game over"                                                                                            # Raises an exception called "Game over"
    
    def reset(self):                                                                                                         # game reset function
        self.snake = Snake(self.window, 3)                                                                                   # changes the snake's length to 3
        self.orb = Orb(self.window)                                                                                          # resets the orb to the default position

    def show_gg(self):                                                                                                       # game over screen function
        self.window.fill(background)                                                                                         # fill the background with the background variable rgb
        font = pygame.font.SysFont('arial', 30)                                                                              # font blueprint
        gg_score = font.render(f"Game over! Score: {self.snake.length - 3}", True, (255, 255, 255))                          # font sprite
        self.window.blit(gg_score, (200, 200))                                                                               # font render
        restart_question = font.render(f"To restart, press Enter", True, (255, 255, 255))                                    # font sprite
        self.window.blit(restart_question, (200, 300))                                                                       # font render
        pygame.display.flip()                                                                                                # update the display

    def collision(self, x1, y1, x2, y2):                                                                                     # collision function
        if x1 >= x2 and x1 < x2 + size:                                                                                      # WHAT?
            if y1 >= y2 and y1 < y2 + size:                                                                                  # WHAT?
                return True                                                                                                  # returns collision + vars as true
        return False                                                                                                         # returns collision + vars as false

    def run(self):                                                                                                           # game run function
        running = True                                                                                                       # sets running to true

        while running:                                                                                                       # whenever running is true it will...
            for event in pygame.event.get():                                                                                 # check for events
                if event.type == KEYDOWN:                                                                                    # if a key is pressed
                    if not pause:                                                                                            # if the game isn't paused
                        if event.key == K_w:                                                                                 # if the key is w
                            if not self.snake.direction == 'down':                                                           # ignore if it's going the opposite direction
                                self.snake.move_up()                                                                         # run the move up function

                        elif event.key == K_s:                                                                               # if the key is s
                            if not self.snake.direction == 'up':                                                             # ignore if it's going the opposite direction
                                self.snake.move_down()                                                                       # run the move down function
                            
                        elif event.key == K_a:                                                                               # if the key is a
                            if not self.snake.direction == 'right':                                                          # ignore if it's going the opposite direction
                                self.snake.move_left()                                                                       # run the move left function
                            
                        elif event.key == K_d:                                                                               # if the key is d
                            if not self.snake.direction == 'left':                                                           # ignore if it's going the opposite direction
                                self.snake.move_right()                                                                      # run the move right function
                        
                    elif event.key == K_RETURN:                                                                              # if they key is enter
                        self.snake.length = 3                                                                                # set the snake's length to 3
                        pause = False                                                                                        # unpause

                    elif event.key == K_ESCAPE:                                                                              # if the key is escape
                        running = False                                                                                      # stop running the game

                if event.type == QUIT:                                                                                       # if the x button is pressed
                    running = False                                                                                          # stop running the game

            try:                                                                                                             # try to
                if not pause:                                                                                                # check if paused, if not
                    self.play()                                                                                              # run the play function
            except Exception as e:                                                                                           # if you can't
                self.show_gg()                                                                                               # run the game over function
                pause = True                                                                                                 # pause the game
                self.reset()                                                                                                 # run the reset function

            time.sleep(0.3)                                                                                                  # wait half a second

class Snake:                                                                                                                 # create the snake class
    def __init__(self, window, length):                                                                                      # initialize the class with the window and length
        self.length = length                                                                                                 # make length a child of the class
        self.window = window                                                                                                 # make window a child of the class
        self.body = pygame.image.load("side_projects/magic_resources/body.png").convert_alpha()                              # make the body a child of the class
        self.body = pygame.transform.smoothscale(self.body, (100,100))                                                       # scale down the body pixels
        self.y = [size] * length                                                                                             # WHAT?
        self.x = [size] * length                                                                                             # WHAT?
        self.direction = ''                                                                                                  # default snake direction

    def draw(self):                                                                                                          # draw function
        for i in range(self.length):                                                                                         # iterates through the snake's body
            self.window.blit(self.body, (self.x[i], self.y[i]))                                                              # renders the snake's body
        pygame.display.flip()                                                                                                # draws everything
    
    def grow(self):                                                                                                          # snake growth function    
        self.length += 1                                                                                                     # adds 1 to the snake's length
        self.x.append(-1)                                                                                                    # WHAT?
        self.y.append(-1)                                                                                                    # WHAT?
    
    def move_up(self):                                                                                                       # move up function
        self.direction = 'up'                                                                                                # set the direction of the snake
    
    def move_down(self):                                                                                                     # move up function
        self.direction = 'down'                                                                                              # set the direction of the snake
    
    def move_left(self):                                                                                                     # move up function
        self.direction = 'left'                                                                                              # set the direction of the snake
    
    def move_right(self):                                                                                                    # move up function
        self.direction = 'right'                                                                                             # set the direction of the snake
    
    def walk(self):                                                                                                          # snake movement function

        for i in range(self.length - 1, 0 , -1):                                                                             # WHAT?
            self.x[i] = self.x[i - 1]                                                                                        # WHAT?
            self.y[i] = self.y[i - 1]                                                                                        # WHAT?

        if self.direction == 'up':                                                                                           # check if the snake's direction is up
            self.y[0] -= 100                                                                                                 # moves the snake up
        if self.direction == 'down':                                                                                         # checks if the snake's direction is down
            self.y[0] += 100                                                                                                 # moves the snake down
        if self.direction == 'left':                                                                                         # check if the snake's direction is left
            self.x[0] -= 100                                                                                                 # moves the snake left
        if self.direction == 'right':                                                                                        # check if the snake's direction is right
            self.x[0] += 100                                                                                                 # moves the snake right

        self.draw()                                                                                                          # runs the draw function

class Orb:                                                                                                                   # creates orb class
    def __init__(self, window):                                                                                              # intializes the orb class
        self.orb = pygame.image.load("side_projects/magic_resources/orb.png").convert_alpha()                                # makes the orb a child of the orb class
        self.orb = pygame.transform.smoothscale(self.orb, (100,100))                                                         # scales down the orb
        self.window = window                                                                                                 # makes the window a child of the orb class
        self.x = 1                                                                                                           # orb default x coordinate
        self.y = 0                                                                                                           # orb default y coordinate
    
    def draw(self):                                                                                                          # orb draw function
        self.window.fill((0, 0, 0))                                                                                          # set the window background to black
        self.window.blit(self.orb, (self.x, self.y))                                                                         # renders the orb
        pygame.display.flip()                                                                                                # updates the window scene

    def move(self):                                                                                                          # orb relocation function
        self.x = random.randint(0,17) * size                                                                                 # changes the orb location to a random x value
        self.y = random.randint(0,8) * size                                                                                  # changes the orb location to a random y value
        if self.x and self.y == 0:
            self.x = 100

game = Game()                                                                                                                # make the game class a variable
game.run()                                                                                                                   # run the game