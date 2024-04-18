import networkx as nx

def remove_cycles_from_digraph(g):
    """
    Remove all cycles from the DiGraph to make it acyclic.

    Args:
        G (nx.DiGraph): A Directed Acyclic Graph (DAG).
    """
    search_for_cycles = True
    while search_for_cycles:
        for cycle_path in nx.simple_cycles(g):
            try:
                g.remove_edge(cycle_path[-1], cycle_path[0])
            except nx.NetworkXError:
                # edge has already been disjointed by a previous edge removal.
                # Restart cycle generator.
                search_for_cycles = (
                    False  # Temporary condition which will be reversed.
                )
                break
        search_for_cycles = not (search_for_cycles)