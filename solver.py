import pygame as pg
from settings import *
import link

pg.init()

class Solver():
    def __init__(self, screen, objects, links):
        self.screen = screen
        self.objects = objects
        self.links = links
        self.gravity = pg.Vector2(0.0, 1000.0)

    def update(self, dt):
        self.subseps = 8
        self.sub_dt = dt / self.subseps
        for i in range(self.subseps):
            self.apply_gravity()
            self.apply_constraint()
            self.apply_collisions()
            self.update_positions(self.sub_dt)

    def update_positions(self, dt):
        for obj in self.objects:
            obj.update_position(dt)

    def apply_gravity(self):
        for obj in self.objects:
            obj.accelerate(self.gravity)

    def apply_constraint(self):
        #apply link constraints
        for link in self.links:
            link.apply()


        #apply other constraint

        position = pg.Vector2(WIDTH/2, HEIGHT/2)
        radius = WIDTH/2


        for obj in self.objects:
            #if the object is outside the constraint
            if (obj.pos - position).length() > radius - obj.radius:
                n = (obj.pos - position).normalize()
                obj.pos = position + n * (radius - obj.radius)


    def apply_collisions(self):
        for obj in self.objects:
            for obj2 in self.objects:
                if obj != obj2:
                    if (obj.pos - obj2.pos).length() < obj.radius + obj2.radius:
                        #resolve collision
                        n = (obj.pos - obj2.pos).normalize()
                        delta = (obj.radius + obj2.radius) - (obj.pos - obj2.pos).length()
                        #move along the collision axis until they are no longer colliding
                        if not obj.is_fixed:
                            obj.pos += 0.5 * delta * n
                        if not obj2.is_fixed:
                            obj2.pos -= 0.5 * delta * n

