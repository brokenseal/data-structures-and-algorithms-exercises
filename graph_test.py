from unittest import TestCase, main
from graph import Graph


class TestGraph(TestCase):
    def test_has_vertex_count_initial(self):
        graph = Graph()

        self.assertEqual(graph.vertex_count, 0)

    def test_adds_an_edge(self):
        graph = Graph()
        graph.add_edge("A", "B")

        self.assertEqual(list(graph.as_adjency_list().keys()), ["A", "B"])

    def test_shows_all_vertexes(self):
        graph = Graph()
        graph.add_edge("A", "B")
        graph.add_edge("A", "C")
        graph.add_edge("B", "C")
        graph.add_edge("B", "Z")

        self.assertEqual(graph.vertexes, ["A", "B", "C", "Z"])

    def test_has_vertex_count(self):
        graph = Graph()
        graph.add_edge("A", "B")

        self.assertEqual(graph.vertex_count, 2)

    def test_can_be_represented_as_adjency_list(self):
        graph = Graph()
        graph.add_edge("A", "B")
        graph.add_edge("A", "C")
        graph.add_edge("B", "C")

        self.assertEqual(graph.as_adjency_list(), {
            "A": ["B", "C"],
            "B": ["A", "C"],
            "C": ["A", "B"]
        })

    def test_adds_multiple_edges(self):
        graph = Graph()
        graph.add_edge(0, 1)
        graph.add_edge(0, 4)
        graph.add_edge(1, 2)
        graph.add_edge(1, 3)
        graph.add_edge(1, 4)
        graph.add_edge(2, 3)
        graph.add_edge(3, 4)

        self.assertEqual(graph.as_adjency_list(), {
            0: [1, 4],
            1: [0, 2, 3, 4],
            2: [1, 3],
            3: [1, 2, 4],
            4: [0, 1, 3]
        })


class BreadthFirstSearchTestCase(TestCase):
    def test_adds_directed_edge(self):
        graph = Graph()
        graph.add_directed_edge(0, 1)
        graph.add_directed_edge(0, 4)
        graph.add_directed_edge(1, 2)
        graph.add_directed_edge(1, 3)
        graph.add_directed_edge(1, 4)
        graph.add_directed_edge(2, 3)
        graph.add_directed_edge(3, 4)

        self.assertEqual(graph.as_adjency_list(), {
            0: [1, 4],
            1: [2, 3, 4],
            2: [3],
            3: [4],
            4: []
        })

    def test_simple_breadth_first_search(self):
        graph = Graph()
        graph.add_directed_edge(0, 1)
        graph.add_directed_edge(0, 2)
        graph.add_directed_edge(1, 2)
        graph.add_directed_edge(2, 0)
        graph.add_directed_edge(2, 3)

        self.assertEqual(graph.breadth_first_search(0), [0, 1, 2, 3])

    def test_letter_base_vertexes_breadth_first_search_with_directed_edges(self):
        graph = Graph()
        graph.add_directed_edge("A", "B")
        graph.add_directed_edge("B", "C")
        graph.add_directed_edge("C", "A")
        graph.add_directed_edge("C", "D")
        graph.add_directed_edge("D", "E")

        self.assertEqual(graph.breadth_first_search("E"), ["E"])

    def test_letter_base_vertexes_breadth_first_search_with_normal_edges_starting_from_the_end(self):
        graph = Graph()
        graph.add_edge("A", "B")
        graph.add_edge("B", "C")
        graph.add_edge("C", "A")
        graph.add_edge("C", "D")
        graph.add_edge("D", "E")

        self.assertEqual(graph.breadth_first_search("E"),
                         ["E", "D", "C", "B", "A"])

    def test_letter_base_vertexes_breadth_first_search_with_normal_edges_starting_from_the_middle(self):
        graph = Graph()
        graph.add_edge("A", "B")
        graph.add_edge("B", "C")
        graph.add_edge("C", "A")
        graph.add_edge("C", "D")
        graph.add_edge("D", "E")

        self.assertEqual(graph.breadth_first_search("C"),
                         ["C", "B", "A", "D", "E"])

    def test_depth_first_search(self):
        graph = Graph()
        graph.add_edge(0, 1)
        graph.add_edge(0, 2)
        graph.add_edge(1, 2)
        graph.add_edge(2, 0)
        graph.add_edge(2, 3)

        self.assertEqual(graph.depth_first_search(0), [0, 1, 2, 3])

    def test_depth_first_search_with_letters(self):
        graph = Graph()
        graph.add_edge("A", "B")
        graph.add_edge("B", "C")
        graph.add_edge("C", "A")
        graph.add_edge("C", "D")
        graph.add_edge("D", "E")
        graph.add_edge("B", "F")
        graph.add_edge("F", "G")
        graph.add_edge("G", "H")
        graph.add_edge("G", "I")

        self.assertEqual(
            graph.as_adjency_list(), {
                "A": ["B", "C"],
                "B": ["A", "C", "F"],
                "C": ["B", "A", "D"],
                "D": ["C", "E"],
                "E": ["D"],
                "F": ["B", "G"],
                "G": ["F", "H", "I"],
                "H": ["G"],
                "I": ["G"]
            })
        self.assertEqual(graph.depth_first_search("A"),
                         ["A", "B", "C", "D", "E", "F", "G", "H", "I"])


if __name__ == "__main__":
    main()
