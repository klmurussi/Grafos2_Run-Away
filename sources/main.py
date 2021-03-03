from typing import Set
import pygame as pg
import sys
from tools import Images, Settings, Sprites, CreateGraph, CreateEdges
from classes import Graph

pg.init()
pg.mouse.set_visible(1)
pg.display.set_icon(Images.icon)
pg.display.set_caption(Settings.TITLE)
screen = pg.display.set_mode((Settings.windowSizeX, Settings.windowSizeY))
clock = pg.time.Clock()

graph = Graph.Graph()
nodes = CreateGraph.nodes(graph)
CreateEdges.edges(graph)

for i in Sprites.line_list:
    print(i[0])
    print(i[1])

while True:
    screen.fill(Settings.WHITE)
    x = 0
    y = 0

    for i in range(20):
        for j in range(27):
            if i == 0 and j == 0:
                screen.blit(Images.initial, (x, y))
            elif i > 17 and j > 23:
                screen.blit(Images.city, (x, y))
            elif i > 3 or j > 2:
                screen.blit(Images.tree, (x, y))
            x = x + 30
        x = 0
        y = y + 30

    Sprites.all_sprites_list.draw(screen)
    for i in Sprites.line_list:
        pg.draw.line(screen, Settings.BLACK, i[0], i[1])

    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

# Background.createBackground()
