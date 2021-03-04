from classes import Node, Connection
import random
from tools import Sprites
from pythonds import PriorityQueue
from math import inf


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
        edge = Connection.Connection(
            (src.rect.x+16, src.rect.y+16), (dest.rect.x+16, dest.rect.y+16), weight)

    def dijkstra_end(self, start, end):
        distance = {node: inf for node in self.graph}
        visited = {node: False for node in self.graph}
        pq = PriorityQueue()
        distance[start] = 0
        pq.add((0, start))
        for next_node in self.graph[start]:
            initial_weight = self.weights[(start.num, next_node.num)]
            pq.add((initial_weight, next_node))
        while not pq.isEmpty():
            currentVert = pq.delMin()
            visited[currentVert] = True
            if (visited[end]):
                break
            for nextVert in self.graph[currentVert]:
                newDist = distance[currentVert] \
                    + self.weights[(currentVert.num, nextVert.num)]
                if newDist < distance[nextVert]:
                    distance[nextVert] = newDist
                    pq.decreaseKey(nextVert, newDist)
                    pq.add((newDist, nextVert))
        return distance[end]


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
