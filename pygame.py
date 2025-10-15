import pygame
pygame.init()
screen=pygame.display.set_mode((400,500))
done=False
while not done:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
    pygame.display.flip()
