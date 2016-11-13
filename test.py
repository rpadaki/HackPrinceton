import d3py
import networkx as nx
import logging
import pathfindertesting
logging.basicConfig(level=logging.DEBUG)
paths, opt = pathfindertesting.test()
g=nx.DiGraph()
for start in opt:
	for end in opt[start]:
		g.add_edge(start,end,weight=opt[start][end])
with d3py.NetworkXFigure(g,width=500, height=500) as p:
	p += d3py.ForceLayout()
	p.show()