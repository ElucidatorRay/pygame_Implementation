import pygame
import random
import math
from sys import exit
'''
from Player_class import *
from Bullet_class import *
from Plant_class import *
from Stone_class import *
from collision_functions import *
'''
###################################################################################################################
class Player():
    '''class to represent player'''
    #Dead image
    DEAD_red_L = pygame.image.load('DEADred_L.png')
    DEAD_blue_R = pygame.image.load('DEADblue_R.png')
    DEAD_red_L = pygame.transform.scale(DEAD_red_L, (60,55))
    DEAD_blue_R = pygame.transform.scale(DEAD_blue_R, (60,55))
    #normal image
    normal_red_L = pygame.image.load('normal_red_L.png')
    normal_blue_R = pygame.image.load('normal_blue_R.png')
    normal_red_L = pygame.transform.scale(normal_red_L, (60,55))
    normal_blue_R = pygame.transform.scale(normal_blue_R, (60,55))
    #gunner image
    gunner_red_L = pygame.image.load('gunner_red_L.png')
    gunner_blue_R = pygame.image.load('gunner_blue_R.png')
    gunner_red_L = pygame.transform.scale(gunner_red_L, (70,55))
    gunner_blue_R = pygame.transform.scale(gunner_blue_R, (70,55))
    #shoted image
    shot_gun_L = pygame.image.load('shot_gun_L.png')
    shot_gun_R = pygame.image.load('shot_gun_R.png')
    shot_nor_L = pygame.image.load('shot_nor_L.png')
    shot_nor_R = pygame.image.load('shot_nor_R.png')
    shot_gun_L = pygame.transform.scale(shot_gun_L, (70,55))
    shot_gun_R = pygame.transform.scale(shot_gun_R, (70,55))
    shot_nor_L = pygame.transform.scale(shot_nor_L, (60,55))
    shot_nor_R = pygame.transform.scale(shot_nor_R, (60,55))
    #initial value
    init_velocity = 3
    init_position_L = 20
    init_position_R = 925
    #each time section
    reload_time = 100
    stop_time = 15
    white_time = 7
    #size of image
    gun_SIZE = (70,55)
    nor_SIZE = (60,55)
    
    def __init__(self,S):
        '''
        X,Y,V,P    position, velocity and side of player
        life       the remaining life point
        counter    timer to handle stoping, shoted and reloading
        center     center of rect
        temp       save the current velocity
        image      graph of player
        bullet     need reload or not
        '''
        if S == 'L':
            self.X = Player.init_position_L
            self.Y = random.randint(0,1000 - 450)
            self.V = Player.init_velocity
            self.P = 'L'
            self.life = 5
            self.counter = [1000,1000,1000]
            self.SIZE = Player.gun_SIZE
            self.rect = pygame.Rect(self.X,self.Y,self.SIZE[0],self.SIZE[1])
            self.image = Player.gunner_red_L
            self.temp = 0
            self.bullet = True
        elif S == 'R':
            self.X = Player.init_position_R
            self.Y = random.randint(0,1000 - 450)
            self.V = Player.init_velocity
            self.P = 'R'
            self.life = 5
            self.counter = [1000,1000,1000]
            self.SIZE = Player.gun_SIZE
            self.rect = pygame.Rect(self.X,self.Y,self.SIZE[0],self.SIZE[1])
            self.image = Player.gunner_blue_R
            self.temp = 0
            self.bullet = True
    def is_dead(self):
        '''function to check dead or not'''
        if self.life <= 0:
            self.counter = [10000,10000,10000]
            self.image_change_to_dead()
            self.V = 0
    def shot(self):
        '''shot the bullet'''
        self.bullet = False
        self.counter[2] = 0
        self.image_change_to_nor()
        if self.P == 'L':
            newbullet = Bullet('L',self.X+65,self.Y+13)
            bullet_L.append(newbullet)
        if self.P == 'R':
            newbullet = Bullet('R',self.X-20,self.Y+13)
            bullet_L.append(newbullet)
    def reload(self):
        '''reload the bullet'''
        self.bullet = True
        self.image_change_to_gun()
    def is_shot(self):
        '''handle the condition od got shot'''
        self.life -= 1
        self.image_change_to_shot()
        self.counter[1] = 0
        self.is_dead()
    def is_in_area(self):
        '''if the player is out of screen'''
        if self.Y > 1000 - 450 or self.Y < 0:
            return False
        return True        
    '''method to change image'''
    def image_change_to_nor(self):
        if self.P == 'L':
            self.image = Player.normal_red_L
            self.SIZE = Player.nor_SIZE
            self.rect.width = 60
        elif self.P == 'R':
            self.image = Player.normal_blue_R
            self.SIZE = Player.nor_SIZE
            self.rect.width = 60
    def image_change_to_gun(self):
        if self.P == 'L':
            self.image = Player.gunner_red_L
            self.SIZE = Player.gun_SIZE
            self.rect.width = 70
        elif self.P == 'R':
            self.image = Player.gunner_blue_R
            self.SIZE = Player.gun_SIZE
            self.rect.width = 70
    def image_change_to_dead(self):
        if self.P == 'L':
            self.image = Player.DEAD_red_L
        elif self.P == 'R':
            self.image = Player.DEAD_blue_R
    def image_change_to_shot(self):
        if self.bullet == True:
            if self.P == 'L':
                self.image = Player.shot_gun_L
                self.SIZE = Player.gun_SIZE
                self.rect.width = 70
            elif self.P == 'R':
                self.image = Player.shot_gun_R
                self.SIZE = Player.gun_SIZE
                self.rect.width = 70
        elif self.bullet == False:
            if self.P == 'L':
                self.image = Player.shot_nor_L
                self.SIZE = Player.nor_SIZE
                self.rect.width = 60
            elif self.P == 'R':
                self.image = Player.shot_nor_R
                self.SIZE = Player.nor_SIZE
                self.rect.width = 60
    def move(self):
        '''update the position'''
        self.Y += self.V
        self.rect.topleft = (self.X,self.Y)
        if not self.is_in_area():
            self.V *= -1

