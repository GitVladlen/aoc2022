import utils

lines = utils.get_file_lines("../inputs/input_day6.txt")
#lines = utils.get_file_lines("../inputs/test_1_day6.txt")

line = lines[0]

def is_marker(chars):
    for ch in chars:
        if chars.count(ch) > 1:
            return False
    return True

def part_one(line):
    for i in range(len(line) - 4 + 1):
        if is_marker(line[i:i+4]):
            break
    return i + 4
    
def part_two(line):
    for i in range(len(line) - 14 + 1):
        if is_marker(line[i:i+14]):
            break
    return i + 14
    
result_part_one = part_one(line)
result_part_two = part_two(line)

print("Part 1 result:", result_part_one)
print("Part 2 result:", result_part_two)