# Write your test here
import pytest
from challenge01 import Node,Edge,Grahp

def test_graph1():
    graph1 = Grahp()
    a = graph1.add_node("A")
    b = graph1.add_node("B")
    c = graph1.add_node("C")
    d = graph1.add_node("D")
    e = graph1.add_node("E")

    graph1.add_edge(a,b)
    graph1.add_edge(a,e)
    graph1.add_edge(b,c)
    graph1.add_edge(b,e)
    graph1.add_edge(e,d)
    graph1.add_edge(d,c)

    assert graph1.GraphBreadthFirst(a) ==['A', 'B', 'E', 'C', 'D']

def test_graph2():
    graph2 = Grahp()

    a = graph2.add_node("A")
    b = graph2.add_node("B")
    c = graph2.add_node("C")
    e = graph2.add_node("E")
    d = graph2.add_node("D")
    f = graph2.add_node("F")
    g = graph2.add_node("G")
    h = graph2.add_node("H")
    i = graph2.add_node("I")
    k = graph2.add_node("K")

    graph2.add_edge(a,c)
    graph2.add_edge(a,e)
    graph2.add_edge(a,b)

    graph2.add_edge(b,d)
    graph2.add_edge(e,g)
    graph2.add_edge(c,f)
    graph2.add_edge(e,f)

    graph2.add_edge(d,e)
    graph2.add_edge(g,h)
    graph2.add_edge(f,i)
    graph2.add_edge(f,h)

    graph2.add_edge(h,k)
    graph2.add_edge(i,k)

    assert graph2.GraphBreadthFirst(a) ==['A', 'C', 'E', 'B', 'F', 'G', 'D', 'I', 'H', 'K']
