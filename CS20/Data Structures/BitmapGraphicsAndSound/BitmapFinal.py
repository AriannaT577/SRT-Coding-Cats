import pygame
import sys
import os

#file directory bc vs is stinky
script_dir = os.path.dirname(__file__)
img_path = os.path.join(script_dir, "background.jpg")
cat_path = os.path.join(script_dir, "cat.png")
meow_path = os.path.join(script_dir, "Meow.ogg")
bg_path = os.path.join(script_dir, "BgMusic.mp3")


#colouring ur mom har har
WHITE = (255, 255, 255)
GREY = (160, 160, 160)
GREY_BUT_EMO = (100, 100, 100)
PINK = (255, 170, 180)
BLACK = (0, 0, 0)
BROWN = (150, 100, 60)

#def draw_cat(screen, x, y):
    #pygame.draw.ellipse(screen, GREY, (x, y, 120, 60))
    #pygame.draw.circle(screen, GREY, (x + 120, y + 30), 25)
    #pygame.draw.polygon(screen, GREY_BUT_EMO, [(x + 105, y + 10), (x + 115, y - 10), (x + 125, y + 10)])
    #pygame.draw.polygon(screen, GREY_BUT_EMO, [(x + 125, y + 10), (x + 135, y - 10), (x + 145, y + 10)])
    #pygame.draw.circle(screen, GREY_BUT_EMO, (x + 115, y + 30), 3)
    #pygame.draw.circle(screen, GREY_BUT_EMO, (x + 130, y + 30), 3)
    #pygame.draw.line(screen, GREY_BUT_EMO, (x, y + 30), (x - 40, y + 10), 6)

def draw_mouse(screen, x, y):
    pygame.draw.ellipse(screen, BROWN, (x, y, 60, 35))
    pygame.draw.circle(screen, BROWN, (x + 60, y + 18), 15)
    pygame.draw.circle(screen, PINK, (x + 55, y + 5), 8)
    pygame.draw.circle(screen, PINK, (x + 70, y + 5), 8)
    pygame.draw.circle(screen, BLACK, (x + 65, y + 18), 3)
    pygame.draw.line(screen, PINK, (x, y + 18), (x - 30, y + 25), 3)

pygame.init()
pygame.mixer.init()
WIDTH, HEIGHT = 700, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))

raw_background = pygame.image.load(img_path).convert()
background_image = pygame.transform.scale(raw_background, (WIDTH, HEIGHT))
meow_sound = pygame.mixer.Sound(meow_path)
bg_sound = pygame.mixer.Sound(bg_path)
bg_sound.play()

clock = pygame.time.Clock()
pygame.display.set_caption("kat n mouse 3.0")

raw_cat = pygame.image.load(cat_path).convert()
cat_sprite = pygame.transform.scale(raw_cat, (120, 100))
cat_sprite.set_colorkey(BLACK)
cat_x, cat_y = 200, 300
cat_speed = 5

done = False
pygame.mouse.set_visible(True) 

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and meow_sound:
                meow_sound.play()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        cat_x -= cat_speed
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        cat_x += cat_speed
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        cat_y -= cat_speed
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        cat_y += cat_speed

    #kat boundaries
    cat_x = max(0, min(WIDTH - 150, cat_x))
    cat_y = max(0, min(HEIGHT - 80, cat_y))

    #mouse follows mouse haha pun
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_x = max(0, min(WIDTH - 90, mouse_x))
    mouse_y = max(0, min(HEIGHT - 50, mouse_y))
    
    screen.blit(background_image, [0, 0])
    screen.blit(cat_sprite, [cat_x, cat_y])
    #draw_cat(screen, cat_x, cat_y)
    draw_mouse(screen, mouse_x, mouse_y)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
