import pygame
pygame.init()
screen=pygame.diaplay.set_mode((400,400))
screen.fill((255,255))
green=(0,255,0)
pygame.draw.circle(screen,green,(300,300),50)
pygame.draw.circle(screen,green,(100,100),50,3)
pygame.display.update()
running=True
while running:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            running=False
pygame.quit()
           
    