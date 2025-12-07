with open('input6.txt') as file:
    lines = file.readlines()

rows = []
for line in lines:
    line = line.rstrip()
    line = line.split(" ")
    while '' in line:
        line.remove('')
    rows.append(line)

problems = []
for i in range(len(line)):
    problem = []
    for row in rows:
        problem.append(row[i])
    problems.append(problem)

results = 0
for problem in problems:
    if problem[4] == "+":
        results += int(problem[0]) + int(problem[1]) + int(problem[2]) + int(problem[3])
    elif problem[4] == "*":
        results += int(problem[0]) * int(problem[1]) * int(problem[2]) * int(problem[3])
print("p1: " + str(results))

# not doing p2, above solution has no chance to be worked on