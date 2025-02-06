from operator import add, mul

square = lambda x: x * x

identity = lambda x: x

triple = lambda x: 3 * x

increment = lambda x: x + 1

HW_SOURCE_FILE = __file__


def product(n, term):
    """Return the product of the first n terms in a sequence.

    n: a positive integer
    term:  a function that takes one argument to produce the term

    >>> product(3, identity)  # 1 * 2 * 3
    6
    >>> product(5, identity)  # 1 * 2 * 3 * 4 * 5
    120
    >>> product(3, square)    # 1^2 * 2^2 * 3^2
    36
    >>> product(5, square)    # 1^2 * 2^2 * 3^2 * 4^2 * 5^2
    14400
    >>> product(3, increment) # (1+1) * (2+1) * (3+1)
    24
    >>> product(3, triple)    # 1*3 * 2*3 * 3*3
    162
    """
    sum = 1
    for i in range(1, n + 1):
        sum *= term(i)
    return sum


def accumulate(fuse, start, n, term):
    """Return the result of fusing together the first n terms in a sequence 
    and start.  The terms to be fused are term(1), term(2), ..., term(n). 
    The function fuse is a two-argument commutative & associative function.

    >>> accumulate(add, 0, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> accumulate(add, 11, 5, identity) # 11 + 1 + 2 + 3 + 4 + 5
    26
    >>> accumulate(add, 11, 0, identity) # 11 (fuse is never used)
    11
    >>> accumulate(add, 11, 3, square)   # 11 + 1^2 + 2^2 + 3^2
    25
    >>> accumulate(mul, 2, 3, square)    # 2 * 1^2 * 2^2 * 3^2
    72
    >>> # 2 + (1^2 + 1) + (2^2 + 1) + (3^2 + 1)
    >>> accumulate(lambda x, y: x + y + 1, 2, 3, square)
    19
    """
    for i in range(1, n + 1):
        start = fuse(start, term(i))
    return start


def summation_using_accumulate(n, term):
    """Returns the sum: term(1) + ... + term(n), using accumulate.

    >>> summation_using_accumulate(5, square) # square(1) + square(2) + ... + square(4) + square(5)
    55
    >>> summation_using_accumulate(5, triple) # triple(1) + triple(2) + ... + triple(4) + triple(5)
    45
    >>> # This test checks that the body of the function is just a return statement.
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(summation_using_accumulate)).body[0].body]
    ['Expr', 'Return']
    """
    return accumulate(add, 0, n, term)


def product_using_accumulate(n, term):
    """Returns the product: term(1) * ... * term(n), using accumulate.

    >>> product_using_accumulate(4, square) # square(1) * square(2) * square(3) * square()
    576
    >>> product_using_accumulate(6, triple) # triple(1) * triple(2) * ... * triple(5) * triple(6)
    524880
    >>> # This test checks that the body of the function is just a return statement.
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(product_using_accumulate)).body[0].body]
    ['Expr', 'Return']
    """
    return accumulate(mul, 1, n, term)


def make_repeater(f, n):
    """Returns the function that computes the nth application of f.

    >>> add_three = make_repeater(increment, 3)  # add_three = make_repeater函数的返回值，即repeat函数
    >>> add_three(5)  # 即repeat(5)
    8
    >>> make_repeater(triple, 5)(1) # 3 * (3 * (3 * (3 * (3 * 1))))
    243
    >>> make_repeater(square, 2)(5) # square(square(5))
    625
    >>> make_repeater(square, 3)(5) # square(square(square(5)))
    390625
    """

    def repeat(x):
        for i in range(n):
            x = f(x)
        return x

    return repeat


## [Optional] Exam Practice
# Fall 2019 MT1 Q3: You Again [Higher-Order Functions]
def parabola(x):
    """A parabola function (for testing the again function)."""

    return (x - 3) * (x - 6)


def vee(x):
    """A V-shaped function (for testing the again function)."""

    return abs(x - 2)


def again(f):
    """Return the smallest non-negative integer n such that f(n) == f(m) for some m < n.

    >>> again(parabola)  # parabola(4) == parabola(5)
    5
    >>> again(vee)  # vee(1) == vee(3)
    3
    """
    n = 1
    while True:
        m = 0
        while m < n:
            if f(m) == f(n):
                return n
            m += 1
        n += 1


# Fall 2021 MT1 Q1b: tik [Functions and Expressions]
def tik(tok):
    """Returns a function that takes gram and prints tok and gram on a line.

    >>> tik(5)(6)
    5 6
    >>> tik(tik(5)(print(6)))(print(7))
    6
    5 None
    7
    None None
    """

    def insta(gram):
        print(str(tok) + " " + str(gram))

    return insta

'''
    解释如下：
    1. tik(5)(print(6)):
        print(6) 会先执行，输出 6，并返回 None。
        tik(5)(None) 会执行 tik(5)，返回一个函数 insta，然后调用 insta(None)。
        insta(None) 会执行 print(str(5) + " " + str(None))，输出 5 None。
    2. tik(tik(5)(print(6)))(print(7)) 此时即为 tik(None)(print(7))
        tik(5)(print(6)) 的结果是 None，所以 tik(None) 会返回一个函数 insta。
        print(7) 会先执行，输出 7，并返回 None。
        insta(None) 会执行 print(str(None) + " " + str(None))，输出 None None
'''
