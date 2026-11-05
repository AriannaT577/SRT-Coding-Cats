import pygame
import random

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


# --- Class Definition ---

class rectangle:
    def __init__(self):
        #x and y positions
        self.x = random.randrange(0, 700)
        self.y = random.randrange(0, 500)

        #sizes aka width and height
        self.width = random.randrange(20, 70)
        self.height = random.randrange(20, 70)

        #movement
        self.change_x = random.choice([-3, -2, -1, 1, 2, 3])
        self.change_y = random.choice([-3, -2, -1, 1, 2, 3])

        #randomg colours
        self.color = (random.randrange(0, 256),
                      random.randrange(0, 256),
                      random.randrange(0, 256))

    def draw(self, screen):
        #draw a rectangle
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.width, self.height])

    def move(self):
        #basically make it move
        self.x += self.change_x
        self.y += self.change_y

        #bounce off the edges
        if self.x < 0:
            self.x = 0
            self.change_x *= -1
        elif self.x + self.width > 700:
            self.x = 700 - self.width
            self.change_x *= -1
        if self.y < 0:
            self.y = 0
            self.change_y *= -1
        elif self.y + self.height > 500:
            self.y = 500 - self.height
            self.change_y *= -1

class ellipse(rectangle):
#uses the settings from rectange
    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, [self.x, self.y, self.width, self.height])

class triangle(rectangle):
    def draw(self, screen):
        point1 = (self.x + self.width // 2, self.y)     
        point2 = (self.x, self.y + self.height)        
        point3 = (self.x + self.width, self.y + self.height) 
        pygame.draw.polygon(screen, self.color, [point1, point2, point3])


pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("classes")

done = False
clock = pygame.time.Clock()

#lists
my_list = []

#rectanges
for i in range(200):
    my_object = rectangle()
    my_list.append(my_object)

#a ellipses
for i in range(200):
    my_object = ellipse()
    my_list.append(my_object)

#a ellipses
for i in range(200):
    my_object = triangle()
    my_list.append(my_object)

# --- Main Program Loop ---
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #moving all the stuffs
    for item in my_list:
        item.move()

    screen.fill(BLACK)

    #all the drawings of shapes n stuff
    for item in my_list:
        item.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()