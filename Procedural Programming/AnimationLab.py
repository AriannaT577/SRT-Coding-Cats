import pygame
import random 

#COLOURS!
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
CREAM = (247, 231, 190)
PINK = (255, 182, 193)
BRIGHTPINK = (215, 53, 230)
DARKBLUE = (10, 67, 118)

RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)

pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Animation: Nyan Cat")

done = False
clock = pygame.time.Clock()

frame_counter = 0
frame = 0

 # ----- rainbow drawing -----
def rainbow_draw(screen, x_position, y_offset):
    pygame.draw.rect(screen, RED, (x_position, 160 + y_offset, 60, 15))
    pygame.draw.rect(screen, ORANGE, (x_position, 175 + y_offset, 60, 15))
    pygame.draw.rect(screen, YELLOW, (x_position, 190 + y_offset, 60, 15))
    pygame.draw.rect(screen, GREEN, (x_position, 205 + y_offset, 60, 15))
    pygame.draw.rect(screen, BLUE, (x_position, 220 + y_offset, 60, 15))
    pygame.draw.rect(screen, PURPLE, (x_position, 235 + y_offset, 60, 15))
    
def cat_body(body_y_offset):
    #body
    pygame.draw.rect(screen, CREAM, (350, 150 + body_y_offset, 200, 120))
    pygame.draw.rect(screen, PINK, (360, 160 + body_y_offset, 175, 100))
    pygame.draw.rect(screen, BLACK, (350, 150 + body_y_offset, 200, 120), 3)

def cat_head(head_y_offset):
    # Ears
    pygame.draw.rect(screen, GRAY, (510 + head_x_offset, 160 + head_y_offset, 20, 30))
    pygame.draw.rect(screen, BLACK, (510 + head_x_offset, 160 + head_y_offset, 20, 30), 3)
    pygame.draw.rect(screen, GRAY, (580 + head_x_offset, 160 + head_y_offset, 20, 30))
    pygame.draw.rect(screen, BLACK, (580 + head_x_offset, 160 + head_y_offset, 20, 30), 3)
    # Head
    pygame.draw.rect(screen, GRAY, (510 + head_x_offset, 185 + head_y_offset, 90, 80))
    pygame.draw.rect(screen, BLACK, (510 + head_x_offset, 185 + head_y_offset, 90, 80), 3)
    # Eyes
    pygame.draw.circle(screen, BLACK, (535 + head_x_offset, 220-5 + head_y_offset), 5)
    pygame.draw.circle(screen, BLACK, (575 + head_x_offset, 220-5 + head_y_offset), 5)
    # Mouth :3
    pygame.draw.rect(screen, BLACK, (552 + head_x_offset, 245-5 + head_y_offset, 5, 8))
    pygame.draw.arc(screen, BLACK, (540 + head_x_offset, 240-5 + head_y_offset, 30, 15), 3.14, 0, 2)
def cat_paws():
    #back paw
    pygame.draw.rect(screen, GRAY, (360, 245 + leg_y_offset, 25, 25))
    pygame.draw.rect(screen, BLACK, (360, 245 + leg_y_offset, 25, 25), 3)
    pygame.draw.rect(screen, GRAY, (390, 245 + leg_y_offset, 25, 25))
    pygame.draw.rect(screen, BLACK, (390, 245 + leg_y_offset, 25, 25), 3)
    #front paw
    pygame.draw.rect(screen, GRAY, (480, 245 + leg_y_offset, 25, 25))
    pygame.draw.rect(screen, BLACK, (480, 245 + leg_y_offset, 25, 25), 3)
    pygame.draw.rect(screen, GRAY, (510, 245 + leg_y_offset, 25, 25))
    pygame.draw.rect(screen, BLACK, (510, 245 + leg_y_offset, 25, 25), 3)

NUM_STARS = 50
stars = [[random.randint(0, size[0]), random.randint(0, size[1])] for _ in range(NUM_STARS)]

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(DARKBLUE)
    
    frame_counter += 1
    if frame_counter % 15 == 0:
        frame = (frame + 1) % 2

    if frame == 0:
        leg_y_offset = 10
        rainbow_y_offset_1 = -5
        rainbow_y_offset_0 = 0
        body_y_offset = -2
        head_y_offset = -3
        head_x_offset = +1
    else:
        leg_y_offset = 15
        rainbow_y_offset_1 = 0
        rainbow_y_offset_0 = -5
        body_y_offset = 0
        head_y_offset = 0
        head_x_offset = 0

    for star in stars:
        star[0] -= 12  # speed of star movement
        if star[0] < 0:
            star[0] = size[0]
            star[1] = random.randint(0, size[1])
        pygame.draw.circle(screen, WHITE, star, 2)
    
    for i in range(6):
        rainbow_x = i * 60
        if i % 2 == 0:
            rainbow_draw(screen, rainbow_x, rainbow_y_offset_1)
        else:
            rainbow_draw(screen, rainbow_x, rainbow_y_offset_0)
    cat_paws()
    cat_body(body_y_offset)
    cat_head(head_y_offset)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
