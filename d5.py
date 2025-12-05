with open('input5.txt') as file:
    lines = file.readlines()

ranges = []

def checkIfInRange(ingredient):
    for range in ranges:
        range = range.split("-")
        if int(range[0]) <= int(ingredient) <= int(range[1]):
            return True
    return False

ingredients = []
mode = True
for line in lines:
    if line.rstrip() == "":
        mode = False
        continue
    if mode:
        ranges.append(line.rstrip())
    else:
        ingredients.append(line.rstrip())

freshIngredients = 0
for ingredient in ingredients:
    freshIngredients += checkIfInRange(ingredient)
print("p1: " + str(freshIngredients))



# Loop through all ranges and try to find an overlap
for frange in ranges:
    frangeFlag = True
    frange = frange.split("-")
    frange = frange.sort()
    for yrange in ranges:
        if frange[0]+"-"+frange[1] == yrange:
            continue # if the pair is the same range, ignore it
        yrange = yrange.split("-")
        yrange = yrange.sort()
        xmin, xmax = int(frange[0]),int(frange[1])
        ymin, ymax = int(yrange[0]),int(yrange[1])
        if xmin <= ymax:
            #overlap x higher
            newRange = str(ymin)+"-"+str(xmax)
            ranges.append(newRange)
            ranges.remove(frange[0]+"-"+frange[1])
            ranges.remove(yrange[0]+"-"+yrange[1])
            frangeFlag = False
        elif ymin <= xmax:
            #overlap y higher
            newRange = str(xmin)+"-"+str(ymax)
            ranges.append(newRange)
            ranges.remove(frange[0]+"-"+frange[1])
            ranges.remove(yrange[0]+"-"+yrange[1])
            frangeFlag = False
        else:
            continue # if no overlap, check next pair
        if frangeFlag == False:
            break

sums = 0
for frange in ranges:
    frange = frange.split("-")
    frangeVal = int(frange[1]) - int(frange[0])
    sums += frangeVal
print("p2: " + str(sums))