class Bullet():
    '''clas to represent a bullet'''
    bullet_image = pygame.image.load('bullet_circle.png')
    bullet_image = pygame.transform.scale(bullet_image, (20,20))
    init_velocity_x = 20
    init_velocity_y = 0
    bullet_size = (20,20)
    def __init__(self,S,X,Y,VX = 0,VY = 0):
        '''method to initialize a bullet object'''
        if S == 'L':
            self.X = X
            self.Y = Y
            self.V_x = Bullet.init_velocity_x
            self.V_y = Bullet.init_velocity_y
            self.image = Bullet.bullet_image
            self.rect = pygame.Rect(self.X,self.Y,Bullet.bullet_size[0],Bullet.bullet_size[1])
            self.radius = 10
        if S == 'R':
            self.X = X
            self.Y = Y
            self.V_x = Bullet.init_velocity_x * -1
            self.V_y = Bullet.init_velocity_y
            self.image = Bullet.bullet_image
            self.rect = pygame.Rect(self.X,self.Y,Bullet.bullet_size[0],Bullet.bullet_size[1])
            self.radius = 10
        if S == None:
            self.X = X
            self.Y = Y
            self.V_x = VX
            self.V_y = VY
            self.image = Bullet.bullet_image
            self.rect = pygame.Rect(self.X,self.Y,Bullet.bullet_size[0],Bullet.bullet_size[1])
            self.radius = 10
    def is_in_area_x(self):
        '''determine if the bullet is in the screen'''
        if self.X < -20 or self.X > 1020:
            return False
        return True
    def is_in_area_y(self):
        '''determine if the bullet is in the screen'''
        if self.Y < 0 or self.Y > 600-20:
            return False
        return True
    def move(self):
        '''function to handle the update of bullet'''
        self.X += self.V_x
        self.Y += self.V_y
        self.rect.topleft = (self.X,self.Y)
        if not self.is_in_area_y():
            self.V_y *= -1
        if not self.is_in_area_x():
            bullet_L.remove(self)

class Plant():
    '''class to represent a plant'''
    plant_image = pygame.image.load('plant.png')
    plant_image = pygame.transform.scale(plant_image, (40,50))
    SIZE = (40,50)
    init_life = 3
    counter = 250
    def __init__(self):
        '''method to initialize a plant'''
        self.X = random.randint(200,760)
        self.Y = random.randint(0,550)
        self.life = Plant.init_life
        self.image = Plant.plant_image
        self.rect = pygame.Rect(self.X,self.Y,Plant.SIZE[0],Plant.SIZE[1])
        self.radius = 20
    def check_alive(self):
        '''method to check the Durability'''
        if self.life > 0:
            return None
        if self.life <= 0:
            plant_L.remove(self)
    def hit(self):
        '''method to handle collision with bullet'''
        self.life -= 1

