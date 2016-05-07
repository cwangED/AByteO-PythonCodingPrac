#!/usr/bin/python
# Filename:func_nest.py

# define functions that nested with another
def func1():
    x1 = 'func1'
    print("func1's variable: ", x1)

    def func2():
        x2 = 'func2'
        print("func1's variable: ", x1)
        print("func2's variable: ", x2)

        def func3():
            x3 = "func3"
            print("func1's variable: ", x1)
            print("func2's variable: ", x2)
            print("func3's variable: ", x3)
        return func3()
    func2()

# define a function that return an anonymous function
# this is closure!
def func_func(m):
    x1 = m
    def func_ano(n): return x1**n
    return func_ano

func1()
funct = func_func(3)
print funct(2)