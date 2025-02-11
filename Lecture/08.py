# Currying

from operator import add, mul

def curry(f):
    """Curry a two-argument function.

    >>> m = curry(add)
    >>> add_three = m(3)
    >>> add_three(4)
    7
    >>> m(2)(1)
    3
    """
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g


def square(x):
    """Square x.

    >>> square(3)
    9
    """
    return pow(x, 2)

def cube(x):
    """Cube x.

    >>> cube(3)
    27
    """
    return pow(x, 3)

def reverse(f):
    return lambda x, y: f(y, x)

square = curry(reverse(pow))(2)
cube = curry(reverse(pow))(2)


# Newton

def find_zero(f, x=1):
    """Return a zero of the function f."""
    update = newton_update(f)
    while not close(f(x), 0):
        x = update(x)
    return x

def close(x, y, tolerance=1e-15):
    return abs(x - y) < tolerance

def slope(f, x, a=1e-10):
    """Return the approximate slope of f at x.

    >>> f = lambda x: x * x - 16
    >>> slope_at_two = 4
    >>> abs(slope(f, 2) - slope_at_two) < 1e-3
    True
    """
    return (f(x+a) - f(x)) / a

def newton_update(f):
    """Return the Newton update for f."""
    return lambda x: x - f(x) / slope(f, x)

def sqrt(a):
    """Return the square root of a.

    >>> sqrt(9)
    3.0
    """
    def f(x):
        return x*x - a
    return find_zero(f)

def inverse(f):  # 反函数
    """Return the inverse function of f.

    >>> sqrt = inverse(lambda x: x * x)
    >>> sqrt(16)
    4.0
    """
    return lambda y: find_zero(lambda x: f(x)-y)  # 找的是f(x) = y的零点




# Twenty-one

def play(strategy0, strategy1, goal=21):
    """Play twenty-one and return the index of the winner.

    >>> play(two_strat, two_strat)
    1
    """
    n = 0
    who = 0  # Player 0 goes first
    while n < goal:
        if who == 0:
            n = n + strategy0(n)
            who = 1
        elif who == 1:
            n = n + strategy1(n)
            who = 0
    return who  # The player who didn't just add to n

def two_strat(n):
    return 2

def best_strat(n):
    return min(4 - n % 4, 3)

def interactive_strat(n):
    choice = 0
    while choice < 1 or choice > 3:
        print('How much will you add to', n, '(1-3)?', end=' ')
        choice = int(input())
    return choice

def noisy(who, s):
    """A strategy that prints its choices.

    >>> play(noisy(0, two_strat), noisy(1, two_strat))
    Player 0 added 2 to 0 to reach 2
    Player 1 added 2 to 2 to reach 4
    Player 0 added 2 to 4 to reach 6
    Player 1 added 2 to 6 to reach 8
    Player 0 added 2 to 8 to reach 10
    Player 1 added 2 to 10 to reach 12
    Player 0 added 2 to 12 to reach 14
    Player 1 added 2 to 14 to reach 16
    Player 0 added 2 to 16 to reach 18
    Player 1 added 2 to 18 to reach 20
    Player 0 added 2 to 20 to reach 22
    1
    """
    def strat(n):
        choice = s(n)
        print('Player', who, 'added', choice, 'to', n, 'to reach', choice + n)
        return choice
    return strat