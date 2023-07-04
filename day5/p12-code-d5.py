#/usr/bin/python3

with open('p12-in-d5.txt') as fhandle:
    lines = [line.rstrip('\n') for line in fhandle]

stacks_unformated = []

for line in lines:
    if "[" in line:
        stacks_unformated.append(line)
    else:
        break

indexes = [x.lstrip() for x in lines[len(stacks_unformated)].split("   ")]
stacks = {}
stacks2 = {}

for j in range(len(indexes)):
    stacks[int(indexes[j])] = []
    stacks2[int(indexes[j])] = []

for i in range(len(stacks_unformated)-1,-1,-1):
    for j in range(len(indexes)):
        #print(stacks_unformated[i][(j*4)+1])
        if ord(stacks_unformated[i][(j*4)+1]) > 64 and ord(stacks_unformated[i][(j*4)+1]) < 91:
            stacks[(j+1)].append(stacks_unformated[i][(j*4)+1])
            stacks2[(j+1)].append(stacks_unformated[i][(j*4)+1])

for i in range(len(stacks_unformated)+2,len(lines)):
    command = lines[i]
    commands = command.split(' ')
    nr, fromstack, tostack = int(commands[1]),int(commands[3]),int(commands[5])
    
    for j in range(nr):
        item = stacks[fromstack].pop()
        stacks[tostack].append(item)
    for j in range((len(stacks2[fromstack])-nr),len(stacks2[fromstack])):
         stacks2[tostack].append(stacks2[fromstack][j])
    del stacks2[fromstack][len(stacks2[fromstack])-nr:len(stacks2[fromstack])]

word = ""
word2 = ""

for stack in stacks.values():
    word += stack[-1]

for stack in stacks2.values():
    word2 += stack[-1]

print("Solution P1: " + word)
print("Solution P2: " + word2)




