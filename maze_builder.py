# Author: John Naulty Jr.
# October 2014
# Cognitive Technology Group
"""
Builds a Maze

"""

import minecraft.minecraft as minecraft
import minecraft.block as block
import time
import serial

mc = minecraft.Minecraft.create()
# Smooth Grass World
mc.setBlocks(-100, -1, -100, 100, 0, 100, 2)
mc.setBlocks(-100, 1, -100, 100, 100, 100, 0)
mc.postToChat("Begin Building Maze")


# grab maze file
# with open('maze2.txt', 'r') as f:
#  data = f.read()
# f.close()
from gen_maze import maze
data = maze(20, 20)


def cur_pos():
    # return vec3
    # get it with pos.x, pos.y, pos.z
    pos = mc.player.getTilePos()
    return pos


def check_block(location, BLOCK):
    # return Boolean if location has block.block
    #location = (x, y, z)
    # block = mcpi block type in CAPS
    if mc.getBlock(location.x, location.y, location.z) == BLOCK:
        return True
    else:
        return False


def check_block_dir(BLOCK):
    # BLOCKS =takes block type: block.TYPE
    # direction: forward, left, right, behind
    space_dict = {'u': 0, 'l': 0, 'r': 0, 'd': 0}
    pos = cur_pos()
    fwd = mc.getBlock(pos.x, pos.y, pos.z + 1)
    left = mc.getBlock(pos.x + 1, pos.y, pos.z)
    right = mc.getBlock(pos.x - 1, pos.y, pos.z)
    back = mc.getBlock(pos.x, pos.y, pos.z - 1)
    for key in space_dict:
        if key == 'u' and fwd == BLOCK:
            space_dict['u'] += 1
        elif key == 'l'and left == BLOCK:
            space_dict['l'] += 1
        elif key == 'r'and right == BLOCK:
            space_dict['r'] += 1
        elif key == 'd' and back == BLOCK:
            space_dict['d'] += 1
    return space_dict


ser = serial.Serial('/dev/ttyACM0', 9600)

def move_player():
    """
    right now, this is a command line interface with moving
    the avatar. Eventually these commands will be taken via the BCI
    interface API. As of now, this is just to fill in the void.
    """
    open_spaces = check_block_dir(block.AIR)
    input_list = []
    for key in open_spaces:
        if open_spaces[key] == 1:
            input_list.append(key)
    # move = raw_input('---Type where you want to move--- \n' +
    #                  str(input_list) + ' ')
    move = ser.readline()
    pos = cur_pos()
    if 'u' in move and 'u' in input_list:
        mc.player.setTilePos(pos.x, pos.y, pos.z + 1)
    elif 'd' in move and 'd' in input_list:
        mc.player.setTilePos(pos.x, pos.y, pos.z - 1)
    elif 'l' in move and 'l' in input_list:
        mc.player.setTilePos(pos.x + 1, pos.y, pos.z)
    elif 'r' in move and 'r' in input_list:
        mc.player.setTilePos(pos.x - 1, pos.y, pos.z)


def set_cam():
    # birds eye view position
    entity = mc.getPlayerEntityIds()
    mc.camera.setFollow(entity[0])


def build_maze(layer):
    """
    Takes in a text generated maze.
    Clears a space in front of player position
    moves player to middle of maze on x-axis
    builds maze
    clears entrance to maze

    """
    # get player position
    # may also use origin = mc.player.getTilePos()
    # then use origin.x, origin.y, origin.z to set
    x, y, z = mc.player.getTilePos()
    if isinstance(layer, str):
        lines = layer.split("\n")
    else:
        lines = layer
    x_origin = x
    z_origin = z
    z_lines = len(lines)
    x_lines = len(lines[0])
    midline = x_lines // 2
    # clear space for maze
    mc.setBlocks(x, y, z, x + x_lines, y + 30, z + z_lines, block.AIR)
    # put player outside of maze in middle
    mc.player.setTilePos(midline, y, z - 1)

    for line in lines:
        x_origin = 0
        for char in line:
            if char == "1" or char == 1:
                # set block where 1 goes
                mc.setBlocks(x_origin, y, z, x_origin, y +
                             2, z,  block.DIAMOND_BLOCK)
                # add one to the origin along x-axis
            else:
                char == "0" or char == 0
                mc.setBlocks(x_origin, y, z, x_origin, y + 2, z, block.AIR)
            x_origin += 1
        # add one to the origin along z-axis
        z += 1
    new_pos = cur_pos()
    new_pos.z += 1
    # make a doorway to maze
    if not check_block(new_pos, block.AIR):
        mc.setBlocks(new_pos.x, new_pos.y, new_pos.z + 1,
                     new_pos.x, new_pos.y + 2, new_pos.z + 1, block.AIR)


def start():
    set_cam()
    mc.player.setPos(0, 0, 0)
    build_maze(data)
    pos = cur_pos()
    mc.player.setPos(pos.x + .5, pos.y, pos.z + 2.5)

start()
while True:
    move_player()
