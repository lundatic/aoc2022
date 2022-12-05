#/usr/bin/python3

#fhandle = open('p1-ex-in-d1.txt','r')
#lines = fhandle.readlines()
with open('p1-in-d1.txt') as fhandle:
    lines = [line.rstrip() for line in fhandle]

elfcals = []
sum = 0
for line in lines:
    if line == "":
        elfcals.append(sum)
        sum = 0
    else:
        sum += int(line)

max1 = max(elfcals)
elfcals.remove(max1)
max2 = max(elfcals)
elfcals.remove(max2)
max3 = max(elfcals)
top3 = max1+max2+max3

print('Max elf (part 1): ' + str(max1))
print('Sum of top 3 elves (part 2): ' + str(top3))