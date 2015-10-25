#!/usr/bin/env python

# Bibtex edit tool ver 0.2
# removes dot (.) from the end of a string
# no regular expression were used

import argparse
import sys
import os


f_in  = open(sys.argv[1], 'r')

fname = sys.argv[1].split('.')[0]


fname = fname + '_dot_removed.txt'

f_out = open(fname, 'w')

has_CA = 0
beginning = 1
resid = ''
previous_line_length = 0

for line in f_in:   
   if len(line.rstrip())==0:      
      f_out.write("\n")      
      
   else:
      if line==".}\n":
         f_out.write("}\n")
      else:
      
        if all(["journal" not in line, "year" not in line,  "Volume" not in line, "volume" not in line, "Number" not in line, "number" not in line, "pages" not in line]):
           f_out.write(line)      
        else:
           new_line = line.replace(".","")
           #f_out.write("---------\n")
           f_out.write(new_line)
           
      
         
         
  
f_out.close()
f_in.close()
