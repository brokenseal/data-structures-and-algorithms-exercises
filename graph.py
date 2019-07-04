from linked_list import SinglyLinkedList


class Graph:
    def __init__(self):
        self._adjency_list = {}

    @property
    def vertex_count(self):
        return len(self.vertexes)

    @property
    def vertexes(self):
        return list(self._adjency_list.keys())

    def as_adjency_list(self):
        return {
            vertex: children.as_list()
            for vertex, children in self._adjency_list.items()
        }

    def add_edge(self, source, destination):
        self._prepare_vertexes(source, destination)
        self._adjency_list[source].append(destination)
        self._adjency_list[destination].append(source)

    def add_directed_edge(self, source, destination):
        self._prepare_vertexes(source, destination)
        self._adjency_list[source].append(destination)

    def _prepare_vertexes(self, source, destination):
        if source not in self._adjency_list:
            self._adjency_list[source] = SinglyLinkedList()
        if destination not in self._adjency_list:
            self._adjency_list[destination] = SinglyLinkedList()

    def breadth_first_search(self, starting_vertex):
        adjency_list = self.as_adjency_list()
        current_vertexes = [starting_vertex]
        visited = []

        while len(current_vertexes) != 0:
            for vertex in current_vertexes:
                if vertex not in visited:
                    visited.append(vertex)

            next_vertexes_to_visit = []
            for vertex in current_vertexes:
                for vertex_to_visit in adjency_list[vertex]:
                    if vertex_to_visit not in next_vertexes_to_visit \
                            and vertex_to_visit not in visited:
                        next_vertexes_to_visit.append(vertex_to_visit)
            current_vertexes = next_vertexes_to_visit
        return visited


# if __name__ == "__main__":
#     graph = Graph()
#     graph.add_directed_edge(0, 1)
#     graph.add_directed_edge(0, 2)
#     graph.add_directed_edge(1, 2)
#     graph.add_directed_edge(2, 0)
#     graph.add_directed_edge(2, 3)

#     result = graph.breadth_first_search(0)
#     print("------------------------------------------------")
#     print(result)
#     print("------------------------------------------------")
