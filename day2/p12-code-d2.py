#/usr/bin/python3

with open('p1-in-d2.txt') as fhandle:
    lines = [line.rstrip() for line in fhandle]

result_matrix = {
    "X": { # Rock (1)
        "A": 4 , # Rock = Tie (3) + 1
        "B": 1, # Paper = Loss (0) + 1
        "C": 7 # Scissors = Win (6) + 1
    },
    "Y": { # Paper
        "A": 8, # Rock = Winn (6) + 2
        "B": 5, # Paper = Tie (3) + 2
        "C": 2 # Scissors = Loss (0) + 2
    },
    "Z": { # Scissor
        "A": 3, # Rock = Loss (0) + 3
        "B": 9, # Paper = Win (6) + 3
        "C": 6 # Scissors = Tie (3) + 3
    }
}

translation_matrix = {
    "X": { # Loose / Rock in result_matrix
        "A": "Z" , # Rock = you loose with Scissors
        "B": "X", # Paper = you loose with Rock
        "C": "Y" # Scissors = you loose with Paper
    },
    "Y": { # Draw / Paper in result_matrix
        "A": "X", # Rock = you draw with Rock
        "B": "Y", # Paper = you draw with Paper
        "C": "Z" # Scissors = you draw with Scissor
    },
    "Z": { # Win / Scissor in result matrix
        "A": "Y", # Rock = you win with Paper
        "B": "Z", # Paper = you win with Scissor
        "C": "X" # Scissors = you win Rock
    }
}

sum_p1 = 0
sum_p2 = 0
for line in lines:
    hands = line.split(" ")
    sum_p1 += result_matrix[hands[1]][hands[0]]
    sum_p2 += result_matrix[translation_matrix[hands[1]][hands[0]]][hands[0]]

print("Solution P1: " + str(sum_p1))
print("Solution P2: " + str(sum_p2))