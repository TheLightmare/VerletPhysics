import pygame as pg

from settings import *
import sprites

pg.init()

class Link(pg.sprite.Sprite):
    def __init__(self, group, obj1, obj2, length):
        pg.sprite.Sprite.__init__(self, group)
        self.obj1 = obj1
        self.obj2 = obj2
        self.length = length

        # Graphics
        self.image = pg.Surface((self.length, 1))
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()

    def apply(self):
        axis = self.obj1.pos - self.obj2.pos
        dist = axis.length()
        n = axis / dist
        delta = self.length - dist
        if not self.obj1.is_fixed:
            self.obj1.pos += 0.5 * delta * n
        if not self.obj2.is_fixed:
            self.obj2.pos -= 0.5 * delta * n


    def draw(self, screen):
        pg.draw.line(screen, WHITE, self.obj1.pos, self.obj2.pos, 1)