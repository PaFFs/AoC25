with open('input3.txt') as file:
    lines = file.readlines()

largestNums = 0

for line in lines:
    line = line.rstrip()
    largestNum = 0
    for num in line:
        for num2 in line[line.index(num)+1:]:
            if int(num+num2) > largestNum:
                largestNum = int(num+num2)
    largestNums += largestNum
print("p1: " + str(largestNums))
