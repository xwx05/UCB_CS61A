# Video: https://www.youtube.com/watch?v=aSqOiUZg7kQ&list=PL6BsET-8jgYW50w7isVJS3YumstvFX1LY&ab_channel=JohnDeNero
# Textbook: Ch.2.3

def box_pointer_example():
    def f(s):
        x = s[0]
        return [x]

    t = [3, [2+2, 5]]
    u = [f(t[1]), t]
    print(u)

box_pointer_example()  # [[4], [3, [4, 5]]]

def double_eights(s):
    """Return whether two consecutive items of list s are 8.

    >>> double_eights([1, 2, 8, 8])
    True
    >>> double_eights([8, 8, 0])
    True
    >>> double_eights([5, 3, 8, 8, 3, 5])
    True
    >>> double_eights([2, 8, 4, 6, 8, 2])
    False
    """
    for i in range(len(s)-1):
        if s[i] == 8 and s[i+1] == 8:
            return True
    return False

def double_eights_rec(s):
    """Return whether two consecutive items of list s are 8.

    >>> double_eights_rec([1, 2, 8, 8])
    True
    >>> double_eights_rec([8, 8, 0])
    True
    >>> double_eights_rec([5, 3, 8, 8, 3, 5])
    True
    >>> double_eights_rec([2, 8, 4, 6, 8, 2])
    False
    """
    if s[:2] == [8, 8]:
        return True
    elif len(s) < 2:
        return False
    else:
        return double_eights_rec(s[1:])

min(range(10), key=lambda i: abs(50 ** 0.5 - i))
sum([2, 3, 4], sum([20, 30, 40]))
any([x > 10 for x in range(10)])

xs = range(-10, 11)
ys = [x*x - 2*x + 1 for x in xs]
min(xs, key=lambda x: x*x - 2*x + 1)
xs[min(range(len(xs)), key=lambda i: ys[i])]


# Spring 2023 Midterm 2 Question
def prefix(s):
    """
    Return a list of all prefix sums of list s.
    >>> prefix([1, 2, 3, 0, 4, 5])
    [1, 3, 6, 6, 10, 15]
    >>> prefix([2, 2, 2, 0, -5, 5])
    [2, 4, 6, 6, 1, 6]
    """
    return [sum(s[:i+1]) for i in range(len(s))]


def park(n):
    """Return the ways to park cars and motorcycles in n adjacent spots.

    >>> park(1)
    ['%', '.']
    >>> park(2)
    ['%%', '%.', '.%', '..', '<>']
    >>> park(3)
    ['%%%', '%%.', '%.%', '%..', '%<>', '.%%', '.%.', '..%', '...', '.<>', '<>%', '<>.']
    >>> len(park(4))
    29
    """
    if n < 0:
        return []
    elif n == 0:
        return ['']
    else:
        return (['%'  + s for s in park(n-1)] +
                ['.'  + s for s in park(n-1)] +
                ['<>' + s for s in park(n-2)])



