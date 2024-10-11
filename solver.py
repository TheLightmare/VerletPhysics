import pygame as pg

from objects import static_objects, special_objects
from settings import *

pg.init()

class Solver():
    def __init__(self, screen, objects, statics, specials, links):
        self.screen = screen
        self.objects = objects
        self.specials = specials
        self.links = links
        self.statics = statics
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



    def apply_collisions(self):
        for obj in self.objects:
            # collisions with special objects
            for special_obj in self.specials:
                if type(special_obj) == special_objects.SinkObject:
                    if (obj.pos - special_obj.pos).length() < special_obj.radius + obj.radius:
                        obj.kill()

            # collisions with static objects
            for static_obj in self.statics:
                # if the static object is a StaticLine
                if type(static_obj) == static_objects.StaticLine:
                    static_obj.circle_collision(obj)

            # collisions with VerletObjects
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

