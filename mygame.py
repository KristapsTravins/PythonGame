import sys
import pygame
import os
import random

pygame.init()

size = width, height = 600, 700
speed = [2, 2]
black = 0, 0, 0
move = 4.5

# init space crueser and roid .png is 124x127
spaceCrouser = pygame.image.load(os.path.join('shutle.png'))
roid = pygame.image.load(os.path.join('roid.png'))
# init disp

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Avoid the asteroids")
#loosing screen

def loose():
    pygame.font.init()
    run = True
    screen.fill((0, 0, 0))
    myfont = pygame.font.SysFont('Ubuntu', 40)
    textsurface = myfont.render('GAME OVER', False, (255, 255, 255))
    screen.blit(textsurface, (170, 300))
    pygame.display.update()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False



# Drawing table
def drawTable(shuttle, roids):
    screen.fill((255, 255, 255))
    screen.blit(spaceCrouser, (shuttle.x, shuttle.y))
    screen.blit(roid, (roids.x, roids.y))
    pygame.display.update()



def main():
    shuttle = pygame.Rect(230, 590, 80, 50)
    roid = pygame.Rect(230, -112, 80, 50)

    clock = pygame.time.Clock()
    runtime = True
    while runtime:
        drawTable(shuttle, roid)
        clock.tick(70)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                runtime = False

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT]:
            if shuttle.x <= -25:
                shuttle.x = -25
            shuttle.x -= move

        if keys_pressed[pygame.K_RIGHT]:
            if shuttle.x >= width - 100:
                shuttle.x = width - 100
            shuttle.x += move

        if roid.y > 700:
            roid.y = -112
            roid.x = random.randint(-25, width - 100)

        roid.y += 5.5
        if roid.colliderect(shuttle):
            loose()
            runtime = False




main()
