import pygame as pg

class StaticLine(pg.sprite.Sprite):
    def __init__(self, group, start : pg.Vector2, end : pg.Vector2, color):
        pg.sprite.Sprite.__init__(self, group)
        self.start = start
        self.end = end
        self.color = color

    def normal(self):
        (d_x, d_y) = (self.end[0] - self.start[0], self.end[1] - self.start[1])
        return pg.Vector2(d_y, -d_x).normalize()

    def dist_from(self, obj):
        return abs((obj.pos - self.start).dot(self.normal()))

    def circle_collision(self, obj):
        # get the normal of the line
        n = self.normal()

        # get the distance from the line
        dist = self.dist_from(obj)
        # if the object is inside the line
        if dist < obj.radius:
            # if the object is between the start and end points
            if (obj.pos - self.start).dot(self.end - self.start) > 0 and (obj.pos - self.end).dot(self.start - self.end) > 0:
                # resolve collision
                # if object same side as normal
                if (obj.pos - self.start).dot(n) > 0:
                    obj.pos += (obj.radius - dist) * n
                else:
                    obj.pos -= (obj.radius - dist) * n



    def draw(self, screen):
        pg.draw.line(screen, self.color, self.start, self.end, 3)