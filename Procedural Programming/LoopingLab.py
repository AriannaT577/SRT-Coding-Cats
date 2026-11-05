#1
print1 = 10
for row1 in range(9):
    for column1 in range(row1+1):
        print (print1,end=" ")
        print1 += 1
    print()

#2
n2 = int(input("Length of the box? "))
print("o" * (n2*2))
for i in range (n2-2):
    print("o" + " " * ((n2*2) - 2) + "o")
print("o" * (n2*2))

#3 idk how it works
n3 = int(input("number idk? "))


#4
import pygame
#COLOURS!
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("IntroToGraphics: Nyan Cat")
done = False
clock = pygame.time.Clock()
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(BLACK)
    #drawing
    x4 = 0
    y4 = 0
    for i in range (200):
        x4 = 0
        for j in range (200):
            pygame.draw.rect(screen, GREEN, (x4, y4, 12, 12))
            x4 += 20
        y4 += 20

    pygame.display.flip()
    clock.tick(60)
pygame.quit()

