import utils
import copy

lines = utils.get_file_lines("../inputs/input_day5.txt")
#lines = utils.get_file_lines("../inputs/test_1_day5.txt")

stacks_lines = []
moves_lines = []

is_stack = True
for line in lines:
    if line == '':
        is_stack = False
        continue
    if is_stack:
        stacks_lines.append(line)
    else:
        moves_lines.append(line)

def parse_stacks(lines):
    lines.reverse()
    rotated = list(zip(*lines))[::-1]
    
    stacks = {}
    for line in rotated:
        if line[0] == ' ':
            continue
        key = line[0]
        stack = []
        for ch in line[1:]:
            if ch != ' ':
             stack.append(ch)
        stacks[key] = stack
        
    return stacks
    
def parse_moves(lines):
    moves = []
    for line in lines:
        nodes = line.split(' ')
        moves.append((int(nodes[1]), nodes[3], nodes[5]))
    return moves
    
g_stacks_1 = parse_stacks(stacks_lines)
g_stacks_2 = copy.deepcopy(g_stacks_1)
g_moves = parse_moves(moves_lines)
    
def part_one(stacks, moves):
    # print("Part 1:")
    # print("Stacks:")
    # print(stacks)
    # print("Moves:")
    # print(moves)
    
    for move in moves:
        count, from_stack_id, to_stack_id = move
        for i in range(count):
            stacks[to_stack_id].append(stacks[from_stack_id].pop())
            
    answer = ""
    
    for i in range(len(stacks)):
        answer += stacks["{}".format(i+1)][-1]
    
    return answer
    
def part_two(stacks, moves):  
    # print("Part 2:")
    # print("Stacks:")
    # print(stacks)
    # print("Moves:")
    # print(moves) 
    for move in moves:
        count, from_stack_id, to_stack_id = move
        buf = []
        for i in range(count):
            buf.append(stacks[from_stack_id].pop())
        buf.reverse()
        for ch in buf:
            stacks[to_stack_id].append(ch)
            
    answer = ""
    
    for i in range(len(stacks)):
        answer += stacks["{}".format(i+1)][-1]
    
    return answer
    
result_part_one = part_one(g_stacks_1, g_moves)
result_part_two = part_two(g_stacks_2, g_moves)

print("Part 1 result:", result_part_one)
print("Part 2 result:", result_part_two)