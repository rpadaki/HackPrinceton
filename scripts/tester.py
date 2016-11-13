from pathfinder import *
from compute_graph import *

def main():
	# clean and analyze the data
	analyze()

	# generate the graph for some amount requested by the user
	compute(generate(10000))

if __name__ == "__main__":
	main()