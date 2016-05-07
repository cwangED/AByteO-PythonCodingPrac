#coding=utf-8
#!/usr/bin/python
# Filename:

def decratorGen(funcToDec):
    def wrapper(*args, **kwargs):
        print "actions before"
        funcToDec(*args, **kwargs)
        print "actions after"
    return wrapper

@decratorGen
def funcNoArg():
    print "I have no args"

@decratorGen
def funcMArgs(a, b, c):
    print "I have args (%s, %s, %s)" % (a, b, c)

@decratorGen
def funcMArgs2(a, b, c, d = "fuck noise makers!!!"):
    print "I have args (%s, %s, %s, %s)" % (a, b, c, d)

@decratorGen
def funcUArgs(*args, **kwargs):
    print "I have args: ", args
    print "and args: ", kwargs

class Marry(object):
    def __init__(self):
        self.age = 31

    @decratorGen
    def sayYourAge(self, lie = -3):
        print "I am %s, what did you think ?" % (self.age + lie)

funcNoArg()
funcMArgs(c = 1, a = 2, b =100 )
funcMArgs2(1, 2, 3)
funcUArgs(1, 2, 4, 5, 6, stupidNoiseMaker = 100)
m = Marry()
m.sayYourAge()