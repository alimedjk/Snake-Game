import pygame
import sys
import random
from pygame.math import Vector2
pygame.init()

class Snake:
   
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(1,0)
        self.new_block = False

    def draw_snake(self,win):
        dis = 20
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int( block.y * cell_size)
            i = self.body[0].x
            j = self.body[0].y
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(win, (255,0,0), block_rect)
            if block == self.body[0]:
                centre = dis//2
                radius = 3
                circleMiddle = (i*dis+centre-radius,j*dis+8)
                circleMiddle2 = (i*dis + dis -radius*2, j*dis+8)
                pygame.draw.circle(win, (0,0,0), circleMiddle, radius)
                pygame.draw.circle(win, (0,0,0), circleMiddle2, radius)

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
           body_copy = self.body[:-1]
           body_copy.insert(0,body_copy[0] + self.direction)
           self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def reset(self):
        self.body = [Vector2(5,10), Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(1,0)
        self.new_block = False


class FRUIT:
    def __init__(self):
        self.randomize()

    def draw_fruit(self,win):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y*cell_size), cell_size, cell_size)
        pygame.draw.rect(win, (0,255,0), fruit_rect)
    
    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x,self.y)


class Main:
       def __init__(self):
          self.snake = Snake()
          self.fruit = FRUIT()
          self.score = 0
        
       def update(self):
            self.snake.move_snake()
            self.check_collision()
            self.check_fail()
            
        
       def draw_main(self,win):
            self.snake.draw_snake(win)
            self.fruit.draw_fruit(win)
            self.Your_score()

       def check_collision(self): 
           if self.fruit.pos == self.snake.body[0]:
               self.fruit.randomize()
               self.snake.add_block()
               self.score =len(self.snake.body)-2

           for block in self.snake.body[1:]:
                if block == self.fruit.pos:
                    self.fruit.randomize()

       def check_fail(self):
            if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
                self.game_over()

            for block in self.snake.body[1:]:
                if block == self.snake.body[0]:
                    self.game_over()

       def Your_score(self):
           score_font = pygame.font.SysFont("comicsansms", 15)
           value = score_font.render("Your Score: " + str(self.score), True, yellow)
           WIN.blit(value, [0, 0])

       def game_over(self):
          self.snake.reset()
          self.fruit.randomize()
          
          


cell_size = 20
cell_number = 20
black = (0, 0, 0)
yellow = (255, 255, 102)
WIN  = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
pygame.display.set_caption("Snake")

font_style = pygame.font.SysFont("bahnschrift", 25)





def drawGrid(w, rows, surface):
    sizeBtwn = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (255,255,255), (x,0),(x,w))
        pygame.draw.line(surface, (255,255,255), (0,y),(w,y))

def redraw(win):
    global main_game
    win.fill(black)
    main_game.draw_main(WIN)
    
    drawGrid(cell_size * cell_number, cell_number, win)
    pygame.display.update()


def main():
    global main_game
    run =True
    clock = pygame.time.Clock()
    main_game = Main()

    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE,150)

    while run:
        clock.tick(60)
        redraw(WIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == SCREEN_UPDATE:
               main_game.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if main_game.snake.direction.y !=1:
                      main_game.snake.direction = Vector2(0,-1)
                if event.key == pygame.K_RIGHT:
                    if main_game.snake.direction.x !=-1:
                      main_game.snake.direction = Vector2(1,0)
                if event.key == pygame.K_DOWN:
                    if main_game.snake.direction.y !=-1:
                      main_game.snake.direction = Vector2(0,1)
                if event.key == pygame.K_LEFT:
                    if main_game.snake.direction.x !=1:
                      main_game.snake.direction = Vector2(-1,0)

    pygame.quit()

if __name__ == '__main__':
    main()

