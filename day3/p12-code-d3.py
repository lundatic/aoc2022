#/usr/bin/python3

with open('p12-in-d3.txt') as fhandle:
    lines = [line.rstrip() for line in fhandle]

# P1
sum = 0
for line in lines:
    middle = len(line)//2
    firstpart = line[:middle]
    lastpart = line[middle:]
    common = list(set(firstpart).intersection(set(lastpart))) # Finds common characters in two strings
    if ord(common[0]) < 96:
        prio = ord(common[0]) - 38
    else:
        prio = ord(common[0]) - 96
    sum += prio

print("Solution P1: " + str(sum))

#P2
sum2 = 0
for i in range(0, len(lines), 3): # step 3
    common = list(set(lines[i]).intersection(set(lines[(i+1)]),set(lines[(i+2)])))
    if ord(common[0]) < 96:
        prio = ord(common[0]) - 38
    else:
        prio = ord(common[0]) - 96
    sum2 += prio

print("Solution P2: " + str(sum2))