class Stone():
    '''class to represent a stone'''
    stone_image = pygame.image.load('stone.png')
    stone_image = pygame.transform.scale(stone_image, (32,24))
    SIZE = (32,24)
    counter = 200
    def __init__(self):
        '''initialize a new stone object'''
        self.X = random.randint(200,760)
        self.Y = random.randint(0,560)
        self.image = Stone.stone_image
        self.rect = pygame.Rect(self.X,self.Y,Stone.SIZE[0],Stone.SIZE[1])
        self.radius = 12
        
class Bucket():
    '''class to represent a bucket object'''
    bucket_image = pygame.image.load('bucket_body.png')
    bucket_image = pygame.transform.scale(bucket_image, (40,50))
    SIZE = (40,50)
    counter = 200
    def __init__(self):
        '''initialize a bucket object'''
        self.X = random.randint(200,760)
        self.Y = random.randint(0,560)
        self.image = Bucket.bucket_image
        #self.shadow = Bucket.shadow_image
        self.rect = pygame.Rect(self.X,self.Y,Bucket.SIZE[0],Bucket.SIZE[1])
        self.radius = 20

def collision_bullet_and_plant():
    '''function to handle all the collision between bullet and plant'''
    global bullet_L,plant_L
    #use two for loops to check all pair of objects
    for bullet in bullet_L:
        for plant in plant_L:
            if pygame.sprite.collide_circle(bullet,plant) and bullet in bullet_L:
                plant.hit()
                dx = bullet.rect.center[0] - plant.rect.center[0]
                dy = bullet.rect.center[1] - plant.rect.center[1]
                plant.check_alive()
                if bullet.V_x**2 + bullet.V_y**2 < (Bullet.init_velocity_x - 1)**2:
                    bullet.V_x *= 4
                    bullet.V_y *= 4
                if dx == 0:
                    bullet.V_y *= -1
                    continue
                if dy == 0:
                    bullet.V_x *= -1
                    continue
                #check four case of ollision to determine the velocity of bullet
                if dx > 0 and dy < 0:
                    theta = math.atan(abs(dy/dx))
                    VT = -1*bullet.V_x*math.cos(theta) + -1*bullet.V_y*math.sin(theta)
                    VN = -1*bullet.V_x*math.sin(theta) + bullet.V_y*math.cos(theta)
                    bullet.V_x = VT*math.cos(theta) + -1*VN*math.sin(theta)
                    bullet.V_y = -1*VT*math.sin(theta) + -1*VN*math.cos(theta)
                    continue
                if dx < 0 and dy < 0:
                    theta = math.atan(abs(dy/dx))
                    VT = bullet.V_x*math.cos(theta) + bullet.V_y*math.sin(theta)
                    VN = bullet.V_x*math.sin(theta) + -1*bullet.V_y*math.cos(theta)
                    bullet.V_x = -1*VT*math.cos(theta) + VN*math.sin(theta)
                    bullet.V_y = -1*VT*math.sin(theta) + -1*VN*math.cos(theta)
                    continue
                if dx < 0 and dy > 0:
                    theta = math.atan(abs(dy/dx))
                    VT = bullet.V_x*math.cos(theta) + -1*bullet.V_y*math.sin(theta)
                    VN = -1*bullet.V_x*math.sin(theta) + -1*bullet.V_y*math.cos(theta)
                    bullet.V_x = -1*VT*math.cos(theta) + -1*VN*math.sin(theta)
                    bullet.V_y = VT*math.sin(theta) + -1*VN*math.cos(theta)
                    continue 
                if dx > 0 and dy > 0:
                    theta = math.atan(abs(dy/dx))
                    VT = -1*bullet.V_x*math.cos(theta) + -1*bullet.V_y*math.sin(theta)
                    VN = bullet.V_x*math.sin(theta) + -1*bullet.V_y*math.cos(theta)
                    VT *= -1
                    bullet.V_x = -1*VT*math.cos(theta) + VN*math.sin(theta)
                    bullet.V_y = -1*VT*math.sin(theta) + -1*VN*math.cos(theta)
                    continue
    return None
