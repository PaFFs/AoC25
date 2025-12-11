with open('input10.txt') as file:
    lines = file.readlines()

#created the dict up here so the class can access it
objDevices = {}

class Device:
    def __init__(self, name, outputs):
        self.outputs = []
        self.name = name
        self.Basecount = 0
        for output in outputs:
            if output == "out":
                self.Basecount += 1
            else:
                self.outputs.append(output)
    
    def countChildren(self):
        if len(self.outputs) == 0:
            return self.Basecount
        else:
            childrenCount = 0
            for output in self.outputs:
                # change below to access dict!
                outputDevice = objDevices[output]
                childrenCount += outputDevice.countChildren()
            return childrenCount + self.Basecount         
    
devices = []
for line in lines:
    line = line.rstrip()
    line = line.split(":")
    devices.append([line[0],line[1].split()])

for device in devices:
    objDevices[device[0]] = Device(device[0],device[1])

print("p1: " + str(objDevices["you"].countChildren()))
