#coding=utf-8
#!/usr/bin/python
# Filename: decMethod.py

def methodDec1(decedFunc):
    def wrapper(self, lie):
        lie = lie -3
        return decedFunc(self, lie)
    return wrapper

class Lucy(object):
    def __init__(self):
        self.age=32

    @methodDec1
    def sayYourAge(self, lie):
        print "I am %s, what did you think?" % (self.age + lie)

    def sayYourAge2(self, lie):
        print "I'm %s, fucker!" % (self.age + lie)

    sayYourAgeT = methodDec1(sayYourAge2)

I = Lucy()
I.sayYourAge(-3)
I.sayYourAge(1)
#I.sayYourAge3 = methodDec1(I.sayYourAge2)
#I.sayYourAge2(1)
I.sayYourAgeT(1)