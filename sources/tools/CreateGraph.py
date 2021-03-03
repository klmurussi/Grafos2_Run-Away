import random as rand
import pygame as pg
from tools import Images, Sprites
from classes import Graph

graph = Graph.Graph()
listPOS = []

def nodes () :
	number = rand.randint(10,20)
	#number = 39
	print (number)
	num = 1
	while True:
		x = 0
		y = 0
		for i in range (12):
			for j in range (16):
				exist = rand.randint(1,10)
				if exist == 1:
					pos = (x,y)
					mark = False
					for k in listPOS:
						if pos == k:
							mark = True
					if mark == False:
						graph.add_node(num, x, y)
						num = num + 1
						listPOS.append((x,y))
						if num == number+1:
							return
				x = x + 50
			x = 0
			y = y + 50