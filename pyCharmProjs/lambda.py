#!/usr/bin/python
# Filename: lambda.py

def make_repeater(n):
    return lambda s:s*n

twice = make_repeater(2)

print twice('word')
print twice(5)

a = [(1, 'aa'), (2, 'bb')]
b = dict(a)
c = ([1, 'aa'], [2, 'bb'])
d = dict(c)
e = ((1, 'aa'), (2, 'bb'))
f = dict(e)
g = [[1, 'aa'], [2, 'bb']]
h = dict(g)
print a, b, c, d, e, f, g, h