#!/usr/bin/env python

from math import sqrt
from math import exp
from random import randint, random
import constants as cnst

def euclidean_distance(x1,y1,x2,y2):
    return round(sqrt(((x2-x1)**2)+((y2-y1)**2)), 5)

def compute_tour(solution):
    
    solution_size = len(solution) - 1
    tour_dist = 0.0
    
    for i in range(0, solution_size):

        tour_dist += euclidean_distance(solution[i].latitude,
                                        solution[i].longitude,
                                        solution[i+1].latitude,
                                        solution[i+1].longitude)

    tour_dist += euclidean_distance(solution[solution_size].latitude,
                                        solution[solution_size].longitude,
                                        solution[0].latitude,
                                        solution[0].longitude)
    #for debugging
    #print tour_dist
    return round(tour_dist,5)

def randomize_solution(solution):

    solution_size = len(solution)-1
    while True:
        rand1 = randint(0, solution_size)
        rand2 = randint(0, solution_size)
        if rand1 != rand2:
            break
        
    temp = solution[rand1]
    solution[rand1] = solution[rand2]
    solution[rand2] = temp
    

def reduce_temperature(Temperature):
                               return Temperature * cnst.ALPHA    


                                    
def accept_solution(cur_solution, new_solution, Temperature):

    delta = new_solution.distance() - cur_solution.distance()

    # Is new solution better, then take it
    if delta < 0.0  :
        cur_solution = new_solution.copy()
    else:
        p = exp( (-delta / Temperature))
        # Randomly accept worse solution
        if p > random():
            cur_solution = new_solution.copy()
                                    
    return cur_solution


        
