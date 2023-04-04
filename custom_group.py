import pygame as pg
from settings import *
import sprites

pg.init()

class VerletGroup(pg.sprite.Group):
    def __init__(self, *sprites):
        pg.sprite.Group.__init__(self, *sprites)

    def draw(self, screen):
        for sprite in self.sprites():
            sprite.draw(screen)

class LinkGroup(pg.sprite.Group):
    def __init__(self, *sprites):
        pg.sprite.Group.__init__(self, *sprites)

    def draw(self, screen):
        for sprite in self.sprites():
            sprite.draw(screen)