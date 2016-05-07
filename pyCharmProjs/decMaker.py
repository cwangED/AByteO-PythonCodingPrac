#coding=utf-8
#!/usr/bin/python
# Filename: decMaker.py

def decMaker():
    print "1. I make decorators!"
    def myDec(funcToDec):
        print "2. I am a decorator!"
        def wrapper(*args, **kwargs):
            print "3. I'm the wrapper"
            return funcToDec(*args, **kwargs)
        print "4. decorator return wrapper"
        return wrapper
    print "5. decorator maker return decorator"
    return myDec

def funcToDec():
    print "6. I am the deced func"

newDec = decMaker()
funcToDec = newDec(funcToDec)
funcToDec()


print "---------------"
funcToDec2 = decMaker()(funcToDec)
funcToDec2()

print "---------------"
@decMaker()
def funcToDec2():
    print "7. I am the second deced func"

funcToDec2()