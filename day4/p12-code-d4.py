#/usr/bin/python3

with open('p12-in-d4.txt') as fhandle:
    lines = [line.rstrip() for line in fhandle]

# P1
full_overlap_list = []
overlap_list = []

for line in lines:
    first, second = line.split(',')
    firststart, firstlast = first.split('-')
    secondstart, secondlast = second.split('-')

    if int(firststart) <= int(secondstart) and int(firstlast) >= int(secondlast):
        full_overlap_list.append(line)
    elif int(firststart) >= int(secondstart) and int(firstlast) <= int(secondlast):
        full_overlap_list.append(line)

    if set(range(int(firststart),int(firstlast)+1)).intersection(set(range(int(secondstart),int(secondlast)+1))) != set():
        overlap_list.append(line)


print("Solution P1: " + str(len(full_overlap_list)))
print("Solution P2: " + str(len(overlap_list)))