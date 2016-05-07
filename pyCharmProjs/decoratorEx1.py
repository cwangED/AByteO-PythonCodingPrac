#coding=utf-8
#!/usr/bin/python
# Filename: decoratorEx1.py

# 这不是黑魔法，你只需要让包装传递参数:

def a_decorator_passing_arguments(function_to_decorate):
    def a_wrapper_accepting_arguments(arg1, arg2):
            print "I got args! Look:", arg1, arg2
            function_to_decorate(arg1, arg2)
    return a_wrapper_accepting_arguments

# 当你调用装饰器返回的函数，实际上是调用包装函数，所以给包装函数传递参数即可将参数传给装饰器函数

@a_decorator_passing_arguments
def print_full_name(first_name, last_name):
    print "My name is", first_name, last_name

print_full_name("Peter", "Venkman")
# outputs:
#I got args! Look: Peter Venkman
#My name is Peter Venkman