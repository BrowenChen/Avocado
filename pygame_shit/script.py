#!/usr/bin/python
import sys
import pygame
from pygame.locals import *

def draw(content):
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 707
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Cheatify!')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    # Display some text
    texts = []
    font = pygame.font.SysFont('helvetica', 12)
    for string in content:
        print(font.size(string))
        texts.append(font.render(string, 1, (10, 10, 10)))

    counter = 0

    for text in texts:
        textpos = text.get_rect()
        textpos.centerx = background.get_rect().centerx
        textpos.centery = counter + 20
        counter += 20;
        background.blit(text, textpos)

    # Blit everything to the screen
    screen.blit(background, (0, 0))

    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

            screen.blit(background, (0, 0))
            pygame.display.flip()

def parse_input(filename):
    f = open(filename, 'r')
    strings = []
    for line in f.readlines():
        if line != '\n':
            for message in line.split('\n'):
                if message != '':
                    strings.append(message)
    return strings

def main():
    if len(sys.argv) < 2:
        print("Please specify text file name")
        exit()
    input_file = sys.argv[1]
    cheatsheet_content = parse_input(input_file)
    print(str(cheatsheet_content))
    draw(cheatsheet_content)

if __name__ == '__main__': main()

