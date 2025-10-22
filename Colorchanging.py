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
        pressed=pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:x-=3
        if pressed[pygame.K_RIGHT]:x+=3
        if pressed[pygame.K_UP]:y-=3
        if pressed[pygame.K_DOWN]:y+=3
        x=min(max(0,x),width-sprite_width)
        y=min(max(0,y),height-sprite_height)
        if x==0:
            currentcolour=colours['blue']
        elif x==width-sprite_width:
            currentcolour=colours['yellow']
        elif y==0:
            currentcolour=colours['red']
        elif y==height-sprite_height:
            currentcolour=colours['green']
        else:
            currentcolour=colours['white']
        screen.fill((0,0,0,0))
        pygame.draw.rect(screen,currentcolour,(x,y,sprite_width,sprite_height))
        pygame.display.flip()
        clock.tick(90)
    pygame.quit()
if __name__=="__main__":
    main()

        
            
        
                
    