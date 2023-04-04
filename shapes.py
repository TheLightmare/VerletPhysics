import pygame as pg
from settings import *
import sprites
import link

pg.init()

def create_bag(object_group, link_group, mouse_pos):
    objects = []
    for i in range(10):
        obj = sprites.VerletObject(object_group, (mouse_pos[0] + i*49, mouse_pos[1]), WHITE)
        objects.append(obj)
    objects[0].is_fixed = True
    objects[-1].is_fixed = True

    for i in range(len(objects) - 1):
        link.Link(link_group, objects[i], objects[i+1], 50)

def create_cloth(object_group, link_group, mouse_pos):
    objects = []
    for i in range(10):
        objects.append([])
        for j in range(10):
            obj = sprites.VerletObject(object_group, (mouse_pos[0] + i*50, mouse_pos[1] + j*50), WHITE)
            objects[i].append(obj)
    objects[0][0].is_fixed = True
    objects[-1][0].is_fixed = True

    for i in range(len(objects)):
        for j in range(len(objects[i]) - 1):
            link.Link(link_group, objects[i][j], objects[i][j+1], 50)
    for i in range(len(objects) - 1):
        for j in range(len(objects[i])):
            link.Link(link_group, objects[i][j], objects[i+1][j], 50)

