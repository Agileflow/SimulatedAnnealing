#!/usr/bin/env python

from place import Place
from solution import Solution
import xml.etree.ElementTree as ET


class XMLReader(Place):

    def __init__(self, src):

        self.src = src
        self.tree = ET.parse(str(src))
        self.root = self.tree.getroot()
        self.places =  []

        self.readall()

    def readall(self):
        p = None
        for place in self.root.findall('place'):
            p = Place(place.get('name'),
                     place.find('latitude').text,
                     place.find('longitude').text,
                     place.find('location').text,
                      {'name' : place.find('neighbor').get('name'), 'direction' : place.find('neighbor').get('direction')})
            self.places.append(p)

    def getData(self):
        return self.places

    def output(self, solutions, name):
        i = 0
        start = solutions[-1].places[0]

        self.root.set('best-distance', str('{:.3f}'.format(solutions[-1].fitness())))
        self.root.set('default-distance', str('{:.3f}'.format(solutions[0].fitness())))
        self.root.set('name', str(name))

        for place in self.root.findall('place'):
            place.attrib['name'] = solutions[-1].places[i].name
            place[0].text = str(solutions[-1].places[i].latitude)
            place[1].text = str(solutions[-1].places[i].longitude)
            place[2].text = str(solutions[-1].places[i].location)

            if i == (len(solutions[-1].places) - 1):
                place[3].attrib['name'] = start.name
                place[3].attrib['direction'] = start.location
            else:
                place[3].attrib['name'] = solutions[-1].places[i + 1].name
                place[3].attrib['direction']  = solutions[-1].places[i + 1].location

            i += 1
        # write best solution to file
        self.tree.write('repo/output.xml')


