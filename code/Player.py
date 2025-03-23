import pygame.key

from code.Entity import Entity
from code.const import Entity_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, \
    PLAYER_KEY_RIGHT


class Player(Entity):
    def __int__(self, name: str, position: tuple):
        super(). __init__(name, position)

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= Entity_SPEED[self.name]
        if pressed_key[PLAYER_KEY_DOWN [self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += Entity_SPEED[self.name]
        if pressed_key[PLAYER_KEY_LEFT [self.name]] and self.rect.left > 0:
            self.rect.centerx -= Entity_SPEED[self.name]
        if pressed_key[PLAYER_KEY_RIGHT [self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += Entity_SPEED[self.name]

        pass
