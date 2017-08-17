#!/usr/bin/env python

from simAnneal import *
from visualize import Visualize, Plot

if __name__ == '__main__':

    src = 'repo/tsp.xml'
    
    configurations = simAnneal(src, 'Lagos')
    showSolution(configurations[-1])
    init = configurations[0].fitness()
    print('Overall improvement using greedy heuristics: ', round(((init - configurations[-1].fitness()) / init), 4))

    fitness = [solution.fitness() for solution in configurations]
    temps = [solution.temperature() for solution in configurations]
    iterations = [i for i in range(len(fitness))]

    #Visualize(configurations,"Travelling Salesman Problem Solution Using Simulated Annealing",'Latitude','Longitude',True)
    Plot('Temperature to Iteration',iterations,temps,'Temperature','Fitness')
    Plot('Fitness to Iteration',iterations,fitness,'Iterations','Fitness')