def collision_bullet_and_stone():
    '''function to handle all the collision between bullet and stone'''
    global stone_L,bullet_L
    for bullet in bullet_L:
        for stone in stone_L:
            if pygame.sprite.collide_circle(bullet,stone) and bullet in bullet_L:
                stone_L.remove(stone)
                VTX = bullet.V_x
                VTY = bullet.V_y
                TX = bullet.X
                TY = bullet.Y
                bullet_L.remove(bullet)
                theta = 10/360*2*math.pi
                Vnew1 = (VTX*math.cos(theta)+VTY*math.sin(theta),VTX*-1*math.sin(theta)+VTY*math.cos(theta))
                Vnew2 = (VTX*math.cos(-1*theta)+VTY*math.sin(-1*theta),VTX*-1*math.sin(-1*theta)+VTY*math.cos(-1*theta))
                newbullet1 = Bullet(None,TX,TY,Vnew1[0],Vnew1[1])
                newbullet2 = Bullet(None,TX,TY,Vnew2[0],Vnew2[1])
                bullet_L.append(newbullet1)
                bullet_L.append(newbullet2)
    return None
def collision_bullet_and_bucket():
    '''function to handle all the collision between bullet and bucket'''
    for bullet in bullet_L:
        for bucket in bucket_L:
            if pygame.sprite.collide_circle(bullet,bucket):
                bucket_L.remove(bucket)
                if bullet.V_x**2+bullet.V_y**2 > 18**2:
                    bullet.V_x *= 0.25
                    bullet.V_y *= 0.25
    return None
def collision_bullet_and_Player():
    '''function to handle all the collision between player and bullet'''
    global P1,P2
    for bullet in bullet_L:
        if pygame.Rect.colliderect(P1.rect,bullet.rect):
            P1.is_shot()
            bullet_L.remove(bullet)
            continue
        if pygame.Rect.colliderect(P2.rect,bullet.rect):
            P2.is_shot()
            bullet_L.remove(bullet)
            continue
def collision_plant_and_stone():
    '''function to handle all collision between plant and stone'''
    for stone in stone_L:
        for plant in plant_L:
            if pygame.sprite.collide_circle(plant,stone):
                dice = random.randint(1,2)
                if dice == 1:
                    stone_L.remove(stone)
                if dice == 2:
                    plant_L.remove(plant)
    return None
def collision_plant_and_bucket():
    '''function to handle all collision between plant and bucket'''
    for plant in plant_L:
        for bucket in bucket_L:
            if pygame.sprite.collide_circle(plant,bucket):
                dice = random.randint(1,2)
                if dice == 1:
                    bucket_L.remove(bucket)
                if dice == 2:
                    plant_L.remove(plant)
###################################################################################################################
pygame.init()
screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption('Micro Battles 3  Ver0.0.0')
start_image = pygame.image.load('Start.png')
start_image = pygame.transform.scale(start_image,(750,300))
NO_infinite = False
clock = pygame.time.Clock()
pygame.mixer.music.load('Persona 5 - Last Surprise 8-bit.mp3')
gun_shot = pygame.mixer.Sound('BULLET.wav')
font = pygame.font.SysFont("comicsansms", 40)
Title_font = pygame.font.SysFont("comicsansms", 60)
button_font = pygame.font.SysFont("comicsansms", 20)
TITLE = Title_font.render('Micro Battles', True, (0,0,0))
AGAIN = Title_font.render('press R go back to start scene', True, (0,0,0))
REDWIN = Title_font.render('Player1 WIN!!!', True, (0,0,0))
BLUEWIN = Title_font.render('Player2 WIN!!!', True, (0,0,0))
DRAW = Title_font.render('Draw',True, (0,0,0))

