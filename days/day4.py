import utils

input_file_name = "../inputs/input_day4.txt"
#input_file_name = "../inputs/test_1_day4.txt"

lines = utils.get_file_lines(input_file_name)
#print(lines)


def is_fully_overlap(first, second):
  f_start_s, f_end_s = first
  s_start_s, s_end_s = second
  f_start, f_end = int(f_start_s), int(f_end_s)
  s_start, s_end = int(s_start_s), int(s_end_s)
  
  #print(f_start, f_end, s_start, s_end)
  
  if f_start <= s_start and f_end >= s_end:
    return True
  if s_start <= f_start and s_end >= f_end:
    return True
  return False


def is_overlap_at_all(first, second):
  if is_fully_overlap(first, second):
    return True
  
  f_start_s, f_end_s = first
  s_start_s, s_end_s = second
  f_start, f_end = int(f_start_s), int(f_end_s)
  s_start, s_end = int(s_start_s), int(s_end_s)

  if f_start < s_start and f_end < s_start:
    return False
  elif s_start < f_start and s_end < f_start:
    return False

  return True


def part_one(lines):
  count = 0
  for line in lines:
    parts = line.split(',')
    if is_fully_overlap(parts[0].split('-'), parts[1].split('-')):
      count += 1
      #print(line)
  return count


def part_two(lines):
  count = 0
  for line in lines:
    parts = line.split(',')
    if is_overlap_at_all(parts[0].split('-'), parts[1].split('-')):
      count += 1
      #print(line)
  return count


print("Lines count:", len(lines))
result_part_one = part_one(lines)
result_part_two = part_two(lines)

print("Part 1 result:", result_part_one)
print("Part 2 result:", result_part_two)
