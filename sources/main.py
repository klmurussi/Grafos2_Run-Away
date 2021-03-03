import pygame as pg
import sys
from tools import Images, Settings, Sprites, CreateGraph

pg.init()
pg.mouse.set_visible(1)
pg.display.set_icon(Images.icon)
pg.display.set_caption(Settings.TITLE)
screen = pg.display.set_mode((Settings.windowSizeX, Settings.windowSizeY))
clock = pg.time.Clock()

nodes = CreateGraph.nodes()

while True:
	screen.fill(Settings.WHITE)
	x = 0
	y = 0
	for i in range (20):
		for j in range (27):
			if i > 17 and j > 23:
				screen.blit(Images.city, (x, y))
			else:
				screen.blit(Images.tree, (x, y))
			x = x + 30
		x = 0
		y = y + 30

	Sprites.all_sprites_list.draw(screen)

	pg.display.update()
	for event in pg.event.get():
		if event.type == pg.QUIT:
			pg.quit()
			sys.exit()

#Background.createBackground()