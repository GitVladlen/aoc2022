import sys

def get_file_lines(file_name):
  lines = []
  try:
    with open(file_name, 'r') as f:
      for line in f:
          buf = ""
          for ch in line:
            if ch == '\n':
              break
            buf += ch
          lines.append(buf)
  except IOError as e:
    print("I/O error({0}): {1}".format(
      e.errno, e.strerror))
  except:
    print("Unexpected error", sys.info()[0])
  return lines

lines = get_file_lines('../inputs/input_day3.txt')
#lines = get_file_lines('../inputs/test_1_day3.txt')

def get_item_type(ch):
  start = 27 if ord(ch) < ord('a') else 1
  lim = ord('A') if ord(ch) < ord('a') else ord('a')
  return ord(ch) - lim + start

def calc_priors(lines):
  res = 0
  for line in lines:
    elems = set()
    l_half = line[:len(line)//2]
    r_half = line[len(line)//2:]
    for ch in l_half:
      if ch in r_half:
        elems.add(ch)
    priors = []
    for ch in elems:
      priors.append(get_item_type(ch))
    res += sum(priors)
  return res

def calc_badges(lines):
  res = 0
  for i in range(len(lines)//3):
    elems = set()
    for ch in lines[i*3]:
      if ch in lines[i*3+1] and ch in lines[i*3+2]:
        elems.add(ch)
    badges = []
    for ch in elems:
      badges.append(get_item_type(ch))
    res += sum(badges)  
  return res

result_part_one = calc_priors(lines)
result_part_two = calc_badges(lines)

print("Part 1 result:", result_part_one)
print("Part 2 result:", result_part_two)
