with open('input2.txt') as file:
    lines = file.readlines()

invalidSum = 0
productIDs = ""

for line in lines:
    productIDs += line.rstrip()

productIDs = productIDs.split(",")

for product in productIDs:
    start, stop = product.split("-")
    for id in range(int(start), int(stop)+1):
        if len(str(id)) % 2 == 0:
            length = int(len(str(id)) / 2)
            a = str(id)[:length]
            b = str(id)[length:]
            if a == b:
                invalidSum += id
print("p1: " + str(invalidSum))

invalidSum = 0
productIDs = ""

for line in lines:
    productIDs += line.rstrip()

productIDs = productIDs.split(",")

for product in productIDs:
    start, stop = product.split("-")
    for id in range(int(start), int(stop)+1):
        passed = False
        idNums = []
        for i in range(1,int(len(str(id)))//2 + 1):
            idNums.append(str(id)[:i])
        for idNum in idNums:
            if len(str(idNum)) * str(id).count(idNum) == len(str(id)):
                invalidSum += id
                break

print("p2: " + str(invalidSum))