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
        self.drawnSourceAnnotation = None
        self.drawnDestinationAnnotation = None
        self.source = None
        self.destination = None
        self.mode = 'Source'

    def __call__(self, event):
        print(self.mode)
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
                    self.drawAnnote(event.inaxes, x, y,node)
                    return node

    def drawAnnote(self, axis, x, y,node):
        if (self.mode == 'Source'):
            if self.drawnSourceAnnotation is not None:
                (t,m) = self.drawnSourceAnnotation
                m = m[0]
                t.set_visible(False)
                m.set_visible(False)
            t = axis.text(x, y, 'Source')
            m = axis.plot([x], [y], marker = 'v', color='red')
            self.drawnSourceAnnotation = (t,m)
            self.axis.figure.canvas.draw()
            self.source = node
        else:
            if self.drawnDestinationAnnotation is not None:
                (t,m) = self.drawnDestinationAnnotation
                m = m[0]
                t.remove()
                m.remove()
            t = axis.text(x, y, 'Destination')
            m = axis.plot([x], [y], marker = '^', color='blue')
            self.drawnDestinationAnnotation = (t,m)
            self.axis.figure.canvas.draw()
            self.destination = node
        #     if (x, y) in self.drawnSourceAnnotations:
        #         markers = self.drawnSourceAnnotations[(x, y)]
        #         for m in markers:
        #             m.set_visible(not m.get_visible())
        #         self.axis.figure.canvas.draw()
        #     else:
        #         t = axis.text(x, y, "%s" % ('Source') )
        #         m = axis.scatter([x], [y], marker='v', c='r', zorder=100)
        #         self.drawnSourceAnnotations[(x, y)] = (t, m)
        #         self.axis.figure.canvas.draw()
        #     for tuples in self.drawnSourceAnnotations.keys():
        #         if tuples[0] != x and tuples[1] != y:
        #             t, m = self.drawnSourceAnnotations[tuples]
        #             t.set_visible(False)
        #             m.set_visible(False)
        # else:
        #     if (x, y) in self.drawnDestinationAnnotations:
        #         markers = self.drawnDestinationAnnotations[(x, y)]
        #         for m in markers:
        #             m.set_visible(not m.get_visible())
        #         self.axis.figure.canvas.draw()
        #     else:
        #         t = axis.text(x, y, "%s" % ('Destination') )
        #         m = axis.scatter([x], [y], marker='^', c='b', zorder=100)
        #         self.drawnDestinationAnnotations[(x, y)] = (t, m)
        #         self.axis.figure.canvas.draw()
        #     for tuples in self.drawnDestinationAnnotations.keys():
        #         if tuples[0] != x and tuples[1] != y:
        #             t, m = self.drawnDestinationAnnotations[tuples]
        #             t.set_visible(False)
        #             m.set_visible(False)

    
    def setMode(self,mode):
        self.mode = mode

    def getMode(self):
        return self.mode

    def getSource(self):
        return self.source
    
    def getDestination(self):
        return self.destination

def getMat(filepath):
    mat = []
    # Read input
    with open(filepath, 'r') as f:
        lines = f.readlines()
        for i in range (len(lines)):
            mat += [list(map(int, lines[i].split()))]
    return mat

def getGraph(mat):
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
