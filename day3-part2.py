file_input = open("input-day3.txt",'r')
sacks = [l.strip() for l in file_input.readlines()]

resp = 0

for i in range(0, len(sacks), 3):
    sack1 = set(sacks[i])
    sack2 = set(sacks[i+1])
    sack3 = set(sacks[i+2])

    c = next(iter(sack1.intersection(sack2).intersection(sack3)))
    if c.islower():
        resp += ord(c) - 96
    else:
        resp += ord(c) - 38

print(resp)