from collections import defaultdict, deque
file_input = open("input-day6.txt",'r')
string = [l.strip() for l in file_input.readlines()][0]

d = deque([])
dd = defaultdict(int)

for i in range(len(string)):
    if not foundSignal:
        if len(d) >= 4:
            popped = d.popleft()
            dd[popped] -= 1
            if dd[popped] <= 0:
                del dd[popped]
        d.append(string[i])
        dd[string[i]] += 1
        if len(dd) == 4:
        print(i+1)
        break


