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
pg.font.init() # you have to call this at the start, 
                   # if you want to use this module.
myfont = pg.font.SysFont('Comic Sans MS', 30)

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

    for i in Sprites.line_list:
        if i[0][0] < i[1][0]:
            xMenor = i[0][0]
            xMaior = i[1][0]
        else:
            xMenor = i[1][0]
            xMaior = i[0][0]

        if i[0][1] < i[1][1]:
            yMenor = i[0][1]
            yMaior = i[1][1]
        else:
            yMenor = i[1][1]
            yMaior = i[0][1]


        pg.draw.line(screen, Settings.BLACK, i[0], i[1])
        text = str(i[2])
        textsurface = myfont.render(text, False, (0, 0, 0))
        posX =  ((xMaior - xMenor)/2) + xMenor 
        posY =  ((yMaior - yMenor)/2) + yMenor
        screen.blit(textsurface, (posX, posY))
        print (text)

    Sprites.all_sprites_list.draw(screen)

    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

# Background.createBackground()
