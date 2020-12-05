import pygame

#initialising pygame and screen window
pygame.init()
screen = pygame.display.set_mode((800,600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('player.png')
playX = 370
playY = 480

def player ():
    screen.blit(playerImg,(playX,playY))


# Game loop
running = True
while running :

    #RGB
    screen.fill((0 , 0 , 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    player()
    pygame.display.update()
