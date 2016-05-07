#!/usr/bin/python
# Filename:func_targs.py

def func1(farg, karg = 1, *targs):
    print "farg: ", farg
    print 'karg:', karg
    print 'targs full:', targs
    for targ in targs:
        print 'targ', targ

def func2(farg, karg = 2, **kwargs):
    print "farg: ", farg
    print 'karg: ', karg
    print "kwargs:", kwargs
    for key in kwargs:
        print "another keyword arg: %s %s" % (key, kwargs[key])

def fullfunc(farg, karg1 = 1, karg2 = 2, *targs, **kwargs):
    print "farg: ", farg
    print "karg1: ", karg1
    print "karg2: ", karg2
    print "targs: ", targs
    print "kwargs: ", kwargs
    for targ in targs:
        print "another targ: ", targ
    for key in kwargs:
        print "another keyword arg: %s => %s" % (key, kwargs[key])

def functest(a, b = 1, c = 3):
    print 'a: ', a, '; ', 'b: ', b, '; ', 'c: ', c, ';';

functest(b = 1, c = 'c', a = 1)
fullfunc(karg2 = 2, karg1 = 3, farg=1, targs = (1, 2, 3, 4), kwargs = {'a':1})