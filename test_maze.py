"""
Creates a wXh of 1's and 0's maze
Taken from RosettaCode site for maze creation
"""
from random import shuffle, randrange

def make_maze(w = 20, h = 20):
  vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w+1)]
  ver = [['100'] * w + ['1'] for _ in range(h)] + [[]]
  hor = [['111'] * w + ['1'] for _ in range(h+1)]

  def walk(x, y):
    vis[y][x] = 1
    d = [(x-1, y), (x, y + 1), (x+1, y), (x, y - 1)]
    shuffle(d)
    for (xx, yy) in d:
      if vis[yy][xx]: continue
      if xx == x: hor[max(y, yy)][x] = "100"
      if yy == y: ver[y][max(x, xx)] = "000"
      walk(xx, yy)
  walk(randrange(w), randrange(h))
  for (a, b) in zip(hor, ver):
    print(''.join(a+ ['\n'] + b))

make_maze()
