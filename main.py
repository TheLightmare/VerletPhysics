import pygame as pg

from settings import *
import solver
import sprites
import custom_group
import link
import shapes

pg.init()

class Game():
    def __init__(self):
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

        self.objects = custom_group.VerletGroup()
        self.links = custom_group.LinkGroup()
        self.solver = solver.Solver(self.screen, self.objects, self.links)


    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        dt = self.clock.get_time() / 1000.0
        self.solver.update(dt)

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.running = False
                if event.key == pg.K_r:
                    self.objects.empty()
                    self.links.empty()
                if event.key == pg.K_b:
                    shapes.create_cloth(self.objects, self.links, pg.mouse.get_pos())
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    sprites.VerletObject(self.objects, event.pos, RED)
                if event.button == 3:
                    for obj in self.solver.objects:
                        if (obj.pos - pg.Vector2(event.pos)).length() < obj.radius:
                            obj.is_fixed = not obj.is_fixed

    def draw(self):
        self.screen.fill(BLACK)
        self.objects.draw(self.screen)
        self.links.draw(self.screen)

        position = pg.Vector2(WIDTH / 2, HEIGHT / 2)
        radius = WIDTH / 2
        pg.draw.circle(self.screen, RED, position, radius, 2)

        pg.display.flip()

g = Game()
g.run()