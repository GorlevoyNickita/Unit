#Unit class, attributes "name", "health", "attack", "defense".
# in "name" only lowercase data, in "health", "attack", "defense" only numeric data
import datetime
import time


class Unit:

    def __init__(self, name=None, health=None, attack=None, protection=None):

        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError('not name')
        if isinstance(health, int):
            self.health = health
        else:
            raise ValueError('not int')

        if isinstance(attack, int):
            self.attack = attack
        else:
            raise ValueError('not int')

        if isinstance(protection, int):
            self.protection = protection
        else:
            raise ValueError(
                'not int')  # If I just put print, it shows as an error, but with valueError it shows that else was executed

    def foo(self):
        return f'Name: {self.name} \nHealth: {self.health} \nAttack: {self.attack}  \nProtection: {self.protection}'


unit = Unit('Hero', 100, 10, 6)
print(unit.foo())

print('-' * 100)
#decorator, measuring the time of the function
def time_stamp(func):

    def new_func(*args, **kwargs):
        start = datetime.datetime.now()
        print('starting process')
        x = func(*args, **kwargs)
        stop = datetime.datetime.now()
        print(f'time complate func:', stop - start)
        return x

    return new_func()

@time_stamp
def foo():
    time.sleep(0.0001)
    print('.....')
    lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum', [1, 2, 3]]
    lst2 = []
    print(lst1)
    for i in lst1:
        if type(i) != str:
            continue
        lst2.append(i)

@time_stamp
def bar():
    time.sleep(0.00001)
    print('......')
