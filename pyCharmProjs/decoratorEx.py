#coding=utf-8
#!/usr/bin/python
# Filename: decoratorEx.py

# bold decorator
def makebold(fn):
    def wrapper():
        return "<b>" + fn() + "<b>"
    return wrapper

# italic decorator
def makeitalic(fn):
    def wrapper():
        return "<i>" + fn() + "<i>"
    return wrapper

@makebold
@makeitalic
def say():
    return "hello"

print say()

def say1():
    return "say hello"
say1 = makebold(makeitalic(say1))

print say1()