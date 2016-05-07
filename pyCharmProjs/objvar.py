#!/usr/bin/python
# Filename:objvar.py

class Person:
    '''Represents a person.'''
    population = 0;
    aaa = 0
    def __init__(self, name):
        '''Initializes the person's data.'''
        self.name = name
        print '(Initializing %s)' % self.name

        Person.population += 1
        Person.aaa = 10

    def __del__(self):
        '''I am dying.'''
        print '%s says bye.' % self.name

        Person.population -= 1

        if Person.population == 0:
            print 'i am the last one.'
        else:
            print 'There are still %d people left.' % Person.population

    def sayHi(self):
        ''' Greeting by the person.

        Really, that's all it does.'''
        print 'Hi, my name is %s.' % self.name

    def howMany(self):
        '''Prints the current population.'''
        if Person.population == 1:
            print 'I am the only person here.'
        else:
            print 'We have %d persons here.' % Person.population

wang = Person('Wang')
wang.sayHi()
wang.howMany()

swaroop = Person('Swaroop')
swaroop.sayHi()
swaroop.howMany()

kalam = Person('Abdul Kalam')
kalam.sayHi()
kalam.howMany()

swaroop.sayHi()
swaroop.howMany()

wang.aaa = 1
wang.population = 1

print swaroop.population, wang.population, kalam.population, Person.population
print wang.aaa, swaroop.aaa, Person.aaa
