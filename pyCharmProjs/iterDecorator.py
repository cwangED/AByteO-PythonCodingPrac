#coding=utf-8
#!/usr/bin/python
# Filename: iterDecorator.py

def bread(func):
    def wrapper():
        print "</''''''\>"
        func()
        print "<\______/>"
    return wrapper

def ingredients(func):
    def wrapper():
        print "#tomatoes#"
        func()
        print "~salad~"
    return wrapper

@ingredients
@bread
def sandwich(food="--ham--"):
    print food

sandwich()
# iter dec
#sandwich = bread(ingredients(sandwich))
#sandwich()

