#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
basic geometry showed with pygame
"""

import pygame

background = (0,0,0)
(wid, hei) = (640,480)
screen = pygame.display.set_mode((wid, hei))
clock = pygame.time.Clock()
loop = True
pygame.display.set_caption('basic geometry')
screen.fill(background)

def draw_point(x,y):
    screen.set_at((x, y), (255, 255, 255))

def draw_line(x1,y1,x2,y2):
    pygame.draw.line(screen, (255, 255, 255), (x1,y1), (x2, y2))

while loop:

    draw_point(100,200)
    draw_point(540,200)
    draw_line(320,300,320,400)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        elif event.type == pygame.KEYDOWN:
            loop = False 
    pygame.display.flip()
    clock.tick(250)
pygame.quit()
