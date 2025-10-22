import pygame
import sys
pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("My Game Screen")
WHITE = (255, 255, 255)
BLUE = (0, 128, 255)
RED = (255, 0, 0)
font = pygame.font.SysFont(None, 48)
text = font.render("Hello, Pygame!", True, RED)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (200, 150, 200, 100))
    screen.blit(text, (180, 50))
    pygame.display.flip()
pygame.quit()
sys.exit()