#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pygame
from pygame.locals import *
from subpixel_surface import *
from math import sin, cos


DOTS = 100


def main():

    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    dot = pygame.image.load("./dot.png")
    dot_subpixel = SubPixelSurface(dot, x_level=8)

    t = 0.
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        time_passed = clock.tick()
        t += time_passed / 3000.

        for n in range(DOTS):
            a = float(n)/DOTS * sin((t)*.1234)*100
            x = sin((t+a)*sin(t/4)) * 200.*sin(t/5) + 320
            y = cos(((t*1.234)+a)*sin(t/8)) * 200.*sin(t/4) + 220
            screen.blit(dot_subpixel.at(x, y), (x, y))

        pygame.display.update()


if __name__ == "__main__":
    main()
