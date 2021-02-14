import pygame
import random
from Models.stone import stoneRock
from Models.Player import Stone
# from Models.circle import circle
import Pictures

pygame.init()
iteration = 0;
stonepost = Stone(50, 50, random.randint(80, 120), 10, 20, 1)
win = pygame.display.set_mode((500, 500));
bear = pygame.image.load("Pictures/Mock1.png")
bbear = pygame.image.load("Pictures/GB_back.png")
bbthrow1 = pygame.image.load("Pictures/GB_throw1.png")
bbthrow2 = pygame.image.load("Pictures/GB_throw2.png")
bbthrow3 = pygame.image.load("Pictures/GB_throw3.png")
bbsweep1 = pygame.image.load("Pictures/GB_sweep1.png")
bbsweep2 = pygame.image.load("Pictures/GB_sweep2.png")
house = pygame.image.load("Pictures/House.png")
rect = bear.get_rect()
pygame.display.set_caption("First Game")
clock = pygame.time.Clock()
x = win.get_width() / 2 + stonepost.radius
y = win.get_height() - stonepost.radius * 2
width = 40
height = 60
vel = 5
run = True
set = 0;
fps = 30;
initdelay = 30
swap = 1;
bob = False;
currteam = True;
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
distance = 0;
speedcap = 100
arrayred = [];  # Grizzly
arrayblue = [];  # Polar
gocount = 0;


