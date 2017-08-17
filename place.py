#!/usr/bin/env python

class Place:
    'This encapsulate a city which has the following attributes;'
    ' name ---> name of the city'
    ' latitude ---> latitude coordinate scheme to locate the point on north and south pole on geographic positioning'
    ' longitude ---> longitude coordinate scheme to locate the city with ref to Greenwich meridian on geographic positioning'
    
    def __init__(self, name, lat, lng, loc = None, nn = {}):
        self.latitude = float(lat)
        self.longitude = float(lng)
        self.name = str(name)
        self.location = str(loc)
        self.neighbor = nn