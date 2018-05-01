#! /usr/bin/env python
import pygame
width=int(input("Input width "))
height=int(input("Input height "))
screen = pygame.display.set_mode((width, height))
running=True
while running:
	event=pygame.event.poll()
	if event.type==pygame.QUIT:
		running=False