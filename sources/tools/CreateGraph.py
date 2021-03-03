import random as rand
import pygame as pg
from tools import Images, Sprites
from classes import Graph

graph = Graph.Graph()
listX = []
listY = []

def nodes () :
	number = rand.randint(10,20)
	x = 10
	y = 0
	pos = []
	for i in range (15):
		for j in range (17):
			exist = rand.randint(1,10)
			if exist == 1:
				graph.add_node(number, x, y)
			x = x + 50
		x = 0
		y = y + 50