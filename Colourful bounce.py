import pygame
import random
pygame.init()
sprite_colour_change_event=pygame.USEREVENT+1
background_colour_change_event=pygame.USEREVENT+2
BLUE=pygame.Color('blue')
LIGHTBLUE=pygame.Color('light blue')
DARKBLUE=pygame.Color('darkblue')
YELLOW=pygame.Color('yellow')
MAGENTA=pygame.Color('magenta')
ORANGE=pygame.Color('orange')
WHITE=pygame.Color('white')
class Sprite(pygame.sprite.Sprite):
    def __init__(self,colour,height,width):
        super().__init__()
        self.image=pygame.Surface([width,height])
        self.image.fill(colour)
        self.rect=self.image.get__rect()
        self.velocity=[random.choice[(-1,1)],random.choice([-1,1])]
    def update(self):
        self.rect.move_ip(self.velocity)
 
        
    
    
    
    
    
