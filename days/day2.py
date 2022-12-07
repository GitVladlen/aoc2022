lines = ""
with open("C:\\MySpace\\AOC2022\\inputs\\input_day2.txt") as file:
    for line in file:
        lines += line

nodes = lines.split('\n')

# A - Rock, B - Paper, C - Scissors
# X - Rock, Y - Paper, Z - Scissors
p1_shapes = {'A': 1, 'B': 2, 'C': 3}
p2_shapes = {'X': 1, 'Y': 2, 'Z': 3}

p1_wins = [('A', 'Z'), ('B', 'X'), ('C', 'Y')]

p1_wins_dict = {'A': 'Z', 'B': 'X', 'C': 'Y'}
p2_wins_dict = {'A': 'Y', 'B': 'Z', 'C': 'X'}
p2_analog = {'A': 'X', 'B': 'Y', 'C': 'Z'}
def calc_score_1(p1, p2):
    if p1_shapes[p1] == p2_shapes[p2]:
        # draw
        return p2_shapes[p2] + 3
    if (p1, p2) in p1_wins:
        # p1 win
        return p2_shapes[p2]
    else:
        # p2 win
        return p2_shapes[p2] + 6

# X - lose, Y - draw, Z - win
action_score = {'X': 0, 'Y': 3, 'Z': 6}
def calc_score_2(p1, action):
    actions = {'X': p1_wins_dict[p1],
               'Y': p2_analog[p1],
               'Z': p2_wins_dict[p1]}
    return calc_score_1(p1, actions[action])

total_score_1 = 0
total_score_2 = 0
for node in nodes:
    player1, player2 = node.split(' ')
    total_score_1 += calc_score_1(player1, player2)
    total_score_2 += calc_score_2(player1, player2)

print("Part1: Total score:", total_score_1)
print("Part2: Total score:", total_score_2)

