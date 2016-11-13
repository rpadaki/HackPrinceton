import networkx as nx
from networkx.readwrite import json_graph as jg
from scripts import compute_graph as cg
from scripts import pathfinder as pf
from scripts import grapher as gr
import numpy as np
import json
from flask import Flask, render_template, request, Response
from project.server import app

countries = cg.analyze()
name_dict = {}
# name_dict = {k:v.name for k, v in countries.items()}

@app.route('/')
# def submitMoney():
# 	print("hello")
# 	if request.method == '':
# 		value = int(request.form['number'])
# 		add_one = value
# 		return render_template('index.html', string="TESTING", value=add_one)
# 	return render_template('index.html', string="TESTING DEFAULT")
def root():
    return render_template('index.html')

@app.route('/graph')
def graph():
	try:
		amount = float(request.args.get('amount',''))
	except ValueError:
		amount = 200.
	connections = cg.generate(amount,countries)
	f, predecessors, distance = pf.compute(connections)
	g = gr.whole(distance)
	nodes = g.nodes()
	relabel = {k:v for k, v in name_dict.items() if k in nodes}
	g = nx.relabel_nodes(g,relabel,True)
	labels = nx.get_edge_attributes(g,'weight')
	newlabels = {k:amount*(1-np.exp(-v)) for k,v in labels.items()}
	for s in g:
		for f in g:
			if f in g[s]:
				if g[s][f]['weight'] == float('inf'):
					g.remove_edge(s,f)
				else:
					g[s][f]['weight'] = amount*(1-np.exp(-g[s][f]['weight']))
			else:
				continue
	resp = Response(response=json.dumps(jg.node_link_data(g)),
			status=200, \
			mimetype="application/json")
	return(resp)

@app.route('/orbit')
def orbit():
	try:
		amount = float(request.args.get('amount',''))
		start = request.args.get('start','')
	except ValueError:
		amount = 200.
		start = ''
	connections = cg.generate(amount,countries)
	f, predecessors, distance = pf.compute(connections)
	g = gr.planet(start, distance)
	nodes = g.nodes()
	relabel = {k:v for k, v in name_dict.items() if k in nodes}
	g = nx.relabel_nodes(g,relabel,True)
	labels = nx.get_edge_attributes(g,'weight')
	newlabels = {k:amount*(1-np.exp(-v)) for k,v in labels.items()}
	for s in g:
		for f in g:
			if f in g[s]:
				if g[s][f]['weight'] == float('inf'):
					g.remove_edge(s,f)
				else:
					g[s][f]['weight'] = amount*(1-np.exp(-g[s][f]['weight']))
			else:
				continue
	resp = Response(response=json.dumps(jg.node_link_data(g)),
			status=200, \
			mimetype="application/json")
	return(resp)

@app.route('/path')
def path():
	try:
		amount = float(request.args.get('amount',''))
		start = request.args.get('start','')
		end = request.args.get('end','')
	except ValueError:
		amount = 200.
		start = ''
		end = ''
	connections = cg.generate(amount,countries)
	f, predecessors, distance = pf.compute(connections)
	g = gr.single(start, end, predecessors, f)
	nodes = g.nodes()
	relabel = {k:v for k, v in name_dict.items() if k in nodes}
	g = nx.relabel_nodes(g,relabel,True)
	labels = nx.get_edge_attributes(g,'weight')
	newlabels = {k:amount*(1-np.exp(-v)) for k,v in labels.items()}
	for s in g:
		for f in g:
			if f in g[s]:
				if g[s][f]['weight'] == float('inf'):
					g.remove_edge(s,f)
				else:
					g[s][f]['weight'] = amount*(1-np.exp(-g[s][f]['weight']))
			else:
				continue
	resp = Response(response=json.dumps(jg.node_link_data(g)),
			status=200, \
			mimetype="application/json")
	return(resp)

if __name__ == "__main__":
	app.run(debug=True) # Auto-update server in test/dev environment