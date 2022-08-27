import pytest
from graph_breadth_first.graph_breadth_first import Graph, Vertex


def test_breadth_first(graph):
    expected = ['1', '2', '3']
    actual = graph
    assert actual == expected

@pytest.fixture
def graph():
    graph = Graph()
    val1 = graph.add_node("1")
    val2 = graph.add_node("2")
    val3 = graph.add_node("3")
    graph.add_edge(val1, val2, 50)
    graph.add_edge(val1, val3, 1)
    graph.add_edge(val2, val3, 1)

    return graph.bfs(val1)
