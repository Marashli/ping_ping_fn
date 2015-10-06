# -*- coding: utf-8 -*-
import pygame
import random

window = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Hello, pygame!')
screen = pygame.Surface((400, 400))


class Sprite:
    def __init__(self, xpos, ypos, filename):
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load(filename)
        self.bitmap.set_colorkey((255, 255, 255))

    def render(self):
        screen.blit(self.bitmap, (self.x, self.y))

player_1 = Sprite(0, 0, 'player.png')
player_2 = Sprite(0, 392, 'player.png')


ball = Sprite(300, 200, 'ball.png')
reverse_x = 1
reverse_y = 1

done = True
while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False

    screen.fill((50, 50, 50))

    # вот эти параметры нужно изменять

    player_1.x = 70
    player_2.x = 290

    ball.x += reverse_x
    ball.y += reverse_y

    if player_1.x < 0:
        player_1.x = 0

    elif player_1.x > 360:
        player_1.x = 360

    if player_2.x < 0:
        player_2.x = 0

    elif player_2.x > 360:
        player_2.x = 360

    if ball.x < 0:
        reverse_x = 1
    elif ball.x > 389:
        reverse_x = -1

    if ball.y < 0:
        # reverse_y = 1
        ball.x = 300
        ball.y = 200
        reverse_x = 1
        reverse_y = 1

    elif ball.y > 389:
        # reverse_y = -1
        ball.x = 300
        ball.y = 200
        reverse_x = 1
        reverse_y = 1

    if player_1.x < ball.x < player_1.x + 20 and ball.y <= 8:
        reverse_y = 1

    if player_2.x < ball.x < player_2.x + 20 and ball.y >= 382:
        reverse_y = -1

    player_1.render()
    player_2.render()
    ball.render()

    window.blit(screen, (0, 0))
    pygame.display.flip()
    pygame.time.delay(5)
