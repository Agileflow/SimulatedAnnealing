#!/usr/bin/env python

import matplotlib.pyplot as plt
from time import sleep


class Visualize:
    def __init__(self, solutions, title, xlabel, ylabel, grid=False, save=None):

        self.fig = plt.figure()
        self.sub = plt.subplot(111)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        self.save = save
        x, y = solutions[0].dataset()
        self.ly = plt.plot(x, y, 'co')
        plt.grid(grid)
        self.link(x,y)
        plt.xlim(0, max(x) * 1.1)
        plt.ylim(0, max(y) * 1.1)

        plt.show(block=False)

        for solution in solutions:
            self.plot(solution)

    def plot(self,solution):
        plt.cla()
        plt.grid(True)
        x, y = solution.dataset()
        self.ly[0].set_xdata(x)
        self.ly[0].set_ydata(y)
        self.link(x, y)
        self.fig.canvas.draw()
        sleep(0.5)

    def link(self,x,y):
        a_scale = float(max(x)) / float(100000)
        # Draw the primary path for the TSP problem
        plt.arrow(x[-1], y[-1], (x[0] - x[-1]), (y[0] - y[-1]), head_width=a_scale,
                  color='b', length_includes_head=True)
        for i in range(0, len(x) - 1):
            plt.arrow(x[i], y[i], (x[i + 1] - x[i]), (y[i + 1] - y[i]), head_width=a_scale,
                      color='g', length_includes_head=True)