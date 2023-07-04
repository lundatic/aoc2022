#/usr/bin/python3

with open('p12-in-d6.txt') as fhandle:
    lines = [line.rstrip('\n') for line in fhandle]

for line in lines:
    start_signal_selection = []
    start_signal_found = False
    start_message_selection = []
    start_message_found = False

    for i in range(len(line)):
        start_signal_selection.append(line[i])
        start_message_selection.append(line[i])
        if len(start_signal_selection) > 4 and not start_signal_found:
            start_signal_selection.pop(0)
        if len(start_message_selection) > 14 and not start_message_found:
            start_message_selection.pop(0)
        if len(start_signal_selection) > 3 and not start_signal_found:
            unique_signal = list(set(start_signal_selection))
            if len(start_signal_selection) == len(unique_signal):
                print("Solution P1: " + str(i+1))
                start_signal_found = True
        if len(start_message_selection) > 13 and not start_message_found:
            unique_message = list(set(start_message_selection))
            if len(start_message_selection) == len(unique_message):
                print("Solution P2: " + str(i+1))
                start_message_found = True
        if start_signal_found and start_message_found:
            break

