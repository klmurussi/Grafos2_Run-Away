# Algoritmo do jogo

1. Gera uma quantidade randomica de nós, no código essa ação é realizada em `main.py` pela função:<br>
  ```python
  (start, end) = CreateGraph.nodes(graph)
  ```
2. Gera uma quantidae randomica de arestas
3. Passa em cada nó, e gera arestas nele baseado na qtd do passo 2, no código essa ação é realizada em conjunto com o passo 2 na `main.py` pela função:<br>
  ```python
  CreateEdges.edges(graph, start, end)
  ```
4. Caso não haja conexão entre o nó inicial e o final, o passo 2 e 3 são repetidos, também nesse passo é calculada a menor distância do nó inicial ao final, no código essa ação é realizada em `main.py` pela função:<br>
  ```python
  distance = graph.dijkstra_end(start, end)
  while distance is None:     
      CreateEdges.edges(graph, start, end)      
      distance = graph.dijkstra_end(start, end)
  ```
5. Verificar se o usuário adivinhou o menor caminho com sucesso, no código essa ação é realizada em `InputBox.py`, que é a classe que rege a caixa de texto presente no jogo:<br>
  ```python
  if (str(distance) == self.text):
      return True
  ```
6. É verificado se o jogo chegou ao fim baseado no passo 5, essa ação é realizada em `main.py`<br>
  ```python
  end = box.handle_event(event, distance, screen)
      if end:
          end_game.end_game(screen)
  ```

Obs1.: No passo 4 é utilizado o algoritmo de dijkstra para essa tarefa, pois o código utiliza o algoritmo de dijkstra para encontrar a menor distância que o usuário deve adivinhar. E na maioria das vezes são geradas arestas suficiente, sendo um gasto maior testar em todas as utilizações se os dois nós estão conectados.

Obs2.: Há outras partes do código que são relacionadas ao funcionamento do jogo, porém esse é o algoritmo básico de como o jogo funciona.


