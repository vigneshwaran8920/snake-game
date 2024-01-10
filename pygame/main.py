import pygame
from pygame.locals import *
import time
import random
size=40
class apple:
    def __init__(self,parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("resource/apple.jpg").convert()
        self.block_x=size*3
        self.block_y=size*3
    def draw(self):
        # self.parent_screen.fill((255,255,255))
        self.parent_screen.blit(self.image,(self.block_x,self.block_y))
        pygame.display.flip()
    def move(self):
        self.block_x=random.randint(0,24)*size
        self.block_y=random.randint(0,18)*size
    

class snake:
    def __init__(self,parent_screen,length):
        self.parent_screen = parent_screen
        self.length=length
        self.block = pygame.image.load("resource/block.jpg").convert()
        self.block_x=[size]*length
        self.block_y=[size]*length
        self.direction='down'
    def increase_length(self):
        self.length+=1
        self.block_x.append(-1)
        self.block_y.append(-1)
    def draw(self):
        self.parent_screen.fill((255,255,255))
        for i in range(self.length):
          self.parent_screen.blit(self.block,(self.block_x[i],self.block_y[i]))
        pygame.display.flip()
    def move_up(self):
        self.block_y[0] -= size
        self.draw()
    def move_down(self):
        self.block_y[0] += size
        self.draw()
    def move_left(self):
        self.block_x[0] -= size
        self.draw()
    def move_right(self):
        self.block_x[0] += size
        self.draw()
    def walk(self):
        for i in range(self.length-1,0,-1):
            self.block_x[i]=self.block_x[i-1]
            self.block_y[i]=self.block_y[i-1]
        if self.direction == 'up':
            self.move_up()
        if self.direction == 'down':
            self.move_down()
        if self.direction == 'left':
           self.move_left()
        if self.direction == 'right':
           self.move_right()
        

class Game:
    def __init__(self):
        pygame.init()
        self.surface=pygame.display.set_mode((1000,760))
        self.surface.fill((255,255,255))
        self.snake = snake(self.surface,1)
        self.snake.draw()
        self.apple=apple(self.surface)
        self.apple.draw()
    def display_score(self):
        font = pygame.font.SysFont('arial',30)
        score =font.render(f"score:{self.snake.length}",True,(200,200,200))
        self.surface.blit(score,(800,10))
    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()
        if self.is_collision(self.snake.block_x[0],self.snake.block_y[0],self.apple.block_x,self.apple.block_y):
            self.snake.increase_length()
            self.apple.move()
        if not(-1<self.snake.block_x[0]<1001):
            raise 'GAME OVER'
        if not(-1<self.snake.block_y[0]<801):
            raise 'GAME OVER'

        for i in range(3,self.snake.length):
            if self.is_collision(self.snake.block_x[0],self.snake.block_y[0],self.snake.block_x[i],self.snake.block_y[i]):
                raise 'GAME OVER'
        
    def show_game_over(self):
        self.surface.fill((255,255,255))    
        font=pygame.font.SysFont('arial',30) 
        line1=font.render(f"game is over! your score is {self.snake.length}",True,(200,200,200))
        self.surface.blit(line1,(200,300))
          
        font=pygame.font.SysFont('arial',30)
        line2=font.render(f"to play again press Enter. to exit press cancel button",True,(200,200,200))
        self.surface.blit(line2,(200,350))
        pygame.display.flip()
    def reset(self):
        self.snake = snake(self.surface,1)
        self.apple=apple(self.surface)

            
    def is_collision(self,x1,y1,x2,y2):
        if x1 >= x2 and x1 < x2 + size:
            if y1 >= y2 and y1 < y2 + size:
                return True
    def run(self):
      running=True
      pause=False
      while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_0:
                    running = False
                if event.key == K_RETURN:
                    pause = False    
                if event.key == K_UP:
                    self.snake.direction='up'
                if event.key == K_DOWN:
                    self.snake.direction='down'
                if event.key == K_LEFT:
                    self.snake.direction='left'
                if event.key == K_RIGHT:
                    self.snake.direction='right'
            
                
            elif event.type == QUIT:
                running = False 
        try:
          if not pause:        
              self.play()
        except Exception as e:
            self.show_game_over()
            pause = True
            self.reset()
        time.sleep(0.2)
               
            
           
                
       


     

    



game=Game()
game.run()
    
   
    

   