<<<<<<< HEAD:test.py
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
=======
>>>>>>> f41509158617d25f198a50ab531252478ec955b8
=======
>>>>>>> 4fb8372713ea3be1fda48d2b32488d68609648ba:FlaskWebProject/graphs.py
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
<<<<<<< HEAD:test.py
	app.run()
<<<<<<< HEAD
>>>>>>> 1de2ae1c04d2198f6fecc5b2517ddf30394f655c
=======
=======
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
>>>>>>> bca8b0139cfeb6016edc723de250b0a90d3eac97
>>>>>>> f41509158617d25f198a50ab531252478ec955b8
=======
	app.run()
>>>>>>> 4fb8372713ea3be1fda48d2b32488d68609648ba:FlaskWebProject/graphs.py
