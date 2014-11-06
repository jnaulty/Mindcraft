"""
Builds a simple dirt hut to shelter you from the enemies at night.
"""

from botchallenge import *


USERNAME = "i_py" # Put your minecraft username here
SERVER = "au.botchallenge.net" # Put the address of the minecraft server here

robot = Robot(USERNAME, SERVER)

with open('templates/rule110.txt', 'r') as f:
  data = f.read()
f.close()

cell_layout = data



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
            robot.move(Dir.LEFT)
        # End of the line, go back to the beginning for the next line
        for i in range(line_len):
            robot.move(Dir.RIGHT)
        robot.move(Dir.UP)
    # End of the layer, go back to the start position
    for l in range(num_lines):
        robot.move(Dir.BACKWARD)




build_layer(cell_layout)





