import networkx as nx

""" Processes graph data to find shortest paths and path lengths
between every node in the graph """

def compute(connections):

	# sets up basic graph, noting that nodes will be added implicitly
	g = nx.DiGraph()

	# add all edges from connections
	for edge in connections:
		g.add_edge(edge[0], edge[1], weight=edge[2])

	# find shortest paths between all nodes
	paths = nx.all_pairs_dijkstra_path(g)
	print(paths)

	# find shortest path length between all nodes
	opt = nx.all_pairs_dijkstra_path_length(g)
	print(opt)