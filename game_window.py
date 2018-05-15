#! /usr/bin/env python
import pygame
width=int(input("Input width "))
height=int(input("Input height "))
color=[0,0,0]
time=int(input("What is the time? (Use military time) "))
if time<1200:
	color[2]=(time/10)
if time==1200:
	color[2]=255
if time>1200:
	color[2]=255-(time/10)
screen = pygame.display.set_mode((width, height))
running=True
while running:
	event=pygame.event.poll()
	if event.type==pygame.QUIT:
		running=False
	screen.fill((color))
	pygame.display.flip()
	
