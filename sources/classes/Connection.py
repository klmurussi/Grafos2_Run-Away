import pygame
from tools import Sprites


class Connection(pygame.sprite.Sprite):
    def __init__(self, src, dest):
        super().__init__()
        Sprites.line_list.append((src, dest))