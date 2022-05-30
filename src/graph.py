import networkx as nx
import matplotlib.pyplot as plt
from pylab import *


class clickEvent:
    def __init__(self, x, y, key):
        self.data = list(zip(x, y, key))
        self.key = key
        self.xtol = ((max(x) - min(x)) / float(len(x))) / 2
        self.ytol = ((max(y) - min(y)) / float(len(y))) / 2
        self.axis = gca()
        self.links = []
        self.drawnAnnotations = {}
        self.sourceNode = None
        self.targetNode = None
        self.sourceNodeKey = None

    def __call__(self, event):
        if event.inaxes:
            clickX = event.xdata
            clickY = event.ydata
            if self.axis is None or self.axis==event.inaxes:
                nodes = []
                smallest_x_dist = float('inf')
                smallest_y_dist = float('inf')

                for x,y,a in self.data:
                    if abs(clickX-x)<=smallest_x_dist and abs(clickY-y)<=smallest_y_dist :
                        dx, dy = x - clickX, y - clickY
                        nodes.append((dx*dx+dy*dy,x,y, a) )
                        smallest_x_dist=abs(clickX-x)
                        smallest_y_dist=abs(clickY-y)
                if nodes:
                    nodes.sort() # to select the nearest node
                    distance, x, y, node = nodes[0]
                    self.drawAnnote(event.inaxes, x, y, node)
                    return node

    def drawAnnote(self, axis, x, y, annote):
        if (x, y) in self.drawnAnnotations:
            markers = self.drawnAnnotations[(x, y)]
            for m in markers:
                m.set_visible(not m.get_visible())
            self.axis.figure.canvas.draw()
        else:
            t = axis.text(x, y, "%s" % (annote) )
            m = axis.scatter([x], [y], marker='v', c='r', zorder=100)
            self.drawnAnnotations[(x, y)] = (t, m)
            self.axis.figure.canvas.draw()

def getMat():
    mat = []
    # Read input
    with open('input/test.txt', 'r') as f:
        lines = f.readlines()
        for i in range (len(lines)):
            mat += [list(map(int, lines[i].split()))]
    return mat

def getGraph():
    mat = getMat()
    # Create Nodes
    g = nx.DiGraph()
    print(mat)
    for i in range(len(mat)):
        g.add_node(i)

    #Create Edges

    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j] != -1:
                g.add_edge(i, j, weight=mat[i][j])
    return g

# g = getGraph()
# pos = nx.spring_layout(g)
# weights = nx.get_edge_attributes(g, 'weight')

# #Setup for Graph Click
# x, y, nodes = [], [], []
# for key in pos:
#     d = pos[key]
#     nodes.append(key)
#     x.append(d[0])
#     y.append(d[1])

# nx.draw_networkx_edge_labels(g, pos, edge_labels=weights)
# nx.draw(g, pos,with_labels = True)

# ce = clickEvent(x, y, nodes)
# connect('button_press_event', ce)
