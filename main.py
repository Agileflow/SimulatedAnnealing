#!/usr/bin/env python

from simAnneal import *
from visualize import Visualize
import threading

if __name__ == '__main__':

    src = 'repo/tsp.xml'
    
    configurations = simAnneal(src, 'Lagos')
    showSolution(configurations[-1])

    plt_thread = threading.Thread(target=Visualize, args= (configurations,"Travelling Salesman Problem Solution Using Simulated Annealing",'Latitude','Longitude',True))
    plt_thread.daemon = False
    plt_thread.start()
