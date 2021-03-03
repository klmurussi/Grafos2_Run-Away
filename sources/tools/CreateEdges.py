import random
from tools import Sprites


def edges(graph):
    all_nodes_non_connected = Sprites.node_list.sprites()
    for i in Sprites.node_list:
        edge_qtt = random.randint(1, 3)
        if edge_qtt == 1:
            edge_qtt = random.randint(1, 3)
        if edge_qtt == 1:
            edge_qtt = random.randint(1, 3)
        print("source = " + str(i.num))
        for j in range(edge_qtt):
            if not all_nodes_non_connected:
                return
            dest = random.choice(all_nodes_non_connected)
            while dest == i:
                dest = random.choice(all_nodes_non_connected)
            all_nodes_non_connected.remove(dest)
            graph.add_edge(i, dest, random.randint(1, 10))
