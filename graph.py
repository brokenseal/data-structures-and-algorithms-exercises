import math

from linked_list import SinglyLinkedList


class Graph:
    def __init__(self):
        self._adjency_list = {}
        self._weights = {}

    @property
    def vertex_count(self):
        return len(self.vertexes)

    @property
    def vertexes(self):
        return list(self._adjency_list.keys())

    def as_adjency_list(self, values_only=True):
        if values_only:
            return {
                vertex: [edge.vertex for edge in edges]
                for vertex, edges in self._adjency_list.items()
            }
        return {
            vertex: edges
            for vertex, edges in self._adjency_list.items()
        }

    def add_edge(self, source, destination, weight=None):
        self._prepare_vertexes(source, destination)
        self._adjency_list[source].append(Edge(destination, weight))
        self._adjency_list[destination].append(Edge(source, weight))

    def add_directed_edge(self, source, destination, weight=None):
        self._prepare_vertexes(source, destination)
        self._adjency_list[source].append(Edge(destination, weight))

    def _prepare_vertexes(self, source, destination):
        if source not in self._adjency_list:
            self._adjency_list[source] = []
        if destination not in self._adjency_list:
            self._adjency_list[destination] = []

    def breadth_first_search(self, starting_vertex):
        adjency_list = self.as_adjency_list()
        current_vertexes = [starting_vertex]
        result = []

        while len(current_vertexes) != 0:
            for vertex in current_vertexes:
                result.append(vertex)

            next_vertexes_to_visit = []
            for vertex in current_vertexes:
                for vertex_to_visit in adjency_list[vertex]:
                    #vertex_to_visit = edge.vertex
                    if vertex_to_visit not in next_vertexes_to_visit \
                            and vertex_to_visit not in result:
                        next_vertexes_to_visit.append(vertex_to_visit)
            current_vertexes = next_vertexes_to_visit
        return result

    def depth_first_search(self, starting_vertex):
        visited = []
        adjency_list = self.as_adjency_list()
        return self._dfs_visit(starting_vertex, adjency_list, visited)

    def _dfs_visit(self, starting_vertex, adjency_list, visited):
        visited.append(starting_vertex)
        result = [starting_vertex]
        adjacent_vertexes = adjency_list[starting_vertex]

        for edge in adjacent_vertexes:
            if edge in visited:
                continue
            result_from_adjacent_vertex = self._dfs_visit(
                edge, adjency_list, visited)
            result.extend(result_from_adjacent_vertex)
            visited.extend(result_from_adjacent_vertex)
        return result


class Edge:
    def __init__(self, vertex, weight=None):
        self.vertex = vertex
        self.weight = weight

    def __eq__(self, cmp):
        return self.vertex == cmp.vertex and self.weight == cmp.weight

    def __gt__(self, cmp):
        return self.weight > cmp

    def __lt__(self, cmp):
        return self.weight < cmp


# Work in progress
class DijkstraPathSearchEngine:
    def __init__(self, graph):
        self.graph = graph

    def get_matrix(self, start, end):
        visited = []
        matrix = {}
        adjency_list = self.graph.as_adjency_list(False)

        def should_visit(edges):
            not_visited = [
                edge for edge in edges if edge.vertex not in visited]
            sorted_edges = sorted(not_visited)

            if len(sorted_edges) == 0:
                return None
            return sorted_edges[0]

        def visit(vertex, weight, previous_vertex):
            visited.append(vertex)
            neighbours = adjency_list[vertex]
            next_edge = should_visit(neighbours)
            if next_edge is None:
                return
            if vertex not in matrix:
                #distance = 0
                # if previous_vertex is not None:
                    #distance = math.inf
                    #distance = weight
                matrix[vertex] = (weight, previous_vertex,)
            else:
                distance_to_start, _ = matrix[vertex]
                distance_to_start = distance_to_start + weight  # next_edge.weight
            visit(next_edge.vertex, next_edge.weight, vertex)

        visit(start, 0, None)
        return matrix
