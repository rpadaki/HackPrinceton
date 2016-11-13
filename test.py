import networkx as nx
from networkx.readwrite import json_graph as jg
import pathfindertesting
import json
from flask import Flask
from flask import request
app=Flask(__name__)

@app.route('/graph')
def graph():
	print(request.args.get('amount',''))
	paths, opt = pathfindertesting.test()
	g=nx.DiGraph()
	for start in opt:
		for end in opt[start]:
			g.add_edge(start,end,weight=opt[start][end])
	return json.dumps(jg.node_link_data(g))

if __name__ == "__main__":
	app.run()

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