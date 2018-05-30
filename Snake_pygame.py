import pygame

#Constant variables
width=800
height=700
screen=pygame.display.set_mode((width,height))
bgcolor=0,0,0

#Non-constant variables
x_posi=(width/2)
y_posi=(height/2)

while running:
	event=pygame.event.poll()
	if event.type==pygame.QUIT:
		running=0
	
	screen.fill(bgcolor)
