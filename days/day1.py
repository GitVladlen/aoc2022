callories = []
data = ""
with open("C:\\MySpace\AOC2022\\inputs\\input_day1.txt") as file:
    for line in file:
        data += line

nodes = data.split('\n');

cur = 0

for node in nodes:
    if node:
        cur += int(node)
    else:
        callories.append(cur)
        cur = 0

callories.append(cur)
print(callories)
callories.sort()
print(callories[-1] + callories [-2] + callories[-3])



