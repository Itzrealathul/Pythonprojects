import pygame
pygame.init()
width,height=(500,500)
surface=pygame.display.setmode((width,height))
pygame.display.set_caption("Adding image and background image")
background_image=pygame.transform.scale(pygame.image.load("Py background.jpg").convert(),(width,height))
penguin_image=pygame.transform.scale(pygame.image.load().convert_alpha,(200,200))
penguin_rect=penguin_image.get_rect(center=(width//2,height//2-30))
