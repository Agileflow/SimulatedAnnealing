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
    cities = len(configurations[0].places)


    #Visualize(configurations,"Travelling Salesman Problem Solution Using Simulated Annealing",'Latitude','Longitude',True)
    Plot('Temperature to '+ str(len(iterations)) +' iterations of ' + str(cities) + ' cities',iterations,temps,'Iteration','Temperature')
    Plot('Fitness to '+ str(len(iterations)) +' iterations of ' + str(cities) + ' cities',iterations,fitness,'Iteration','Fitness')
    Visualize('Initial tour of ' + str(cities) + ' cities',[place.latitude for place in configurations[0].places],[place.longitude for place in configurations[0].places],'Latitude','Longitude',True)
    Visualize('Optimum tour after '+ str(len(iterations)) +' iterations of ' + str(cities) + ' cities',[place.latitude for place in configurations[-1].places],[place.longitude for place in configurations[-1].places],'Latitude','Longitude', True)
