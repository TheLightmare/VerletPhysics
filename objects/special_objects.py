import pygame as pg
from objects.physics_objects import VerletObject


class SinkObject(pg.sprite.Sprite):
    '''
    Destroys VerletObjects that collide with it.
    '''
    def __init__(self, group, pos : pg.Vector2, color, radius=10):
        pg.sprite.Sprite.__init__(self, group)

        self.group = group
        self.pos = pos
        self.color = color
        self.radius = radius
        self.image = pg.Surface((self.radius, self.radius))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update(self):
        pass

    def draw(self, screen):
        pg.draw.circle(screen, self.color, self.pos, self.radius)


class SpawnerObject(pg.sprite.Sprite):
    '''
    Spawns VerletObjects when timer reaches 0.
    '''
    def __init__(self, game, group, pos, active_color, inactive_color, radius=10, spawn_rate=1):
        pg.sprite.Sprite.__init__(self, group)
        self.game = game
        self.pos = pg.Vector2(pos)
        self.activecolor = active_color
        self.inactivecolor = inactive_color
        self.color = self.activecolor
        self.radius = radius
        self.spawn_rate = spawn_rate
        self.timer = 0
        self.image = pg.Surface((self.radius, self.radius))
        self.image.fill(self.color)
        self.image.set_colorkey(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

        self.active = True

    def toggle(self):
        self.active = not self.active
        self.color = self.activecolor if self.active else self.inactivecolor

    def update(self):
        if not self.active:
            return
        self.timer += self.game.clock.get_time() / 1000.0
        if self.timer > 1 / self.spawn_rate:
            self.timer = 0
            VerletObject(self.game.objects, self.pos, self.game.ball_color, self.radius)

    def draw(self, screen):
        pg.draw.circle(screen, self.color, self.pos, self.radius)