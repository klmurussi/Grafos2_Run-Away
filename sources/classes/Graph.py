from classes import Node, Connection
import random
from tools import Sprites

class Graph:
    def __init__(self):
        self.graph = {}
        self.weights = {}

    def add_node(self, num, x, y):
        empty_node = Node.Node(num, x, y)
        self.graph[empty_node] = []
        return empty_node

    def add_edge(self, src, dest, weight):
        if (dest in self.graph[src]):
            return
        self.graph[src].append(dest)
        self.graph[dest].append(src)
        self.weights[(src.num, dest.num)] = weight
        self.weights[(dest.num, src.num)] = weight
        edge = Connection.Connection(src, dest)



"""graph = Graph()
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
              str(graph.weights[(i.num, j.num)]))"""
 
