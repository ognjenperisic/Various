#!/usr/bin/env python

import argparse
import sys
import os


fname = sys.argv[1].split('.')[0]


chains = []

f_in  = open(sys.argv[1], 'r')
for line in f_in:  
   elements = line.split() # this line is not correct, using 'split' is not very good approach
   if elements[0]=='ATOM' and elements[2]=='CA':
   #if elements[0]=='ATOM':

      print elements[0], elements[1], elements[2], elements[4], elements[5]
      if not(elements[4] in chains):
         chains.append(elements[4])
f_in.close()  




for ch in chains:

  f_in  = open(sys.argv[1], 'r')

  fname_c = fname + '_' + ch + '_CA_coordinates.txt'
  #print fname_c

  f_out = open(fname_c, 'w')

  for line in f_in:  
     elements = line.split()
     if elements[0]=='ATOM' and elements[2]=='CA':
     #if elements[0]=='ATOM':

        #print elements[0], elements[1], elements[2], elements[4], elements[5], elements[6], elements[7], elements[8]   
        if (elements[4] == ch):
           f_out.write("{0} {1} {2} {3} {4}\n".format(elements[1], elements[5], elements[6], elements[7], elements[8]))
           
  f_out.close()
  f_in.close()  
  
  
print chains 

for ch in chains:
   print ch 
