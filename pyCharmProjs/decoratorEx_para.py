#coding=utf-8
#/usr/bin/python
# Filename: decoratorEx_para.py

# bold装饰器
def makebold(fn):
    def wrapper(param="hello"):
        # 在前后加入标签
        return "<b>" + fn(param) + "</b>"
    return wrapper

# italic装饰器
def makeitalic(fn):
    def wrapper(param="hello"):
        # 加入标签
        return "<i>" + fn(param) + "</i>"
    return wrapper

@makebold
@makeitalic
def say(param = "hello"):
    return param

print say("fuck you!")
#outputs: <b><i>hello</i></b>

# 等价的代码
def say1(param = "fuck_noisy_stupids"):
    return param
say1 = makebold(makeitalic(say1))

print say1()
#outputs: <b><i>hello</i></b>