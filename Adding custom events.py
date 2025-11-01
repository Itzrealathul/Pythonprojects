import pygame
import random
pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Add Custom Event")
sprite1 = pygame.Rect(150, 150, 100, 100)
sprite2 = pygame.Rect(350, 150, 100, 100)
color1 = (255, 0, 0)
color2 = (0, 0, 255)
CHANGE_COLOR = pygame.USEREVENT + 1
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if sprite1.collidepoint(event.pos):
                pygame.event.post(pygame.event.Event(CHANGE_COLOR))
        if event.type == CHANGE_COLOR:
            color2 = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, color1, sprite1)
    pygame.draw.rect(screen, color2, sprite2)
    pygame.display.flip()
pygame.quit()
