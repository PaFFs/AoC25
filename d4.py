with open('input4.txt') as file:
    lines = file.readlines()

grid = []
width = len(lines[-1])
emptyRow = ""
for i in range(width+2):
    emptyRow += "."
grid.append(emptyRow)

for line in lines:
    # add lines to grid
    line = line.rstrip()
    line = "." + line + "."
    grid.append(line)
grid.append(emptyRow)

# do the task
movablePaper = 0
for yPos in range(len(grid)):
    for xPos in range(len(grid[0])):
        cell = grid[yPos][xPos]
        if cell == ".":
            next
        else:
            adjacents = [
                grid[yPos-1][xPos-1],
                grid[yPos-1][xPos],
                grid[yPos-1][xPos+1],
                grid[yPos][xPos-1],
                grid[yPos][xPos+1],
                grid[yPos+1][xPos-1],
                grid[yPos+1][xPos],
                grid[yPos+1][xPos+1]
            ]
            if adjacents.count("@") > 3:
                next
            else:
                movablePaper += 1
print("p1: " + str(movablePaper))

# do the task
movablePaper = 0
movedPaper = 1
while movedPaper != 0:
    movedPaper = 0
    for yPos in range(len(grid)):
        for xPos in range(len(grid[0])):
            cell = grid[yPos][xPos]
            if cell == ".":
                next
            else:
                adjacents = [
                    grid[yPos-1][xPos-1],
                    grid[yPos-1][xPos],
                    grid[yPos-1][xPos+1],
                    grid[yPos][xPos-1],
                    grid[yPos][xPos+1],
                    grid[yPos+1][xPos-1],
                    grid[yPos+1][xPos],
                    grid[yPos+1][xPos+1]
                ]
                if adjacents.count("@") > 3:
                    next
                else:
                    movablePaper += 1
                    movedPaper += 1
                    # build a new row, with the paper removed, and put it in the grid
                    newRow = grid[yPos][:xPos] + "." + grid[yPos][xPos+1:]
                    grid[yPos] = newRow
print("p2: " + str(movablePaper))