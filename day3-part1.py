file_input = open("input-day3.txt",'r')
sacks = [l.strip() for l in file_input.readlines()]

resp = 0

for sack in sacks:
    n = len(sack)
    a = set(sack[:n//2])
    b = set(sack[n//2:])
    c = next(iter(a.intersection(b)))
    if c.islower():
        resp += ord(c) - 96
    else:
        resp += ord(c) - 38

print(resp)