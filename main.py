import pygame
from Models.stone import stoneRock
from Models.Player import playerSprite
#from Models.circle import circle
import Pictures
pygame.init()

win = pygame.display.set_mode((500, 500));
bear = pygame.image.load("Pictures/Mock1.png")
swbear = pygame.image.load("Pictures/Mock_Sweeper_1.png")
smbear = pygame.image.load("Pictures/Mock_Sweeper_2.png")
rect = bear.get_rect()
pygame.display.set_caption("First Game")
clock = pygame.time.Clock()
x = 50
y = 50
width = 40
height = 60
vel = 5
run = True

while run:
   # pygame.time.delay(
    #    20)  # This will delay the game the given amount of milliseconds. In our casee 0.1 seconds will be the delay

    for event in pygame.event.get():  # This will loop through a list of any keyboard or mouse events.
        if event.type == pygame.QUIT:  # Checks if the red button in the corner of the window is clicked
            run = False  # Ends the game loop
    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pressed()

    if keys[pygame.K_LEFT]:  # We can check if a key is pressed like this
        x-= vel/2
    if keys[pygame.K_RIGHT]:
        x += vel/2
    if keys[pygame.K_UP]:
        y -= vel

    if keys[pygame.K_DOWN]:
        y += vel
    if mouse[0]:
        y-= vel

    win.fill((255, 255, 255))
    #win.blit(bear, rect)
    #pygame.draw(win, bear, rect, 1)
    bear1 = pygame.transform.scale(swbear, (100, 100))
    bear2 = pygame.transform.scale(smbear, (100, 100))
    win.blit(bear1, (x, y))
    pygame.draw.circle(win, (255, 0, 0), (400, 50), 20)
    pygame.draw.circle(win, (255, 0, 0), (x, y), 20)  # This takes: window/surface, color, rect
    pygame.display.update()
    pygame.time.delay(10);
    win.blit(bear2, (x, y))
    pygame.draw.circle(win, (0, 255, 0), (x, y), 20)
    pygame.display.update()  # This updates the screen so we can see our rectangle
    pygame.time.delay(10);

pygame.quit()  # If we exit the loop this will execute and close our game
