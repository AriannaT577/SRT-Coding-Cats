import pygame

#COLOURS!
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("title")

done = False

clock = pygame.time.Clock()
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

# --- Game logic should go here
# --- Screen-clearing code goes here
screen.fill(WHITE)

pygame.display.flip()

clock.tick(60)

pygame.quit()