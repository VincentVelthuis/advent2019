import numpy as np

w1p="R8,U5,L5,D3".split(',')
max1=[0,0]
start=coord=max_coord=[0,0]


def change_location(x,y,action):
  if action[0]=='R':
    return x+int(action[1]), y
  elif action[0]=='U':
    return x, y+int(action[1])
  elif action[0]=='L':
    return x-int(action[1]), y
  elif action[0]=='D':
    return x, y-int(action[1])
  else:
    return x,y

def update_max_coord(x_0,y_0,x_new,y_new):
  x_max = max(x_0,x_new)
  y_max = max(y_0, y_new)
  return x_max, y_max



for action in range(0,len(w1p)):
  x,y = change_location(coord[0],coord[1],w1p[action])
  x_max, y_max = update_max_coord(max_coord[0],max_coord[1],x,y)
  print("(",coord[0],coord[1],") to (",x,y,"),[",x_max, y_max,"]")

  coord = [x,y]
  max_coord=[x_max,y_max]

matrix1=np.zeros((max_coord[1]+1 , max_coord[0]+1))
coord=[0,0]
for action in range(0,len(w1p)):
  x,y = change_location(coord[0],coord[1],w1p[action])
  for i range(coord[0],x):
    for j in range(coord[1],y):
      print(i,j)
print(matrix1)
