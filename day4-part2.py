file_input = open("input-day4.txt",'r')
pairs = [l.strip().split(',') for l in file_input.readlines()]

resp = 0

for pair1, pair2 in pairs:
    pair1min, pair1max = tuple(map(int, pair1.split('-')))
    pair2min, pair2max = tuple(map(int, pair2.split('-')))
    if max(pair1min, pair2min) <= min(pair1max, pair2max):
        resp += 1

print(resp)
