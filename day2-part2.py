file_input = open("input-day2.txt",'r')
rounds = [l.strip().split() for l in file_input.readlines()]

scoreMap = {
    'A': 1, # rock
    'B': 2, # paper
    'C': 3, # scissors
    'X': 0, # lose
    'Y': 3, # draw
    'Z': 6, # win
}

scoreMe = 0

for him, me in rounds:
    scoreMe += scoreMap[me]
    if me == 'X':
        if him == 'A':
            scoreMe += 3
        elif him == 'B':
            scoreMe += 1
        else:
            scoreMe += 2
    elif me == 'Y':
        scoreMe += scoreMap[him]
    else:
        if him == 'A':
            scoreMe += 2
        elif him == 'B':
            scoreMe += 3
        else:
            scoreMe += 1

print(scoreMe)