def calc_fuel(x):
    y = int(int(x) / 3) - 2
    if y < 0:
        return 0
    else:
        return y + calc_fuel(y)


with open("file.txt") as f:
  sum = 0
  for line in f:
    output = calc_fuel(int(line))
    sum += output
  print(sum)
