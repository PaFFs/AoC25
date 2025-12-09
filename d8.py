import numpy as np
from operator import itemgetter

with open('input8.txt') as file:
    lines = file.readlines()

def distance(point1, point2):
    x1,y1,z1 = point1[0], point1[1], point1[2]
    x2,y2,z2 = point2[0], point2[1], point2[2]
    xDiff = x1-x2
    yDiff = y1-y2
    zDiff = z1-z2
    sumDiff = np.pow(xDiff,2) + np.pow(yDiff,2) + np.pow(zDiff,2)
    dist = np.sqrt(sumDiff)
    return dist

class Box:
    def __init__(self, point, dist, point2):
        self.point = point
        self.dist = dist
        self.point2 = point2

class Circuit:
    def __init__(self, point1, point2):
        self.points = []
        self.points.append(point1)
        self.points.append(point2)
    
    def addPoint(self, point3):
        self.points.append(point3)

    def joinCircuits(self, circuit1):
        for point4 in circuit1:
            if point4 in self.points:
                continue
            else:
                self.points.append(point4)
    def countBoxes(self):
        return len(self.points)


points = []
for line in lines:
    line = line.rstrip()
    line = line.split(",")
    point = []
    point.append(int(line[0]))
    point.append(int(line[1]))
    point.append(int(line[2]))
    points.append(point)

# make a list of the shortest distances from each point
pointsList = []
for point in points:
    pointList = []
    for point2 in points:
        if point == point2:
            continue
        else:
            pointList.append([point2, distance(point,point2)])
    pointList = sorted(pointList,key=itemgetter(1))
    breaker = Box(point,pointList[0][1],pointList[0][0])
    pointsList.append(breaker)
pointsList = sorted(pointsList, key=lambda x: x.dist)
pointsList = pointsList[::2]

circuits = []
circuits.append(Circuit(pointsList[0].point,pointsList[0].point2))
for point in pointsList[1:]:
    point1 = point.point
    point2 = point.point2
    for circuit in circuits:
        point1C = False
        point2C = False
        # check if either point is in a circuit
        if point1 in circuit.points:
            point1C = circuit
            break
        if point2 in circuit.points:
            point2C = circuit
            break
        
    if point1C and not point2C:
        # point 1 in circuit
        point1C.addPoint(point2)
        continue
    elif point2C and not point1C:
        # point 2 in circuit
        point2C.addPoint(point1)
        continue
    elif point1C and point2C:
        # both points in circuit
        if point1C == point2C:
            # both in same circuit
            continue
        else:
            # separate circuits
            point1C.joinCircuits(point2C)
            circuits.remove(point2C)
            continue
    else:
        # if neither box in any circuit, form new circuit with both
        circuits.append(Circuit(point1,point2))
        continue

print(len(circuits))
count = []
for circuit in circuits:
    count.append(circuit.countBoxes())
count.sort(reverse=True)
print(count)