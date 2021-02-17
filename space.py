# tutorial on pygame:  https://www.youtube.com/watch?v=FfWpgLFMI7w
import pygame

#initializa the pygagme
pygame.init()

#create the screen
screen = pygame.display.set_mode((800,600))


#Game Loop
running = True
while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
