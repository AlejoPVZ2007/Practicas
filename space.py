import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 900, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Game")

clock = pygame.time.Clock()

stars = []

for _ in range(500):
    angle = random.uniform(0, math.pi * 2)
    dist = random.uniform(5, 450)
    speed = random.uniform(2, 6)
    stars.append([angle, dist, speed])

running = True

while running:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 15))

    cx = WIDTH // 2
    cy = HEIGHT // 2

    for s in stars:
        
        angle, dist, speed = s

        dist -= speed

        if dist < 5:
            dist = 450
            angle = random.uniform(0, 2 * math.pi)

        x = cx + math.cos(angle) * dist
        y = cy + math.sin(angle) * dist

        size = max(1, int((450 - dist) / 70))

        color = (
            120 + size * 20,
            100,
            255
        )

        pygame.draw.circle(
            screen,
            color,
            (int(x), int(y)),
            size
        )

        s[0] = angle
        s[1] = dist

    for r in range(35, 0 , -3):
        pygame.draw.circle(
            screen,
            (80, 180, 255),
            (cx, cy),
            r,
            1
        )

    pygame.display.flip()

pygame.quit()