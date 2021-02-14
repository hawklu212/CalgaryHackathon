import pygame
from pygame.locals import*
import os
import main

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


# Colors
white = (255, 255, 255)
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
FPS = 5
bg1 = pygame.image.load("Pictures/Mock_Sweeper_1.png")
bg2 = pygame.image.load("Pictures/Mock_Sweeper_2.png")

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
            screen.blit(bg1, (0, 0))
        else:
            screen.blit(bg2, (0, 0))

        screen.blit(title, (screen_width / 2 - (title_rect[2] / 2), 80))
        button("Start", (screen_width / 2), 300, 100, 50, green, green, main.main)
        button("How to Play", (screen_width / 2) - 8, 400, 120, 50, yellow, yellow, howtoplay)
        button("Quit", (screen_width / 2), 500, 100, 50, red, red, pygame.quit)

        pygame.display.update()
        clock.tick(FPS)

#How to Play screen
def howtoplay():
    howto = True
    font = pygame.font.Font("NOTMK___.ttf", 30)
    text = font.render("THIS IS SOME SAMPLE TEXT", True, black, white)
    textRect = text.get_rect()
    textRect.center = (screen_width // 2, screen_height // 2)
    screen.fill(gray)
    screen.blit(text, textRect)

    button("Back", 50, 50, 100, 50, white, white, main_menu)

    while howto:
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                pygame.quit()
                quit()

            button("Back", 50, 50, 100, 50, white, white, main_menu)
            pygame.display.update()
            clock.tick(FPS)

#Initialize the Game
main_menu()
pygame.quit()
quit()