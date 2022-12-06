def get_file_lines(f_name):
  lines = []
  try:
    with open(f_name, 'r') as f:
      for line in f:
        buf = ""
        for ch in line:
          if ch == '\n':
            break
          buf += ch
        lines.append(buf)
  except IOError as e:
    print("I/O Error({0}): {1}".format(e.errno, e.strerror)) 
  except:
    print("Unexpected error:", sys.info()[0])
  return lines
