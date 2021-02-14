import pygame
from pygame.locals import*
import os
import main
import MainMenu

# Game Initialization
pygame.init()

# Center the Game Application
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Game Resolution
screen_width = 900
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))

whiteC = (255, 255, 255)
black = (0, 0, 0)
gray = (50, 50, 50)
font = "NOTMK___.ttf"
yellow = (255, 255, 0)
clock = pygame.time.Clock()
FPS = 5

white = pygame.image.load("Pictures/white1.png")
brown = pygame.image.load("Pictures/brown1.png")
white = pygame.transform.scale(white, (350, 350))
brown = pygame.transform.scale(brown, (350, 350))

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

def text_format(message, textFont, textSize, textColor):
    newFont = pygame.font.Font(textFont, textSize)
    newText = newFont.render(message, 0, textColor)

    return newText

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
    run = True
    team = 0
    xb = 30
    xw = 510
    y = 150
    button("Back", 50, 50, 100, 50, white, white, MainMenu.main_menu)
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
            button("Grizzlies Start", (screen_width / 2 - 100), 600, 200, 50, whiteC, whiteC, main.main)
        if team == 2:
            button("Polars Start", (screen_width / 2 - 100), 600, 200, 50, whiteC, whiteC, main.main)

        for event in pygame.event.get():
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