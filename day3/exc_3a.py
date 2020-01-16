from tqdm import tqdm

wire1 = "R8,U5,L5,D3".split(',')
wire2 = "U7,R6,D4,L4".split(',')

def update_path(path, direction):
  # take one step from the last coordinate of 'path'
  # in any given 'direction'. 
  #'new_path' is a concat of the step added to the original path.
  coord = path[-1] #last coordinate as starting point
  if direction == "L": 
    new_path = path + [[coord[0]-1, coord[1]]]
  elif direction == "R":
    new_path = path + [[coord[0]+1,coord[1]]]
  elif direction == "U":
    new_path = path + [[coord[0],coord[1]+1]]
  elif direction == "D":
    new_path = path + [[coord[0],coord[1]-1]]
  return new_path

def closest_point(path):
  coord = []
  small_dist = 123456789
  for x,y in path:
    if abs(x) + abs(y) < small_dist:
      small_dist = abs(x) + abs(y)
      coord = [x,y]
  return small_dist, coord

def create_path(wire):
  wpath = [[0,0]] #starts at origin
  for command in tqdm(wire):
    direction = command[0]
    distance = int(command[1:])
    for step in range(distance):
      wpath = update_path(wpath,direction)
  return wpath[1:]  # remove origin from intersection
  
print("Creating path for wire 1.")
w1path = create_path(wire1)
print("Creating path for wire 2.")
w2path = create_path(wire2)

print("Calculating intersection.")
intersection = [value for value in tqdm(w1path) if value in w2path]

mh_dist,coord = closest_point(intersection)
print("Closest coord is", coord, "with MH dist", mh_dist)
