import networkx as nx
from networkx.readwrite import json_graph as jg
from scripts import pathfindertesting
import json
from flask import Flask, render_template, request, Response
from project.server import app

@app.route('/', methods=['GET', 'POST'])
def home():
	print("hello")
	if request.method == 'POST':
		value = int(request.form['number'])
		add_one = value
		return render_template('index.html', string="TESTING", value=add_one)
	return render_template('index.html', string="TESTING DEFAULT")

@app.route('/graph')
def graph():
	print(request.args.get('amount',''))
	paths, opt = pathfindertesting.test()
	g=nx.DiGraph()
	for start in opt:
		for end in opt[start]:
			g.add_edge(start,end,weight=opt[start][end])
	resp = Response(response=json.dumps(jg.node_link_data(g)),
			status=200, \
			mimetype="application/json")
	return(resp)

if __name__ == "__main__":
	app.run(debug=True) # Auto-update server in test/dev environment