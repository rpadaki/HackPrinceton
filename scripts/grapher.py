""" Outputs graphs in ready-to-draw format """
import networkx as nx

def tree(start, predecessors, graph):
	# graphs the shortest path between one node and every other node
	g = nx.DiGraph()

	# for every pair of predecessors, creates an edge between the two
	# with the same weight as determined by connections
	# note that the edge starts at the value and goes to the key
	print(predecessors[start])
	for key, value in predecessors[start].items():
		g.add_edge(value, key, weight=graph[value][key]["weight"])

	return g

def single(start, end, predecessors, graph):
	# graphs the shortest path between two specific nodes
	g = nx.DiGraph()

	# handle the case where the start and end are the same
	if start == end:
		g.add_node(start)
		return g

	# search through the list for the end node and work backwards
	# assumes that the start and end are connected
	previous = predecessors[start][end]
	while True:
		# while we haven't reached the start
		# add an edge for each connection
		g.add_edge(previous, end, weight=graph[previous][end]["weight"])

		# move onto the next pair
		end = previous
		if end == start:
			break
			
		previous = predecessors[start][previous]

		if end == start:
			break

	# at this point, should have fully-connected 1D graph
	return g

def planet(start, distances):
	# graphs one node and connects it to all other nodes, with the length
	# being a function of the actual distance (no path included)
	g = nx.DiGraph()

	# for each key-value pair in distances, adds an edge whose start is the
	# start point, end is the key, and weight is the value
	# only does so if distance is not infinite
	for key, value in distances[start].items():
		if not value == "inf" and not start == key:
			g.add_edge(start, key, weight=value)

	return g



