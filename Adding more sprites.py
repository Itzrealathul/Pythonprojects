import pygame
import random
pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Add More Sprites")
player = pygame.Rect(280, 180, 40, 40)
enemies = [pygame.Rect(random.randint(0, 560), random.randint(0, 360), 40, 40) for _ in range(7)]
player_color = (0, 255, 0)
enemy_color = (255, 0, 0)
score = 0
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5
    if keys[pygame.K_UP]:
        player.y -= 5
    if keys[pygame.K_DOWN]:
        player.y += 5
    for enemy in enemies:
        if player.colliderect(enemy):
            score += 1
            enemy.x = random.randint(0, 560)
            enemy.y = random.randint(0, 360)
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, player_color, player)
    for enemy in enemies:
        pygame.draw.rect(screen, enemy_color, enemy)
    text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(text, (10, 10))
    pygame.display.flip()
    clock.tick(30)
pygame.quit()