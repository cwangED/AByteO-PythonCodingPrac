#!/usr/bin/python
# Filename: using_name.py

if __name__ =='__main__':
    print 'This program is being run by itself'
    print '__name__ is: ', __name__
else:
    print 'I am being imported from another module'
    print '__name__ is: ', __name__
