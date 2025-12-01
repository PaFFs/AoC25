with open('input1.txt') as file:
    lines = file.readlines()

def moveDial(start, dir):
    if dir == "R":
        if 0 <= start <= 98:
            return start + 1
        elif start == 99:
            return 0
    if dir == "L":
        if 0 < start <= 99:
            return start - 1
        elif start == 0:
            return 99

dialPos = 50
password1 = 0
password2 = 0
for line in lines:
    if line[0] == "R":
        #do right stuff
        for i in range(int(line[1:])):
            dialPos = moveDial(dialPos,"R")
            if dialPos == 0:
                password2 += 1
    else:
        #do left stuff
        for i in range(int(line[1:])):
            dialPos = moveDial(dialPos,"L")
            if dialPos == 0:
                password2 += 1
    if dialPos == 0:
        password1 += 1
print(password1)
print(password2)

