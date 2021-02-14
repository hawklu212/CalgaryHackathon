import os
import main
import pregame
import pygame
import random
from Models.Player import Stone

currTeam = True

# Game Initialization
pygame.init()

# Center the Game Application
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Game Resolution
screen_width = 900
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))

# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont = pygame.font.Font(textFont, textSize)
    newText = newFont.render(message, 0, textColor)

    return newText

white = pygame.image.load("Pictures/white1.png")
brown = pygame.image.load("Pictures/brown1.png")
white = pygame.transform.scale(white, (350, 350))
brown = pygame.transform.scale(brown, (350, 350))

# Colors
whiteC = (255, 255, 255)
black = (0, 0, 0)
gray = (50, 50, 50)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# Game Fonts
font = "NOTMK___.ttf"

# Game Framerate
clock = pygame.time.Clock()
FPS = 10
bg1 = pygame.image.load("Pictures/Mock_Sweeper_1.png")
bg2 = pygame.image.load("Pictures/Mock_Sweeper_2.png")
white1 = pygame.image.load("Pictures/white1.png")
white1 = pygame.transform.scale(white1, (300, 300))
white2 = pygame.image.load("Pictures/white2.png")
white2 = pygame.transform.scale(white2, (300, 300))

def button(text, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))

    smallText = pygame.font.SysFont("NOTMK___.ttf",30)
    textSurf, textRect = text_objects(text, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

# Main Menu
def main_menu():
    mouse = pygame.mouse.get_pos()
    menu = True
    image = 1
    while menu:
        image *= -1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Main Menu UI
        screen.fill(gray)

        title = text_format("BCS Cats Curling", font, 90, yellow)
        title_rect = title.get_rect()

        # Main Menu Text
        if image == 1:
            screen.blit(bg1, (0, -25))
            screen.blit(white1, (600, 300))
        else:
            screen.blit(bg2, (0, -25))
            screen.blit(white2, (600, 300))

        screen.blit(title, (screen_width / 2 - (title_rect[2] / 2), 80))
        button("Start", (screen_width / 2), 300, 100, 50, green, green, pregame)
        button("How to Play", (screen_width / 2) - 8, 400, 120, 50, yellow, yellow, howtoplay)
        button("Quit", (screen_width / 2), 500, 100, 50, red, red, pygame.quit)

        pygame.display.update()
        clock.tick(FPS)

#How to Play screen
def howtoplay():
    howto = True
    font = pygame.font.Font("NOTMK___.ttf", 30)
    text = font.render("Click to scrub, press up to chuck and enjoy the show", True, black, whiteC)
    textRect = text.get_rect()
    textRect.center = (screen_width // 2, screen_height // 2)
    screen.fill(gray)
    screen.blit(text, textRect)

    button("Back", 50, 50, 100, 50, whiteC, whiteC, main_menu)

    while howto:
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                pygame.quit()
                quit()

            button("Back", 50, 50, 100, 50, whiteC, whiteC, main_menu)
            pygame.display.update()
            clock.tick(FPS)

def draw_rect_black(x, y):
    rect_upper = pygame.Rect(x-10, y-10, 370, 10)
    rect_left = pygame.Rect(x-10, y, 10, 360)
    rect_lower = pygame.Rect(x, y+350, 360, 10)
    rect_right = pygame.Rect(x+350, y, 10, 350)
    pygame.draw.rect(screen, black, rect_upper)
    pygame.draw.rect(screen, black, rect_left)
    pygame.draw.rect(screen, black, rect_lower)
    pygame.draw.rect(screen, black, rect_right)

def draw_rect_white(x, y):
    rect_upper = pygame.Rect(x-10, y-10, 370, 10)
    rect_left = pygame.Rect(x-10, y, 10, 360)
    rect_lower = pygame.Rect(x, y+350, 360, 10)
    rect_right = pygame.Rect(x+350, y, 10, 350)
    pygame.draw.rect(screen, whiteC, rect_upper)
    pygame.draw.rect(screen, whiteC, rect_left)
    pygame.draw.rect(screen, whiteC, rect_lower)
    pygame.draw.rect(screen, whiteC, rect_right)

def pregame():
    global currTeam
    run = True
    team = 0
    xb = 30
    xw = 510
    y = 150

    while run:

        screen.fill(gray)
        title = text_format("Choose Your Team", font, 80, yellow)
        title_rect = title.get_rect()

        screen.blit(title, (screen_width / 2 - (title_rect[2] / 2), 30))

        screen.blit(brown, (30, 150))
        screen.blit(white, (510, 150))

        pointer = pygame.mouse.get_pos()
        brownpointer = brown.get_rect(x = 30, y=150)
        whitepointer = white.get_rect(x=510, y=150)

        if brownpointer.collidepoint(pointer):
            draw_rect_white(30, 150)
            pygame.display.update()
        elif whitepointer.collidepoint(pointer):
            draw_rect_black(510, 150)
            pygame.display.update()

        if team == 1:
            button("Grizzlies Start", (screen_width / 2 - 100), 600, 200, 50, whiteC, whiteC, main)
        if team == 2:
            currTeam = False
            button("Polars Start", (screen_width / 2 - 100), 600, 200, 50, whiteC, whiteC, main)

        for event in pygame.event.get():
            button("Back", 50, 550, 100, 50, whiteC, whiteC, main_menu)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if brownpointer.collidepoint(pos):
                    team = 1
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if whitepointer.collidepoint(pos):
                    team = 2

        pygame.display.update()
        clock.tick(FPS)

def main():
    global currTeam
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
    pygame.display.set_caption("Bear Curling Game")
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
        if (currTeam == True):
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
                win.fill((255, 255, 255))
                win.blit(house, (xcache, ycache))
                pygame.draw.circle(win, (0, 0, 0),
                                   (x, y),
                                   stonepost.radius)
                win.blit(text, textRect)

                swap = 1
                distance = 0;
                if iteration >= 16:
                    swap = -9000
                    run = False
                    break;

                y += 3 * (win.get_width() / 6)
                stonepost.speed = random.randint(80, 120)
                if (currTeam):
                    arrayred.append((xcache - x) * (xcache - x) + (ycache - y) * (ycache - y))
                else:
                    arrayblue.append((xcache - x) * (xcache - x) + (ycache - y) * (ycache - y))
                if (gocount):
                    gocount = 0;
                    currTeam = not currTeam
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
                win.fill((255, 255, 255))
                win.blit(text, textRect)

                swap = 1
                distance = 0;
                y += 3 * (win.get_width() / 6)
                if iteration >= 16:
                    swap = -9000
                    run = False
                    break;
                stonepost.speed = random.randint(80, 120)
                if (currTeam):
                    arrayred.append((xcache - x) * (xcache - x) + (ycache - y) * (ycache - y))
                else:
                    arrayblue.append((xcache - x) * (xcache - x) + (ycache - y) * (ycache - y))
                if (gocount):
                    gocount = 0;
                    currTeam = not currTeam
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
                win.fill((255, 255, 255))
                win.blit(text, textRect)

                swap = 1
                distance = 0;
                if iteration >= 4:
                    swap = -9000
                    run = False
                    break;
                stonepost.speed = random.randint(80, 120)
                y += 3 * (win.get_width() / 6)
                if (currTeam):
                    arrayred.append((xcache - x) * (xcache - x) + (ycache - y) * (ycache - y))
                else:
                    arrayblue.append((xcache - x) * (xcache - x) + (ycache - y) * (ycache - y))
                if (gocount):
                    gocount = 0;
                    currTeam = not currTeam
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

#Initialize the Game
main_menu()
pygame.quit()
quit()