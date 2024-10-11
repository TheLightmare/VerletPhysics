import pygame as pg

from settings import *

pg.init()

class VerletObject(pg.sprite.Sprite):
    def __init__(self, group, pos, color, radius=10, is_fixed=False):
        pg.sprite.Sprite.__init__(self, group)

        self.is_fixed = is_fixed
        self.pos = pg.Vector2(pos)
        self.color = color
        self.old_pos = pos
        self.acc = pg.Vector2(0.0, 0.0)
        self.radius = radius
        # Graphics
        self.image = pg.Surface((self.radius, self.radius))
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()


    def update_position(self, dt):
        if self.is_fixed:
            return

        self.vel = self.pos - self.old_pos
        self.old_pos = self.pos
        self.pos = self.pos + self.vel + self.acc * dt * dt
        self.acc = pg.Vector2(0.0, 0.0)

        self.rect.center = self.pos

    def accelerate(self, acc):
        if self.is_fixed:
            return

        self.acc += acc

    def draw(self, screen):
        pg.draw.circle(screen, self.color, self.pos, self.radius)