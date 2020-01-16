from tqdm import tqdm

wire1 = "R8,U5,L5,D3".split(',')
wire2 = "U7,R6,D4,L4".split(',')

def closest_point_mh(path):
  coord = []
  small_dist = 123456789
  for x,y in tqdm(path):
    if abs(x) + abs(y) < small_dist:
      small_dist = abs(x) + abs(y)
      coord = [x,y]
  return small_dist, coord

def closest_point_sd(intersection, wire1, wire2):
  #signal distance for all intersected points
  close_coord = []
  small_dist = 123456789

  for coord in tqdm(intersection):
    sd_wire1 = first_occurence(coord,wire1)
    sd_wire2 = first_occurence(coord,wire2)
    sd_dist = sd_wire1 + sd_wire2
    if sd_dist < small_dist:
      small_dist = sd_dist
      close_coord = coord
  return small_dist, close_coord

def first_occurence(item, lst):
  for i in range(len(lst)):
    if lst[i] == item:
      return i+1

def create_path(wire):
  wpath = [[0,0]] #starts at origin
  for command in tqdm(wire):
    direction = command[0]
    distance = int(command[1:])
    
    if direction == "L":
      for step in range(distance):
        last_coord = wpath[-1]
        wpath.append([last_coord[0]-1, last_coord[1]])
    if direction == "R":
      for step in range(distance):
        last_coord = wpath[-1]
        wpath.append([last_coord[0]+1, last_coord[1]])
    if direction == "U":
      for step in range(distance):
        last_coord = wpath[-1]
        wpath.append([last_coord[0], last_coord[1]+1])
    if direction == "D":
      for step in range(distance):
        last_coord = wpath[-1]
        wpath.append([last_coord[0], last_coord[1]-1])
  return wpath[1:]  # remove origin from intersection
  
print("Creating path for wire 1.")
w1path = create_path(wire1)
print("Creating path for wire 2.")
w2path = create_path(wire2)

print("Calculating intersection.")
intersection = [value for value in tqdm(w1path) if value in w2path]

print("\nCalculation closest ManHattan (MH) point")
mh_dist,mh_coord = closest_point_mh(intersection)
print("Closest coord is", mh_coord, "with MH dist", mh_dist)

print("\nCalculation closest SignalDelay (SD) point")
sd_dist,sd_coord = closest_point_sd(intersection, w1path, w2path)
print("Closest coord is", sd_coord, "with SD dist", sd_dist)
