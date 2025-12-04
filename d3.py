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

#p2

def lineMath(line):
    # make a new list of lists, populate with shorter lines
    newLines = []
    # remove 1 char from line for each char in line
    for i in range(len(line)):
        newLine = line[:i] + line[i+1:]
        newLines.append(newLine)
    # convert each row in newLine to int for comparison, then sort and grab highest value
    newLinesInt = []
    for newLineInt in newLines:
        newLineInt = int(newLineInt)
        newLinesInt.append(newLineInt)
    newLinesInt.sort()
    largestNum = newLinesInt[-1]
    newLine = str(newLinesInt[-1])
    return newLine, largestNum

largestNums = 0
for line in lines:
    line = line.rstrip()
    while len(line) > 12:
        newLine, largestNum = lineMath(line)
        line = newLine
    largestNums += int(largestNum)
print(largestNums)
    