def main(team):
    iteration = 0;
    stonepost = Stone(50, 50, random.randint(80, 120), 10, 20, 1)
    win = pygame.display.set_mode((500, 500));
    bear = pygame.image.load("Pictures/Mock1.png")
    bbear = pygame.image.load("Pictures/GB_back.png")
    bbthrow1 = pygame.image.load("Pictures/GB_throw1.png")
    bbthrow2 = pygame.image.load("Pictures/GB_throw2.png")
    bbthrow3 = pygame.image.load("Pictures/GB_throw3.png")
    bbsweep1 = pygame.image.load("Pictures/GB_sweep1.png")
    bbsweep2 = pygame.image.load("Pictures/GB_sweep2.png")
    house = pygame.image.load("Pictures/House.png")
    rect = bear.get_rect()
    pygame.display.set_caption("First Game")
    clock = pygame.time.Clock()
    x = win.get_width() / 2 + stonepost.radius
    y = win.get_height() - stonepost.radius * 2
    width = 40
    height = 60
    vel = 5
    run = True
    set = 0;
    fps = 30;
    initdelay = 30
    swap = 1;
    bob = False;
    currteam = True;
    if team == 2:
        currteam = False
    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)
    distance = 0;
    speedcap = 100
    arrayred = [];  # Grizzly
    arrayblue = [];  # Polar
    gocount = 0;

    while run:
        # pygame.time.delay(
        #    20)  # This will delay the game the given amount of milliseconds. In our casee 0.1 seconds will be the delay
        if (iteration == 16):
            run = False;
            swap = -2000
        for event in pygame.event.get():  # This will loop through a list of any keyboard or mouse events.
            if event.type == pygame.QUIT:  # Checks if the red button in the corner of the window is clicked
                run = False  # Ends the game loop
        red = 10000000000;
        blue = 1000000000;
        for i in arrayblue:
            if (i < blue):
                blue = i;

        for i in arrayred:
            if (i < red):
                red = i;

        if (red < blue):
            font = pygame.font.Font('freesansbold.ttf', 32)
            house = pygame.transform.scale(house, (win.get_width(), win.get_height()))

            # create a text suface object,
            # on which text is drawn on it.
            text = font.render(("Blue Wins"), True, green, (255, 255, 255))

            # create a rectangular object for the
            # text surface object
            textRect = text.get_rect()

            # set the center of the rectangular object.
            textRect.center = (x // 2, y // 2)
            win.fill((255, 255, 255))
            win.blit(text, textRect)
        if (red == blue):
            font = pygame.font.Font('freesansbold.ttf', 32)
            house = pygame.transform.scale(house, (win.get_width(), win.get_height()))

            # create a text suface object,
            # on which text is drawn on it.
            text = font.render(("Tie game"), True, green, (255, 255, 255))

            # create a rectangular object for the
            # text surface object
            textRect = text.get_rect()

            # set the center of the rectangular object.
            textRect.center = (x // 2, y // 2)
            win.fill((255, 255, 255))
            win.blit(text, textRect)
        else:
            font = pygame.font.Font('freesansbold.ttf', 32)
            house = pygame.transform.scale(house, (win.get_width(), win.get_height()))

            # create a text suface object,
            # on which text is drawn on it.
            text = font.render(("Red Wins"), True, green, (255, 255, 255))

            # create a rectangular object for the
            # text surface object
            textRect = text.get_rect()

            # set the center of the rectangular object.
            textRect.center = (x // 2, y // 2)
            win.fill((255, 255, 255))
            win.blit(text, textRect)

        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()
        if (currteam):
            bear = pygame.image.load("Pictures/Mock1.png")
            bbear = pygame.image.load("Pictures/GB_back.png")
            bbthrow1 = pygame.image.load("Pictures/GB_throw1.png")
            bbthrow2 = pygame.image.load("Pictures/GB_throw2.png")
            bbthrow3 = pygame.image.load("Pictures/GB_throw3.png")
            bbsweep1 = pygame.image.load("Pictures/GB_sweep1.png")
            bbsweep2 = pygame.image.load("Pictures/GB_sweep2.png")
        else:
            bear = pygame.image.load("Pictures/Mock1.png")
            bbear = pygame.image.load("Pictures/PB_back.png")
            bbthrow1 = pygame.image.load("Pictures/PB_throw1.png")
            bbthrow2 = pygame.image.load("Pictures/PB_throw2.png")
            bbthrow3 = pygame.image.load("Pictures/PB_throw3.png")
            bbsweep1 = pygame.image.load("Pictures/PB_sweep1.png")
            bbsweep2 = pygame.image.load("Pictures/PB_sweep2.png")

        while (swap == 2):
            for event in pygame.event.get():  # This will loop through a list of any keyboard or mouse events.
                if event.type == pygame.QUIT:  # Checks if the red button in the corner of the window is clicked
                    pygame.quit()

            font = pygame.font.Font('freesansbold.ttf', 32)
            house = pygame.transform.scale(house, (win.get_width(), win.get_height()))

            # create a text suface object,
            # on which text is drawn on it.
            text = font.render("Distance: " + str(distance), True, green, (255, 255, 255))

            # create a rectangular object for the
            # text surface object
            textRect = text.get_rect()

            # set the center of the rectangular object.
            textRect.center = (x // 2, y // 2)
            win.fill((255, 255, 255))
            win.blit(text, textRect)

            distance += stonepost.speed;

            if (distance <= 6000 and distance >= 4000 and stonepost.speed <= 0):
                xcache = x + random.randint(-400, 40)
                ycache = y + random.randint(-400, 40)
                win.fill((255, 255, 255))
                win.blit(house, (xcache, ycache))
                pygame.draw.circle(win, (0, 0, 0),
                                   (x, y),
                                   stonepost.radius)
                pygame.display.update()

                font = pygame.font.Font('freesansbold.ttf', 32)
                house = pygame.transform.scale(house, (win.get_width(), win.get_height()))

                # create a text suface object,
                # on which text is drawn on it.
                text = font.render(
                    "Closeness:" + str(((xcache - x) * (xcache - x) + (ycache - y) * (ycache - y)) // 1000), True,
                    green, (255, 255, 255))

                # create a rectangular object for the
                # text surface object
                textRect = text.get_rect()

                # set the center of the rectangular object.
                textRect.center = (x // 2, y // 2)
               # win.fill((255, 255, 255))
                win.blit(text, textRect)

                swap = 1
                distance = 0;
                y += 3 * (win.get_width() / 6)
                stonepost.speed = random.randint(80, 120)
                if (currteam):
                    arrayred.append((xcache - x) * (xcache - x) + (ycache - y) * (ycache - y))
                else:
                    arrayblue.append((xcache - x) * (xcache - x) + (ycache - y) * (ycache - y))
                if (gocount):
                    gocount = 0;
                    currteam = not currteam
                else:
                    gocount += 1;
                pygame.display.update()
                pygame.time.delay(5000)
                break;

            if (distance < 4000 and stonepost.speed <= 0):
                xcache = x + random.randint(-400, 40)
                ycache = y + random.randint(-400, 40)
                win.fill((255, 255, 255))
                win.blit(house, (xcache, ycache))
                pygame.draw.circle(win, (0, 0, 0),
                                   (x, y),
                                   stonepost.radius)
                pygame.display.update()

                font = pygame.font.Font('freesansbold.ttf', 32)
                house = pygame.transform.scale(house, (win.get_width(), win.get_height()))

                # create a text suface object,
                # on which text is drawn on it.
                text = font.render("Too short", True, green, (255, 255, 255))

                # create a rectangular object for the
                # text surface object
                textRect = text.get_rect()

                # set the center of the rectangular object.
                textRect.center = (x // 2, y // 2)
                #win.fill((255, 255, 255))
                win.blit(text, textRect)

                swap = 1
                distance = 0;
                y += 3 * (win.get_width() / 6)
                stonepost.speed = random.randint(80, 120)
                if (currteam):
                    arrayred.append((xcache - x) * (xcache - x) + (ycache - y) * (ycache - y))
                else:
                    arrayblue.append((xcache - x) * (xcache - x) + (ycache - y) * (ycache - y))
                if (gocount):
                    gocount = 0;
                    currteam = not currteam
                else:
                    gocount += 1;
                pygame.display.update()
                pygame.time.delay(5000)
                break;
            if (distance > 6000 and stonepost.speed <= 0):
                xcache = x + random.randint(-400, 40)
                ycache = y + random.randint(-400, 40)
                win.fill((255, 255, 255))
                win.blit(house, (xcache, ycache))
                pygame.draw.circle(win, (0, 0, 0),
                                   (x, y),
                                   stonepost.radius)
                pygame.display.update()

                font = pygame.font.Font('freesansbold.ttf', 32)
                house = pygame.transform.scale(house, (win.get_width(), win.get_height()))

                # create a text suface object,
                # on which text is drawn on it.
                text = font.render("Too far", True, green, (255, 255, 255))

                # create a rectangular object for the
                # text surface object
                textRect = text.get_rect()

                # set the center of the rectangular object.
                textRect.center = (x // 2, y // 2)
                #win.fill((255, 255, 255))
                win.blit(text, textRect)

                swap = 1
                distance = 0;
                stonepost.speed = random.randint(80, 120)
                y += 3 * (win.get_width() / 6)
                if (currteam):
                    arrayred.append((xcache - x) * (xcache - x) + (ycache - y) * (ycache - y))
                else:
                    arrayblue.append((xcache - x) * (xcache - x) + (ycache - y) * (ycache - y))
                if (gocount):
                    gocount = 0;
                    currteam = not currteam
                else:
                    gocount += 1;
                pygame.display.update()
                pygame.time.delay(5000)
                break;

            if (stonepost.speed > 0):
                stonepost.speed -= stonepost.acc;
            else:
                stonepost.speed = 0;
            pygame.draw.circle(win, (0, 0, 0),
                               (x, y),
                               stonepost.radius)
            pygame.time.delay(20)
            if pygame.mouse.get_pressed()[0]:
                for event in pygame.event.get():  # This will loop through a list of any keyboard or mouse events.
                    if event.type == pygame.QUIT:  # Checks if the red button in the corner of the window is clicked
                        pygame.quit()
                bbsweep1 = pygame.transform.scale(bbsweep1, (win.get_width() // 4, win.get_height() // 4))
                bbsweep2 = pygame.transform.scale(bbsweep2, (win.get_width() // 4, win.get_height() // 4))
                win.fill((255, 255, 255))
                win.blit(bbsweep1, pygame.mouse.get_pos())
                pygame.draw.circle(win, (0, 0, 0),
                                   (x, y),
                                   stonepost.radius)
                pygame.display.update()
                pygame.time.delay(10);
                win.fill((255, 255, 255))
                win.blit(bbsweep2, pygame.mouse.get_pos())
                pygame.draw.circle(win, (0, 0, 0),
                                   (x, y),
                                   stonepost.radius)
                pygame.display.update()
                pygame.time.delay(10);
            pygame.display.update()

        bear = pygame.transform.scale(bear, (win.get_width() // 4, win.get_height() // 4))
        bbear = pygame.transform.scale(bbear, (win.get_width() // 4, win.get_height() // 4))

        if keys[pygame.K_UP] and swap == 1:
            swap = 0;

        while (swap == 0):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            win.fill((255, 255, 255))
            bbthrow1 = pygame.transform.scale(bbthrow1, (win.get_width() // 4, win.get_height() // 4))
            bbthrow2 = pygame.transform.scale(bbthrow2, (win.get_width() // 4, win.get_height() // 4))
            bbthrow3 = pygame.transform.scale(bbthrow3, (win.get_width() // 4, win.get_height() // 4))
            win.blit(bbthrow1, (win.get_width() / 2 - bear.get_width() / 2 - 20,
                                win.get_height() - bear.get_height()))
            pygame.draw.circle(win, (0, 0, 0),
                               (x, y),
                               stonepost.radius)
            y -= win.get_width() / 6
            pygame.display.update()
            pygame.time.delay(50)
            win.fill((255, 255, 255))
            win.blit(bbthrow2, (win.get_width() / 2 - bear.get_width() / 2 - 20,
                                win.get_height() - bear.get_height()))
            pygame.draw.circle(win, (0, 0, 0),
                               (x, y),
                               stonepost.radius)
            y -= win.get_width() / 6
            pygame.display.update()
            pygame.time.delay(50)
            win.fill((255, 255, 255))
            win.blit(bbthrow3, (win.get_width() / 2 - bear.get_width() / 2 - 20,
                                win.get_height() - bear.get_height()))
            pygame.draw.circle(win, (0, 0, 0),
                               (x, y),
                               stonepost.radius)
            y -= win.get_width() / 6
            pygame.time.delay(50)
            pygame.display.update()
            swap = 2

        if (swap == 1):
            win.fill((255, 255, 255))
            win.blit(bbear, (win.get_width() / 2 - bear.get_width() / 2 - 20,
                             win.get_height() - bear.get_height()))
            pygame.draw.circle(win, (255, 0, 0),
                               (win.get_width() / 2 + stonepost.radius, win.get_height() - stonepost.radius * 2),
                               stonepost.radius)

            pygame.display.update();

        clock.tick(120)

pygame.quit()  # If we exit the loop this will execute and close our game
