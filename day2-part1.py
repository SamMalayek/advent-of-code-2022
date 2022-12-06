file_input = open("input-day2.txt",'r')
rounds = [l.strip().split() for l in file_input.readlines()]

scoreMap = {
    'A': 1, # rock
    'B': 2, # paper
    'C': 3, # scissors
    'X': 1, # lose
    'Y': 2, # draw
    'Z': 3, # win
}

scoreMe = 0

for him, me in rounds:
    scoreMe += scoreMap[me]
    if scoreMap[him] == scoreMap[me]:
        scoreMe += 3
    else:
        if him == 'A' and me == 'Y':
            scoreMe += 6
        elif him == 'A' and me == 'Z':
            continue
        elif him == 'B' and me == 'X':
            continue
        elif him == 'B' and me == 'Z':
            scoreMe += 6
        elif him == 'C' and me == 'X':
            scoreMe += 6
        elif him == 'C' and me == 'Y':
            continue

print(scoreMe)