while not NO_infinite:
    #two flag to determine if players want another game after finish
    flag1 = False
    flag2 = False
    #assume that players play only one turn
    NO_infinite = True
    start = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                #if event.key == pygame.K_s:
                start = False
        screen.fill((255,195,77))
        START = button_font.render('press any button to start game', True, (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        screen.blit(TITLE,(500 - TITLE.get_width() // 2, 75 - TITLE.get_height() // 2))
        screen.blit(start_image,(125,150))
        screen.blit(START,(500 - START.get_width() // 2, 525 - START.get_height() // 2))
        pygame.display.flip()
    P1 = Player('L')
    P2 = Player('R')
    player_L = [P1,P2]
    bullet_L = []
    plant_L = []
    stone_L = []
    bucket_L = []
    stone_counter = 0
    plant_counter = 0
    bucket_counter = 0
    done = False
    weapon_lock = False
    
    pygame.mixer.music.play(-1)
    
    while not done:
        for counter in range(0,3):
            P1.counter[counter] += 1
            P2.counter[counter] += 1
        stone_counter += 1
        plant_counter += 1
        bucket_counter += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                #P1 control
                if event.key == pygame.K_a and not weapon_lock:
                    if P1.bullet:
                        P1.counter[0] = 0
                        P1.counter[2] = 0
                        P1.temp = P1.V
                        P1.V = 0
                        gun_shot.play()
                        P1.shot()
                    else:
                        P1.V *= -1
                #P2 control
                if event.key == pygame.K_l and not weapon_lock:
                    if P2.bullet:
                        P2.counter[0] = 0
                        P2.counter[2] = 0
                        P2.temp = P2.V
                        P2.V = 0
                        gun_shot.play()
                        P2.shot()
                    else:
                        P2.V *= -1
                if event.key == pygame.K_r and flag1 == True:
                    NO_infinite = False
                    flag2 = True
        screen.fill((191, 128, 64))
        #204 136 0
        #255 195 77
        
        #check stop, white and bullet reloading
        if P1.counter[0] == Player.stop_time:
            P1.V = P1.temp
        if P2.counter[0] == Player.stop_time:
            P2.V = P2.temp
        if P1.counter[1] == Player.white_time:
            if P1.bullet:
                P1.image_change_to_gun()
            else:
                P1.image_change_to_nor()
        if P2.counter[1] == Player.white_time:
            if P2.bullet:
                P2.image_change_to_gun()
            else:
                P2.image_change_to_nor()
        if P1.counter[2] == Player.reload_time:
            P1.reload()
        if P2.counter[2] == Player.reload_time:
            P2.reload()
            
        #generate new plant and stone in screen
        if plant_counter == Plant.counter and len(plant_L) <= 15:
            T = Plant()
            plant_L.append(T)
            plant_counter = 0
        if stone_counter == Stone.counter and len(stone_L) <= 15:
            T = Stone()
            stone_L.append(T)
            stone_counter = 0
        if bucket_counter == Bucket.counter and len(bucket_L) <= 15:
            T = Bucket()
            bucket_L.append(T)
            bucket_counter = 0
            
        #update all the object in List
        for elem in player_L:
            elem.move()
            screen.blit(elem.image,(elem.X,elem.Y))
        for elem in plant_L:
            elem.check_alive()
            screen.blit(elem.image,(elem.X,elem.Y))
        for elem in stone_L:
            screen.blit(elem.image,(elem.X,elem.Y))
        for elem in bullet_L:
            elem.move()
            screen.blit(elem.image,(elem.X,elem.Y))
        for elem in bucket_L:
            screen.blit(elem.image,(elem.X,elem.Y))
        #handla all the collision
        collision_bullet_and_plant()
        collision_bullet_and_stone()
        collision_bullet_and_Player()
        collision_plant_and_stone()
        collision_bullet_and_bucket()
        #update the score
        score1 = font.render(f' {5 - P2.life} ', True, (0, 0, 0))
        score2 = font.render(f' {5 - P1.life} ', True, (0, 0, 0))
        screen.blit(score1,(70, 0))
        screen.blit(score2,(870, 0))
        
        #check if someone has dead and print winner message
        if P1.life <= 0 and P2.life > 0:
            screen.blit(BLUEWIN,(500 - REDWIN.get_width() // 2, 200 - REDWIN.get_height() // 2))
            screen.blit(AGAIN,(500 - AGAIN.get_width() // 2, 300 - AGAIN.get_height() // 2))
            flag1 = True
            weapon_lock = True
        if P2.life <= 0 and P1.life > 0:
            screen.blit(REDWIN,(500 - BLUEWIN.get_width() // 2, 200 - BLUEWIN.get_height() // 2))
            screen.blit(AGAIN,(500 - AGAIN.get_width() // 2, 300 - AGAIN.get_height() // 2))
            flag1 = True
            weapon_lock = True
        if P1.life <= 0 and P2.life <= 0:
            screen.blit(DRAW,(500 - DRAW.get_width() // 2, 200 - DRAW.get_height() // 2))
            screen.blit(AGAIN,(500 - AGAIN.get_width() // 2, 300 - AGAIN.get_height() // 2))
            flag1 = True
            weapon_lock = True
        #
        if flag2:
            break
        pygame.display.flip()
        clock.tick(60)
pygame.quit()
exit()