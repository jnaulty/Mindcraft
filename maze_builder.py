"""
Builds a Maze

"""

from botchallenge import *


USERNAME = "i_py" # Put your minecraft username here
SERVER = "au.botchallenge.net" # Put the address of the minecraft server here

robot = Robot(USERNAME, SERVER)

with open('templates/maze.txt', 'r') as f:
  data = f.read()
f.close()
with open('templates/ground.txt', 'r') as f:
  ground = f.read()
f.close()
ground_layout = ground

maze_layout = data
def mine_if_solid(direction):
  is_solid = robot.is_block_solid(direction)
  if is_solid: 
    robot.mine(direction)
def bot_block():
  block = robot.get_block_type(Dir.DOWN)
  if block != BlockType.COBBLESTONE:
    robot.mine(Dir.DOWN)
    robot.place(Dir.DOWN, BlockType.COBBLESTONE)
"""
Assume that you have a square matrix
Otherwise you will not return at the same spot.
"""

def build_layer(layer):
    # Move up one so we're placing the blocks downward
    robot.move(Dir.UP)
    old_lines = layer.split("\n")
    #reverses cellular automation
    lines = old_lines[::-1]
    num_lines = len(lines)
    print("There are", num_lines, "lines")
    for line in lines:
        line_len = len(line)
        for char in line:
            if char == "1":
              robot.place(Dir.DOWN, BlockType.COBBLESTONE)
            mine_if_solid(Dir.LEFT)
            robot.move(Dir.LEFT)
        # End of the line, go back to the beginning for the next line
        for i in range(line_len):
            robot.move(Dir.RIGHT)
        mine_if_solid(Dir.FORWARD)
        robot.move(Dir.FORWARD)
    # End of the layer, go back to the start position
    for l in range(num_lines):
      mine_if_solid(Dir.BACKWARD)
      robot.move(Dir.BACKWARD)

build_layer(ground_layout)
for layer in range(2):
  build_layer(maze_layout)






