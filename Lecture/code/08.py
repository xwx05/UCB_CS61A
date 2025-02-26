# Video: https://www.youtube.com/watch?v=31EDjrN1x5k&list=PL6BsET-8jgYUUBHIgUAqjrMUoPCGQcYdl&ab_channel=JohnDeNero
# Textbook: Ch.1.7

# Self-Reference

def add_up(k):
    """Add up k numbers after k repeated calls.
    >>> add_up(4)(10)(20)(30)(40)  # Add up 4 numbers: 10 + 20 + 30 + 40
    100
    """
    assert k > 0
    def f(n):
        if k == 1:
            return n
        else:
            return lambda t: add_up(k-1)(n+t)
    return f

# Recursion

from ucb import trace

def fact(n):
    """Compute n factorial.

    >>> fact(5)
    120
    >>> fact(0)
    1
    """
    result = 1
    while n > 0:
        result = result * n
        n -= 1
    return result

def fact(n):
    """Compute n factorial.

    >>> fact(5)
    120
    >>> fact(0)
    1
    """
    if n == 0 or n == 1:
        return 1
    else:
        return fact(n-1) * n

def fact_k(n, k):
    """Compute n factorial times k.

    >>> fact_k(5, 1)
    120
    >>> fact_k(5, 10)
    1200
    >>> fact_k(0, 10)
    10
    """
    if n == 0 or n == 1:
        return k
    else:
        return fact_k(n-1, k * n) # * n

def fact_tail(n):
    """Compute n factorial.

    >>> fact_tail(5)
    120
    >>> fact_tail(0)
    1
    """
    def f(n, k):
        if n == 0 or n == 1:
            return k
        else:
            return f(n-1, k * n) # * n
    return f(n, 1)


