import pygame
import random
import math
from sys import exit

###################################################################################################################
'''
TO DO    class and function
'''
class Board():
    '''class to represent a board object'''
    SIZE = (80,15)
    ori_image = pygame.image.load('plate.png')
    board_image = pygame.transform.scale(ori_image,SIZE)
    def __init__(self):
        '''initialize a board object'''
        self.X = 0
        self.Y = 575
        self.length = 80
        self.image = Board.board_image
        self.rect = pygame.Rect(self.X,self.Y,Board.SIZE[0],Board.SIZE[1])
        self.ball = True
    def move(self,posi):
        '''method to update the position of board'''
        self.X = posi[0] - self.length/2
        if self.X < 0:
            self.X = 0
        if self.X > 800-self.length:
            self.X = 800-self.length
    def elongation(self,l = 20):
        '''method to elongate the board'''
        self.X -= 10
        self.length += 20
        Board.SIZE = (80 + l,15)
        Board.board_image = pygame.transform.scale(Board.ori_image,Board.SIZE)
        self.image = Board.board_image
        self.rect = pygame.Rect(self.X,self.Y,Board.SIZE[0],Board.SIZE[1])
    def shorten(self,l = 20):
        '''method to shorten the board'''
        self.X += 10
        self.length -= 20
        Board.SIZE = (80 - l,15)
        Board.board_image = pygame.transform.scale(Board.ori_image,Board.SIZE)
        self.image = Board.board_image
        self.rect = pygame.Rect(self.X,self.Y,Board.SIZE[0],Board.SIZE[1])
        
class Ball():
    SIZE = (20,20)
    ori_image = pygame.image.load('ball.png')
    ball_image = pygame.transform.scale(ori_image,SIZE)
    
    def __init__(self,X,Y,VX,VY,B):
        '''initialize a Ball object'''
        self.X = X
        self.Y = Y
        self.V_x = VX
        self.V_y = VY
        self.image = Ball.ball_image
        self.rect = pygame.Rect(self.X,self.Y,Ball.SIZE[0],Ball.SIZE[1])
        self.in_board = B
    def move(self):
        '''method to update position of ball'''
        self.X += self.V_x
        self.Y += self.V_y
        self.rect.topleft = (self.X,self.Y)
        if not self.is_in_area_x():
            self.V_x *= -1
        if not self.is_in_area_y_up():
            self.V_y *= -1
        if not self.is_in_area_y_down():
            ball_L.remove(self)
    #three mathod to check if ball is in area
    def is_in_area_x(self):
        if self.X < 0 or self.X > 800-Ball.SIZE[0]:
            return False
        return True
    def is_in_area_y_up(self):
        if self.Y < 0:
            return False
        return True
    def is_in_area_y_down(self):
        if self.Y > 600+Ball.SIZE[1]:
            return False
        return True
        
class Brick():
    def __init__(self,X,Y,T):
        self.X = X
        self.Y = Y
        self.rect = pygame.Rect(self.X,self.Y,40,20)
        if T == '0':
            if (X/40) % 2 == 0: 
                self.color = (255,204,204)
            else:
                self.color = (204,155,153)
        elif T == '1':
            self.color = (255,0,0)
        elif T == '2':
            self.color = (255,128,0)
        elif T == '3':
            self.color = (255,255,0)
        elif T == '4':
            self.color = (0,255,255)
        
def collision_ball_and_brick():
    '''function to handle all collision between ball and brick'''
    for ball in ball_L:
        for brick in brick_L:
            if pygame.Rect.colliderect(ball.rect,brick.rect):
                print(123)
                center_ball = (ball.X+10,ball.Y+10)
                center_brick = (brick.X+20,brick.Y+10)
                dx = abs(center_ball[0] - center_brick[0])
                dy = abs(center_ball[1] - center_brick[1])
                brick_L.remove(brick)
                theta = dy/dx
                if theta < 1/3:
                    ball.V_x *= -1
                if theta > 1/3:
                    ball.V_y *= -1
                break
    return None
def collision_ball_and_board():
    '''function to handle all collision between ball and board'''
    global P
    global ball
    #for ball in ball_L:
    if pygame.Rect.colliderect(P.rect,ball.rect) and ball.Y < 585:
        ball.V_x = random.uniform(-6,6)
        ball.V_y = -1*(7**2 - ball.V_x**2)**(1/2)
    return None
###################################################################################################################
pygame.init()
SIZE = (800,600)
screen = pygame.display.set_mode(SIZE)
BackGround = pygame.image.load('BG3.png')
BackGround = pygame.transform.scale(BackGround,(590,400))
done = False
clock = pygame.time.Clock()
P = Board()
ball = Ball(P.X+30,P.Y-20,0,0,True)
ball_L = [ball]
brick_L = []

file = open('brick.txt','r')
level = file.read()
L_level = level.split(' \n')
level = []
for elem in L_level:
    L_elem = elem.split(' ')
    level += L_elem
level.pop(-1)
file.close()

data_brick = 0
for j in range(0,381,20):
    for i in range(0,761,40):
        T = Brick(i,j,level[data_brick])
        brick_L.append(T)
        data_brick += 1



while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and ball.in_board:
                ball.in_board = not ball.in_board
                ball.V_x = random.uniform(-6,6)
                ball.V_y = -1*(7**2 - ball.V_x**2)**(1/2)
        if event.type == pygame.MOUSEMOTION:
            posi = list(event.pos)
            P.move(posi)
    screen.fill((255,255,255))
    screen.blit(BackGround,(105,0))
    P.rect.topleft = (P.X,P.Y) 
    screen.blit(P.image,(P.X,P.Y))
    for elem in ball_L:
        if elem.in_board:
            elem.X = P.X+30
            elem.Y = P.Y-20
            screen.blit(elem.image,(elem.X,elem.Y))
        if not elem.in_board:
            elem.move()
            screen.blit(elem.image,(elem.X,elem.Y))
    for elem in brick_L:
        pygame.draw.rect(screen,elem.color,elem.rect)

    collision_ball_and_brick()
    collision_ball_and_board()
        
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
exit()