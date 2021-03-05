import pygame as pg
import sys
from tools import Images, Settings, Sprites, CreateGraph, CreateEdges, end_game
from classes import Graph, InputBox
from math import inf

pg.init()
pg.mouse.set_visible(1)
pg.display.set_icon(Images.icon)
pg.display.set_caption(Settings.TITLE)
screen = pg.display.set_mode((Settings.windowSizeX, Settings.windowSizeY))
clock = pg.time.Clock()

pg.font.init()
myfont = pg.font.SysFont('Comic Sans MS', 30)
guide_font = pg.font.SysFont('Comic Sans MS', 22)
graph = Graph.Graph()
(start, end) = CreateGraph.nodes(graph)

CreateEdges.edges(graph, start, end)
distance = graph.dijkstra_end(start, end)

while distance is None:
    CreateEdges.edges(graph, start, end)
    distance = graph.dijkstra_end(start, end)


# para "roubar" descomente a linha abaixo
# print("distancia", distance)

input_box1 = InputBox.InputBox(0, 560, 140, 32)
input_boxes = [input_box1]
done = False
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
        posX = ((xMaior - xMenor)/2) + xMenor
        posY = ((yMaior - yMenor)/2) + yMenor
        screen.blit(textsurface, (posX, posY))

    guideText = guide_font.render(
        "Digite o menor caminho até a cidade", False, (0, 0, 0))
    screen.blit(guideText, (0, 545))
    Sprites.all_sprites_list.draw(screen)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        for box in input_boxes:
            end = box.handle_event(event, distance, screen)
            if end:
                end_game.end_game(screen)

    for box in input_boxes:
        box.update()

    #screen.fill((30, 30, 30))
    for box in input_boxes:
        box.draw(screen)

    pg.display.update()
