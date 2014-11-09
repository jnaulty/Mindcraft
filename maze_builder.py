"""
Builds a Maze

"""

import minecraft.minecraft as minecraft
import minecraft.block as block
import time

mc = minecraft.Minecraft.create()
#Smooth Grass World
mc.setBlocks(-100, -1, -100, 100, 0, 100, 2)
mc.setBlocks(-100, 1, -100, 100, 100, 100, 0)
mc.postToChat("Begin Building Maze")


#grab maze file 
with open('maze.txt', 'r') as f:
  data = f.read()
f.close()

def cur_pos():
  #return list of player's tile position
  x,y,z = mc.player.getTilePos()
  location = [x, y, z]
  return location

def check_block(location, BLOCK, direction):
  #return Boolean if location has block.block
  #location = (x, y, z)
  #block = mcpi block type in CAPS
  if mc.getBlock(location[0], location[1], location[2]) == BLOCK:
    return True
  else:
    return False

def check_block_dir(BLOCK):
  #BLOCKS =takes block type: block.TYPE
  #direction: forward, left, right, behind
  space_dict = {'forward': 0, 'left': 0, 'right': 0, 'back': 0}
  pos = cur_pos()
  fwd = pos[2]+1
  left = pos[0]-1
  right = pos[0]+1
  back = pos[2]-1
  for key in space_dict:
    if key == 'forward':
      while mc.getBlock(pos[0], pos[1], fwd) == BLOCK:
        space_dict['forward'] += 1
        fwd +=1
    elif key == 'left':
      while mc.getBlock(left, pos[1], pos[2]) == BLOCK:
        space_dict['left'] -= 1
        left +=1
    elif key == 'right':
      while mc.getBlock(right, pos[1], pos[2]) == BLOCK:
        space_dict['right'] += 1
        right +=1
    elif key == 'back':
      while mc.getBlock(pos[0], pos[1], back) == BLOCK:
        space_dict['back'] += 1
        back -=1
  return space_dict
      

def nav_maze(pos):
  

def build_maze(layer):
  """
  Takes in a text generated maze.
  Clears a space in front of player position
  moves player to middle of maze on x-axis
  builds maze
  clears entrance to maze

  """
  #get player position
  #may also use origin = mc.player.getTilePos()
  #then use origin.x, origin.y, origin.z to set
  x,y,z = mc.player.getTilePos()
  lines = layer.split("\n")
  x_origin = x
  z_origin = z
  z_lines = len(lines)
  x_lines = len(lines[0])
  midline = x_lines//2
  #clear space for maze
  mc.setBlocks(x, y, z, x+x_lines, y+30, z+z_lines, block.AIR)
  #put player outside of maze in middle
  mc.player.setTilePos(midline, y, z-1)
  
  for line in lines:
    x_origin=0	
    for char in line:
      if char == "1":
        #set block where 1 goes
        mc.setBlocks(x_origin, y, z, x_origin, y+2, z,  block.DIAMOND_BLOCK)
        #add one to the origin along x-axis
      else:
	char == "0"
	mc.setBlocks(x_origin, y, z, x_origin, y+2, z, block.AIR)
      x_origin+=1
    #add one to the origin along z-axis
    z+=1
  new_pos = cur_pos()
  new_pos[2]+=1 
  #make a doorway to maze
  if not check_block(new_pos, block.AIR):
    mc.setBlocks(new_pos[0], new_pos[1], new_pos[2], new_pos[0], new_pos[1]+2, new_pos[2]+1, block.AIR)  
      

        
build_maze(data)






