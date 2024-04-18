import networkx as nx
from cycle_remover import remove_cycles_from_digraph

def test_remove_cycles_from_digraph():
    G = nx.read_edgelist('cyclic_digraph.edges', create_using=nx.DiGraph())
    DAG = remove_cycles_from_digraph(G)
    assert nx.is_directed_acyclic_graph(DAG)
