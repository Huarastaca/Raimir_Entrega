import math
import pprint


# https://docs.python.org/3/library/pprint.html

class Dijkstra:
    def __init__(self, graph, vertice_inicial):
        self.grafo = graph
        self.vertice_inicial = vertice_inicial
        self.vertices = list(graph.keys())

        # distancia minima do vertice inicial
        self.vertice_labels = {vertice: {'distancia': math.inf, 'predecessor': None} for vertice in self.vertices}

        # Ja que setamos o vertice inicial, a distancia dele é 0
        self.vertice_labels[vertice_inicial]['distancia'] = 0

    def _get_peso(self, vertice1, vertice2):
        try:
            return self.grafo[vertice1][vertice2]
        except KeyError:
            return math.inf

    def _set_label(self, vertice, weight, prev=None):
        self.vertice_labels[vertice]['distancia'] = weight

        if prev is not None:
            self.vertice_labels[vertice]['predecessor'] = prev

    def _get_label(self, vertice):
        if vertice in self.vertice_labels:
            return self.vertice_labels[vertice]
        else:
            return {'distancia': math.inf, 'predecessor': None}

    def dijkstra(self):
        interiors = [self.vertice_inicial]
        max_interior_vertices = len(self.vertices)

        while True:
            exteriors = [vertice for vertice in self.vertices if vertice not in interiors]

            # Vertice mais proximo do inicio
            vertice_proximo = None

            # Distancia total do vertice inicial até o momento
            vertice_proximo_distancia = math.inf

            for exterior in exteriors:
                exterior_label = self._get_label(exterior)

                # Menor distancia atual do vertice inicial
                menor_distancia = exterior_label['distancia']

                # Ultimo vetor pai achado quando chegamos no menor caminho
                # P(v)

                predecessor = exterior_label['predecessor']

                for interior in interiors:

                    # Distancia mais curta do vertice inicial (i) até o vertice (j)
                    # C(i,j)

                    distancia_exterior = self._get_label(interior)['distancia'] + self._get_peso(interior, exterior)

                    if distancia_exterior < menor_distancia:
                        menor_distancia = distancia_exterior
                        predecessor = interior

                self._set_label(exterior, menor_distancia, predecessor)

                # Procurando adjacencia de V a u
                if menor_distancia < vertice_proximo_distancia:
                    vertice_proximo_distancia = menor_distancia
                    vertice_proximo = exterior

            interiors.append(vertice_proximo)

            if len(interiors) == max_interior_vertices:
                break

    def menor_caminho(self, vertice):
        if vertice is None:
            return []

        return self.menor_caminho(self.vertice_labels[vertice]['predecessor']) + [vertice]


graph = {'A': {'B': 5, 'C': 7, 'D': 1},
         'B': {'C': 2},
         'C': {'D': 6, 'E': 5},
         'D': {'B': 3, 'F': 5, 'G': 3},
         'E': {'F': 4},
         'F': {'C': 1},
         'G': {'G': 1}
         }

dijkstra = Dijkstra(graph, vertice_inicial='C')

dijkstra.dijkstra()

# PPrinta novos rotulos dado a cada vertice que lhe foi atualizado a cada chave/vertice do dicionario (distancia inicial, ultimo predecessor do ponto que chegamos)
pprint.pprint(dijkstra.vertice_labels)

# Constroi e printa o menor caminho do vertice Inicial (nesses casos C) até cada vertice alcançavel
for vertice in dijkstra.vertices:
    print('C ->', vertice + ':', dijkstra.menor_caminho(vertice))

print("--------------------------------------------------------------")
print("Proximo Grafo")
print("--------------------------------------------------------------")

graph2 = {'A': {'L': 2, 'E': 5, 'F': 1},
          'B': {'C': 11, 'I': 2},
          'C': {'F': 3, 'D': 3, 'G': 5, 'J': 6},
          'D': {'N': 5},
          'E': {'B': 1, 'H': 8},
          'F': {'I': 6, 'M': 4},
          'G': {'F': 1, 'D': 4},
          'H': {'M': 7},
          'I': {'H': 10},
          'J': {'L': 8, 'K': 13},
          'K': {},
          'L': {},
          'M': {'K': 9},
          'N': {'K': 6}
          }

dijkstra2 = Dijkstra(graph2, vertice_inicial='C')

dijkstra2.dijkstra()
pprint.pprint(dijkstra2.vertice_labels)
for vertice in dijkstra2.vertices:
    print('C ->', vertice + ':', dijkstra2.menor_caminho(vertice))