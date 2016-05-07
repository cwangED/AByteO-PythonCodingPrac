#!/usr/bin/python
# Filename: funcCallVar.py

def changeme( mylist ):
   "change"
   mylist.append([1,2,3,4]);
   print "inner func value:", mylist
   return

mylist = [10,20,30];
changeme( mylist );
print "outer func value:", mylist