#i made a python version bc i was figuring out the logic. try it out if u want lol but its just logic stuff
import pygame
import random

pygame.init()

WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("rotator test")

clock = pygame.time.Clock()

colors = {
    "red": 0.277,
    "orange": 0.333,
    "yellow": 0.388,
    "sage": 0.444,
    "green": 0.5,
    "azure": 0.555,
    "blue": 0.611,
    "violet": 0.722,
    "white": 1.0
}

color_rgb = {
    "red": (255, 0, 0),
    "orange": (255, 165, 0),
    "yellow": (255, 255, 0),
    "sage": (188, 184, 138),
    "green": (0, 255, 0),
    "azure": (0, 127, 255),
    "blue": (0, 0, 255),
    "violet": (138, 43, 226),
    "white": (255, 255, 255)
}

color_names = list(colors.keys())

actionValue = 0

current_color_name = random.choice(color_names)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        #mouse click as the action, but it would be the actions for meghan
        if event.type == pygame.MOUSEBUTTONDOWN:
            actionValue += 1
            # Randomly pick a new color
            current_color_name = random.choice(color_names)
            print(f"Click #{actionValue}, Color: {current_color_name}, Servo Value: {colors[current_color_name]}")

    screen.fill(color_rgb[current_color_name])
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()