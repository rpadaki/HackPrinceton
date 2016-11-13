import networkx as nx
from grapher import *
import matplotlib.pyplot as plt

""" Processes graph data to find shortest paths and path lengths
between every node in the graph """

def main():

	# sets up basic graph, noting that nodes will be added implicitly
	g = nx.DiGraph()

	g.add_edge("AUS", "USA", weight=4)
	g.add_edge("USA", "AUS", weight=3)
	g.add_edge("AUS", "FRN", weight=5)
	g.add_edge("AUS", "CHN", weight=-1)
	g.add_edge("FRN", "USA", weight=7)
	g.add_edge("FRN", "CHN", weight=6)
	g.add_edge("UK", "CHN", weight=7)
	g.add_edge("USA", "UK", weight=2)
	g.add_edge("UK", "OMG", weight=-3)
	g.add_edge("USA", "FRN", weight=1)

	predecessors, distances = nx.floyd_warshall_predecessor_and_distance(g, weight='weight')
	one = tree("AUS", predecessors, g)
	two = single("AUS", "OMG", predecessors, g)
	three = planet("AUS", distances)

	# graph all the graphs
	print(one.nodes())
	print(one.edges())
	print("one")
	print(two.nodes())
	print(two.edges())
	print("two")
	print(three.nodes())
	print(three.edges())
	print("three")


if __name__ == "__main__":
	main()