#!/usr/bin/python
# Filename: pickling.py

import cPickle as cp
# import pickle as P

shoplistfile = 'shoplist.data'

shoplist = ['apple', 'mango', 'carrot']

f = file(shoplistfile, 'w')
cp.dump(shoplist, f)
f.close()

del shoplist

f = file(shoplistfile)
storedlist = cp.load(f)
print storedlist