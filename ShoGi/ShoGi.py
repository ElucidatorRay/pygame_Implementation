import pygame
import random
import math
from sys import exit




pygame.init()
screen = pygame.display.set_mode((1100,700))
pygame.display.set_caption('ShoGi')
clock = pygame.time.Clock()
board_img = pygame.image.load('棋盤.jpg')
board_img = pygame.transform.scale(board_img,(700,700))
start = True

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
    screen.blit(board_img,(0,0))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
exit()