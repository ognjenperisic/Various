#!/usr/bin/env python

import argparse
import sys
import os


f_in  = open(sys.argv[1], 'r')

fname = sys.argv[1].split('.')[0]


fname = fname + '_edited.txt'

f_out = open(fname, 'w')

has_CA = 0
beginning = 1
resid = ''
previous_line_length = 0

for line in f_in:   
   if len(line.rstrip())==0:
      f_out.write("{0}".format(line))
      f_out.write("\n")
      
      
   else:
      new_line = line.split('\n')
      #if len(new_line)>1:
      #  print new_line[0]
      #  print new_line[1]
      #  print "\n"
      f_out.write("{0} ".format(new_line[0].rstrip(' \t\n\r')))
      

  
f_out.close()
f_in.close()