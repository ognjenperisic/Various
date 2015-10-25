#!/usr/bin/env python

# Bibtex author reversal tool ver 0.1
# no regular expression were used

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
      f_out.write("\n")
      
      
   else:
      if "author" not in line:
         f_out.write(line)
      else:
         
         author_elements = line.split('"')
         print "\n"
         #print author_elements
         f_out.write(author_elements[0])  # print author = 
         f_out.write('"');
        
         authors = author_elements[1].split(" and ")
         #print "authors = ", authors
         
         for i, author in enumerate(authors):
         
            elements = author.split()
            length = 0
            #for j in elements:
               #print "j = ", j, len(j)
            #   if len(j)==2:
            #     length = 1
            if (elements[0][1]=="."):
              length=1
            #print "length = ", length, "\n"
            
            if length==1:            
               for k, m in enumerate(author.split()[1:]):
                 #print k, "->", m
                 if k==(len(author.split())):
                   f_out.write(' ')
                 f_out.write(m)
               #print author.split()[0]
               
               f_out.write(' ')
               f_out.write(author.split()[0])
            else:
              print author
              f_out.write(author)
              
            if i<(len(authors)-1):
               f_out.write(' and ')
            
            
            #f_out.write(' and ')
           
         f_out.write('",\n');   
         
  
f_out.close()
f_in.close()