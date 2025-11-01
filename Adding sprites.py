import pygame, sys
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
player = pygame.Rect(100, 100, 60, 60)
enemy = pygame.Rect(400, 300, 60, 60)
speed = 5
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT: pygame.quit(); sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: player.x -= speed
    if keys[pygame.K_RIGHT]: player.x += speed
    if keys[pygame.K_UP]: player.y -= speed
    if keys[pygame.K_DOWN]: player.y += speed
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 255), player)
    pygame.draw.rect(screen, (255, 0, 0), enemy)
    pygame.display.flip()
    clock.tick(60)