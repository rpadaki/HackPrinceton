import networkx as nx

""" Processes graph data to find shortest paths and path lengths
between every node in the graph """

def compute(connections):

    # sets up basic graph, noting that nodes will be added implicitly
    g = nx.DiGraph()

    # add all edges from connections
    for edge in connections:
        g.add_edge(edge[0], edge[1], weight=edge[2])

    predecessors, distance = nx.floyd_warshall_predecessor_and_distance(g, weight='weight')
    return g, predecessors, distance
