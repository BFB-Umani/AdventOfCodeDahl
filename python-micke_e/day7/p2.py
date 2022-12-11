
dirsizes = {}
checked_f = {}
currentdir = []

file = open("input.txt", "r")
for row in file:
  row = row.strip()
  if row.startswith('$ cd'):
    if len(currentdir) == 0:
      currentdir.append('/')
    elif row.split(' ')[2] == '/':
      currentdir = currentdir[0]
    elif row.split(' ')[2] == '..':
      currentdir = currentdir[:-1]
    else: currentdir.append(row.split(' ')[2])
  elif row[0].isnumeric():
    dir_str = '\\'.join(currentdir)
    if dir_str not in checked_f.keys():
      checked_f[dir_str] = []
    if row.split(' ')[1] not in checked_f[dir_str]:
      checked_f[dir_str].append(row.split(' ')[1])
      for f in range(len(currentdir)+1):
        if '\\'.join(currentdir[:f]) not in dirsizes.keys():
          if '\\'.join(currentdir[:f]).strip() == '':
            continue
          dirsizes['\\'.join(currentdir[:f])] = 0
        dirsizes['\\'.join(currentdir[:f])] += int(row.split(' ')[0])

sort_vals = sorted(dirsizes.values())
space_needed = 30000000-(70000000-sort_vals[-1])
for n in sort_vals:
  if n >= space_needed:
    print(n)
    break