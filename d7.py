with open('input7.txt') as file:
    lines = file.readlines()

rows = []
for line in lines:
    line = line.rstrip()
    line = list(line)
    rows.append(line)

splits = 0
startXcor = ''.join(rows[0]).index("S")
rows[1][startXcor] = "|"
yCor = 2
for row in rows[2:]:
    for xCor in range(len(row)):
        if rows[yCor-1][xCor] == "|":
            # Do stuff
            if rows[yCor][xCor] == "^":
                #split stuff
                #Only change cells if dot! if arrow or line dont touch
                if rows[yCor][xCor-1] == ".":
                    rows[yCor][xCor-1] = "|"
                if rows[yCor][xCor+1] == ".":
                    rows[yCor][xCor+1] = "|"
                splits += 1
                
            else:
                rows[yCor][xCor] = "|"
    yCor += 1

print(splits)