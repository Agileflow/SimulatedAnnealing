#!/usr/bin/env python

from XMLReader import XMLReader
from solution import Solution
from helper import *
from constants import *
#from visualize import PlotGraph

def simAnneal(src, name):
    
    xml = XMLReader(src) # parses .xml source file refer to ./tsp.xml
    solutions = list()
    # creates a default solution from the source file    
    current_solution = Solution(xml.getData())
    solutions.append(current_solution)
    # Start temperature 
    current_temperature = START_TEMPERATURE
    
    while current_temperature > 1:

        # copies the current solution
        temp_solution = current_solution.copy()
        
        # Monte Carlo Iterations for NUM_ITERATIONS steps
        # can be found in constants.py
        for i in range(0, NUM_ITERATIONS):

            # perturb the tour refer to helper.py            
            randomize_solution(temp_solution.places)
            
            # For accept_solution refer to helper.py
            current_solution = accept_solution(current_solution,
                                               temp_solution,
                                               current_temperature)
            solutions.append(current_solution)
        # reduces the temperature with an Alpha value in constants.py
        current_temperature = reduce_temperature(current_temperature)

    # output the best solution found to repo
    xml.output(solutions, name)

    # returns best solution found
    return solutions


def showSolution(solution):
    for place in solution.places:
        print('Town: ', place.name)
        print('\tLat: ', place.latitude)
        print('\tLon: ', place.longitude)
        #print '\tLocation: ', place.location
        #print '\tNearest Neighbor: ', place.neighbor['name'],' + Direction: ', place.neighbor['direction'], '\n'

    print('Best distance: ', solution.distance())
    #print('Overall improvement using greedy heuristics: ', round(((init - solution.distance()) / init), 4))


