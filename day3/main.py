wire1 = "R8,U5,L5,D3".split(',')
w1path = [[0,0]] #starts at origin
wire2 = "U7,R6,D4,L4".split(',')
w2path = [[0,0]] #starts at origin

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

for direction,distance in wire1:
  for step in range(0,int(distance)):
    w1path = update_path(w1path,direction)
  #print("End w1:",direction,distance)

for direction,distance in wire2:
  for step in range(0,int(distance)):
    w2path = update_path(w2path,direction)
  #print("End w2:",direction,distance)

intersection = [value for value in w1path if value in w2path]
intersection = intersection[1:] # remove origin from intersection

mh_dist,coord = closest_point(intersection)
print("distance",mh_dist)
