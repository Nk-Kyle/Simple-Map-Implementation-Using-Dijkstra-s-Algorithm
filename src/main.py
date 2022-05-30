import tkinter
import networkx as nx
from graph import *
from Djikstra import *
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np

def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)

def _quit():
    root.quit()     # stops mainloop
    root.destroy()

def test():
    ce.setMode('Test')

def calcDist():
    if (ce.getSource() is None or ce.getDestination() is None):
        tkinter.messagebox.showinfo('Error', 'Source and Destination must be selected')
    else:
        resultvar.set(djikstra(getMat(), ce.getSource(), ce.getDestination()))


mode = 'Source'
root = tkinter.Tk()
root.wm_title("Embedding in Tk")
g = getGraph()
pos = nx.spring_layout(g)
weights = nx.get_edge_attributes(g, 'weight')

#Setup for Graph Click
x, y, nodes = [], [], []
for key in pos:
    d = pos[key]
    nodes.append(key)
    x.append(d[0])
    y.append(d[1])

nx.draw_networkx_edge_labels(g, pos, edge_labels=weights)
nx.draw(g, pos,with_labels = True, node_size=500)


ce = clickEvent(x, y, nodes)
connect('button_press_event', ce)

canvas = FigureCanvasTkAgg(plt.gcf(), master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


canvas.mpl_connect("key_press_event", on_key_press)

sourceButton = tkinter.Button(master=root, text="Source", command=lambda: ce.setMode('Source'))
sourceButton.pack(side=tkinter.LEFT)

destinationButton = tkinter.Button(master=root, text="Destination", command=lambda: ce.setMode('Destination'))
destinationButton.pack(side=tkinter.LEFT)

calculateDistanceButton = tkinter.Button(master=root, text="Calculate Distance", command = calcDist)
calculateDistanceButton.pack(side=tkinter.LEFT)

resultvar = tkinter.StringVar()
resultvar.set('')
resultLable = tkinter.Label(master=root, textvariable= resultvar)
resultLable.pack(side=tkinter.BOTTOM, pady=10)

exitButton = tkinter.Button(master=root, text="Quit", command=_quit)
exitButton.pack(side=tkinter.BOTTOM)

tkinter.mainloop()