wire1 = "R8,U5,L5,D3".split(',')
#wire1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72,U62,R66,U55,R34,D71,R55,D58,R83".split(',')
wire2 = "U7,R6,D4,L4".split(',')
#wire2 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51,U98,R91,D20,R16,D67,R40,U7,R15,U6,R7".split(',')

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
    if x + y < small_dist:
      small_dist = x + y
      coord = [x,y]
  return small_dist, coord

def create_path(wire):
  wpath = [[0,0]] #starts at origin
  for command in wire:
    direction = command[0]
    distance = int(command[1:])
    for step in range(distance):
      wpath = update_path(wpath,direction)
  return wpath[1:]  # remove origin from intersection

w1path = create_path(wire1)
w2path = create_path(wire2)
intersection = [value for value in w1path if value in w2path]

mh_dist,coord = closest_point(intersection)
print("dist: ",mh_dist)
print("coord:",coord)
