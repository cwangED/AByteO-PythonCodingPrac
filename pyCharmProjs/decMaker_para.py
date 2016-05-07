#coding=utf-8
#!/usr/bin/python
# Filename: decMaker_para.py

def decMaker(decArg1, decArg2):
    print "1. I make decorators! with args: ", decArg1, decArg2
    def myDec(funcToDec):
        print "2. I am a decorator! with args: ", decArg1, decArg2
        def wrapper(*args, **kwargs):
            print "3. I'm the wrapper"
            return funcToDec(*args, **kwargs)
        print "4. decorator return wrapper"
        return wrapper
    print "5. decorator maker return decorator"
    return myDec
@decMaker('decArg1', 'decArg2')
def funcToDec(args = "fuck!"):
    print "6. I am the deced func", args

funcToDec()
print "--------------"
funcToDec = decMaker('newArg1', 'newArg2')(funcToDec)
funcToDec('Fuck!!!')
'''newDec = decMaker('decArg1', 'decArg2')
funcToDec = newDec(funcToDec)
funcToDec()'''

'''
print "---------------"
funcToDec2 = decMaker()(funcToDec)
funcToDec2()

print "---------------"
@decMaker()
def funcToDec2():
    print "7. I am the second deced func"

funcToDec2()'''