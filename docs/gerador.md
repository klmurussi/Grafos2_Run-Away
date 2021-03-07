# Algoritmo de gerar uma árvore

1. Gera uma quantidade randomica de nós, no código essa ação é realizada em `main.py` pela função:<br>
  ```python
  (start, end) = CreateGraph.nodes(graph)
  ```
2. Gera uma quantidae randomica de arestas
3. Passa em cada nó, e gera arestas nele baseado na qtd do passo 2, no código essa ação é realizada em conjunto com o passo 2 na `main.py` pela função:<br>
  ```python
  CreateEdges.edges(graph, start, end)
  ```
4. Caso não haja conexão entre o nó inicial e o final, o passo 2 e 3 são repetidos, no código essa ação é realizada em `main.py` pela função:<br>
  ```python
  distance = graph.dijkstra_end(start, end)
  while distance is None:     
      CreateEdges.edges(graph, start, end)      
      distance = graph.dijkstra_end(start, end)
  ```
Obs.: No passo 4 é utilizado o algoritmo de dijkstra para essa tarefa, pois o código utiliza o algoritmo de dijkstra para encontrar a menor distância que o usuário deve adivinhar. E na maioria das vezes são geradas arestas suficiente, sendo um gasto maior testar em todas as utilizações se os dois nós estão conectados.


