import pygame
import time

pygame.init()
screen = pygame.display.set_mode([500, 500])
cpt = 0
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (cpt, 0, 255), (250, 250), 75)

    # Flip the display
    pygame.display.flip()
    if cpt < 255:
        cpt +=1

    print(cpt)
    time.sleep(0.1)


# Done! Time to quit.
pygame.quit()
