with open('input9.txt') as file:
    lines = file.readlines()

class Corner:
    def __init__(self, xPos, yPos):
        self.xPos = int(xPos)
        self.yPos = int(yPos)
    
    def rectangle(self, otherCorner):
        xDiff = abs(self.xPos - otherCorner.xPos) + 1
        yDiff = abs(self.yPos - otherCorner.yPos) + 1
        return xDiff * yDiff

corners = []
for line in lines:
    line = line.rstrip()
    line = line.split(",")
    corners.append(Corner(line[0], line[1]))

bigSquare = 0
for corner in corners:
    for corner2 in corners:
        if corner == corner2:
            continue
        else:
            if corner.rectangle(corner2) > bigSquare:
                bigSquare = corner.rectangle(corner2)
print(bigSquare)