import networkx as nx
import matplotlib.pyplot as plt
from pylab import *



mat = []
# Read input
with open('input/test.txt', 'r') as f:
    lines = f.readlines()
    for i in range (len(lines)):
        mat += [list(map(int, lines[i].split()))]

# Create Nodes
g = nx.DiGraph()
for i in range(len(mat)):
    g.add_node(i)

#Create Edges

for i in range(len(mat)):
    for j in range(len(mat)):
        if mat[i][j] != -1:
            g.add_edge(i, j, weight=mat[i][j])

pos = nx.spring_layout(g)
weights = nx.get_edge_attributes(g, 'weight')

nx.draw_networkx_edge_labels(g, pos, edge_labels=weights)
nx.draw(g, pos,with_labels = True)

plt.show()
