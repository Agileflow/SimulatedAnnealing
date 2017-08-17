#!/usr/bin/env python

from helper import compute_tour

class Solution():
    
    def __init__(self, places = []):
        self.places = places
        self.dist = 0.0
   
    def distance(self):
        self.dist = compute_tour(self.places)
        return self.dist

    def copy(self):
        return Solution(list(self.places))

    def fitness(self):
        return self.dist

    def dataset(self):
        x = list()
        y = list()
        for place in self.places:
            x.append(place.latitude)
            y.append(place.longitude)

        return x, y

