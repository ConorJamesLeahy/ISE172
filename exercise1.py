"""
    Create a display surface and caption it. Download an image of a small ball and
    import that image into your program.
    Create a horizontal ground of some thickness (something similar to what we saw
    in the aliens game). Let the initial position of this ball be on this ground.
    
    Write code such that the ball bounces between this ground and the top boundary
    of your display surface. That is, the ball keeps bouncing up and down and up and
    down and (you guessed it ;-))
    
    Note: Try to play around with colors as well. Also play with the frame speed.
    Hint: Recall that any action can be performed by writing code for various events.
            How to bounce the ball once it hits the ground or the boundary?
"""

import pygame, sys
 



def main():
    # Write your pygame code (the "while" loop) in this "main" function.
    pygame.init()
    
    win = pygame.display.set_mode((500,500))
    pygame.display.set_caption("First Game")
    
    gameExit = False


    while not gameExit:

         for event in pygame.event.get():
             #print(event)
             if event.type == pygame.QUIT:
                 gameExit = True


    pygame.quit()
    
   

if __name__ == '__main__':
    main()
