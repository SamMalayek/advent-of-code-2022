file_input = open("input-day5.txt",'r')
moves = [l.strip().split() for l in file_input.readlines()]

stacks = [
    ['B','L','D','T','W','C','F','M'],
    ['N','B','L'],
    ['J','C','H','T','L','V'],
    ['S','P','J','W'],
    ['Z','S','C','F','T','L','R'],
    ['W','D','G','B','H','N','Z'],
    ['F','M','S','P','V','G','C','N'],
    ['W','Q','R','J','F','V','C','Z'],
    ['R','P','M','L','H'],
]

for move in moves:
    numStacksToMove = int(move[1])
    fromStackIdx = int(move[3])-1
    toStackIdx = int(move[5])-1
    stacks[toStackIdx].extend(stacks[fromStackIdx][-numStacksToMove:])
    stacks[fromStackIdx] = stacks[fromStackIdx][:len(stacks[fromStackIdx])-numStacksToMove]

print(stacks[0][-1]+stacks[1][-1]+stacks[2][-1]+stacks[3][-1]+stacks[4][-1]+stacks[5][-1]+stacks[6][-1]+stacks[7][-1]+stacks[8][-1])
