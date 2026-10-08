import pyqtgraph as pg

class Graph():
    def __init__(self, window):
        window.plot_graph = pg.PlotWidget()
        window.setCentralWidget(window.plot_graph)
        window.plot_graph.setBackground("w")
        minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 30]
        window.plot_graph.plot(minutes, temperature)