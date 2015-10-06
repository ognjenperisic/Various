#!/usr/bin/env python

import argparse
import sys
import os


contacts = {}

res_contacts = open('residue_contacts_pairs.txt','r')
for line in res_contacts:
   pair = line.split()
   contacts[pair[0]] = pair[1];
res_contacts.close();

fname = sys.argv[1].split('.')[0]

f_in  = open(sys.argv[1], 'r')

fname_c = fname + '_beta_colored.pdb'
f_out = open(fname_c, 'w')


for line in f_in:  
   elements = line.split()
   
   if elements[0]=='ATOM':   
      cont = float(contacts[elements[5]])      
      cb = 120*(abs(cont - 14.00)/13.00) - 10.15      
      f_out.write("%s%7s  %-4s%3s%2s%4s%12s%8s%8s%6s %4.2f%12s\n" % 
      (elements[0], elements[1], elements[2], elements[3], elements[4], 
      elements[5], elements[6], elements[7], elements[8], elements[9], cb, elements[11]));
      
   else:
      f_out.write(line)
      
f_in.close()  




