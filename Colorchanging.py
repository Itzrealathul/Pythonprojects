import pygame
def main():
    pygame.init()
    width,height=500,500
    screen=pygame.display.set_mode((width,height))
    pygame.display.set_caption("Colour changing sprite")
    colours={'red':pygame.Color('red'),'blue':pygame.Color('blue'),'green':pygame.Color('green'),'yellow':pygame.Color('yellow'),'white':pygame.Color('white')}
    currentcolour=colours['white']
    x,y=30,30
    sprite_width,sprite_height=60,60
    clock=pygame.time.Clock()
    running=True
    while running:
        for i in pygame.event.get():
            if i.type==pygame.QUIT:
                running=False
    