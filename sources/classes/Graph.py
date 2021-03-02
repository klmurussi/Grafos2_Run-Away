# from classes import Node
from typing import Counter
import Node
#import random

# random.seed(413215412321)


class Graph:
    def __init__(self):
        self.graph = {}
        self.weights = {}

    def add_node(self, num):
        empty_node = Node.Node(num)
        self.graph[empty_node] = []
        return empty_node

    def add_edge(self, src, dest, weight):
        if (dest in self.graph[src]):
            return
        self.graph[src].append(dest)
        self.graph[dest].append(src)
        self.weights[(src.num, dest.num)] = weight
        self.weights[(dest.num, src.num)] = weight


""" graph = Graph()
nodeList = []

for i in range(10):
    print("creating node" + str(i))
    nodeList.append(graph.add_node(i))
count = 1
for i in range(9):
    graph.add_edge(nodeList[count-1], nodeList[count], random.randint(1, 10))
    count = count + 1

for i in graph.graph:
    print("node: " + str(i.num) + " Edges:")
    for j in graph.graph[i]:
        print("vizinho: " + str(j.num) + " peso: " +
              str(graph.weights[(i.num, j.num)]))
 """
