import networkx as nx
import matplotlib as mpl

""" Processes graph data to find shortest paths and path lengths
between every node in the graph """

# sets up basic graph
countries = 7
g = nx.DiGraph()
g.add_nodes_from(range(1, countries))

# open and read data file, adding all vertices to graph
# each line is assumed to be a vertex in the form: [start] [end] [weight]
reader = open("data.txt", "r")
for line in reader:
	current = line.split()
	g.add_edge(int(current[0]), int(current[1]), weight=float(current[2]))
reader.close()

nx.write_edgelist(g, "edges.txt")

# find shortest paths between all nodes
paths = nx.all_pairs_dijkstra_path(g)
print(paths)

# find shortest path length between all nodes
opt = nx.all_pairs_dijkstra_path_length(g)
print(opt)

