#cellular_automa.py

import numpy as np
import sys

#rule_num, num_steps = arg[1], arg[2]

#convert rule number to binary
class cell_automata(object):
  def __init__(self, rule_num, num_steps):
    self.rule_num = rule_num
    self.num_steps = num_steps

  def convert_bin(self):
    bin_num = bin(self.rule_num)[2:]
    input_bin = ['111', '110', '101', '100', '011', '010', '001', '000']
    while len(bin_num) < 8:
      bin_num = '0' + bin_num
    rule = dict(zip(input_bin, bin_num))
    return rule

  def picture(self):
    total_columns = self.num_steps*2 + 1
    midpoint = self.num_steps

    #set up first array
    cur_row=[0] * total_columns
    cur_row[midpoint]=1
    return cur_row

  def game(self):
    rule = self.convert_bin()
    cur_row = self.picture()
    count = 0
    right_edge = self.num_steps*2
    next_row = [0]*(right_edge+1)
    print ('{}'*len(cur_row)).format(*cur_row) 
    #print cur_row


    while count < self.num_steps:
      counted = 0
      while counted < len(cur_row):
        lefted = counted-1
        righted = counted+1
        if counted == 0:
          left = '0'
          cur= str(cur_row[counted])
          right = str(cur_row[righted])
          dict_key = left+cur+right 
          next_row[counted]=int(rule[dict_key])
        elif counted == right_edge:
          left = str(cur_row[lefted])
          cur= str(cur_row[counted])
          right = '0'
          dict_key = left+cur+right
          next_row[counted]=int(rule[dict_key])
        else:
          left = str(cur_row[lefted])
          #print 'left' + left + 'count' + str(counted) 
          cur= str(cur_row[counted])
          right = str(cur_row[righted])
          dict_key = left+cur+right
          next_row[counted]=int(rule[dict_key])
        counted+=1
      print ('{}'*len(next_row)).format(*next_row) 
      #print(next_row)
      cur_row=next_row[:]
      count+=1

 

#x = cell_automata(110, 200)
#x.game()
if __name__ == "__main__":
  rule_number = int(sys.argv[1])
  number_steps = int(sys.argv[2])
  x=cell_automata(rule_number, number_steps)
  x.game()







