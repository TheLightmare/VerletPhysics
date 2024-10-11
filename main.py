import pygame as pg

from settings import *
import solver
from objects import physics_objects, static_objects, special_objects
import custom_group
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
        self.statics = custom_group.StaticGroup()
        self.specials = custom_group.SpecialGroup()
        self.solver = solver.Solver(self.screen, self.objects, self.statics, self.specials, self.links)


        self.ball_color = RED

    def init_scene(self):
        '''
        Initialize the scene (to be replaced with json files ultimately)
        :return:
        '''
        # create a sink object
        special_objects.SinkObject(self.specials, pg.Vector2(WIDTH / 2, HEIGHT), BLUE, 100)
        # create a spawn object
        special_objects.SpawnerObject(self, self.specials, pg.Vector2(30, 10), GREEN, 10, 5)

    def run(self):
        self.init_scene()

        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        dt = self.clock.get_time() / 1000.0
        self.specials.update()
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
                    # lerp between all colors
                    colors = [RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA]
                    self.ball_color = colors[(colors.index(self.ball_color) + 1) % len(colors)]
                    physics_objects.VerletObject(self.objects, event.pos, self.ball_color)
                if event.button == 3:
                    if not hasattr(self, 'static_first_point'):

                        self.static_first_point = pg.Vector2(pg.mouse.get_pos())
                    else:
                        static_objects.StaticLine(self.statics, self.static_first_point, pg.Vector2(pg.mouse.get_pos()), RED)
                        del self.static_first_point

    def draw(self):
        self.screen.fill(BLACK)
        self.objects.draw(self.screen)
        self.links.draw(self.screen)
        self.statics.draw(self.screen)
        self.specials.draw(self.screen)

        if hasattr(self, 'static_first_point'):
            pg.draw.line(self.screen,BLUE, self.static_first_point, pg.mouse.get_pos(), 5)

        pg.display.flip()

g = Game()
g.run()