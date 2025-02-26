# Video: https://www.youtube.com/watch?v=1P2UgdAWwYg&list=PL6BsET-8jgYXTuSlJNYQS740YMCRHT79g
# Textbook: Ch.1.6

# Print and None (Fall 2022 Midterm 1)

s = "Knock"
print(print(print(s, s) or print("Who's There?")), "Who?")


# Functional arguments

def twice(f, x):
    """Return f(f(x))

    >>> twice(square, 2)
    16
    >>> from math import sqrt
    >>> twice(sqrt, 16)
    2.0
    """
    return f(f(x))


def square(x):
    return x * x


result = twice(square, 2)
print(result)


# Functional return values

def make_adder(n):
    """Return a function that takes one argument k and returns k + n.

    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """

    def adder(k):
        return k + n

    return adder


# Lexical scope and returning functions

def f(x, y):
    return g(x)


def g(a):
    return a + y


# This expression causes an error because y is not bound in g.
# f(1, 2)

# Lambda (Fall 2022 Midterm 1)

print(twice(lambda y: y + y, 3))

bear = -1
oski = lambda print: print(bear)  # 此处print是一个形参的名字，不是内置函数print
bear = -2
oski(abs)  # 即abs(bear)


def f(x):
    """f(x)(t) returns max(x*x, 3*x)
    if t(x) > 0, and 0 otherwise.
    """
    y = max(x * x, 3 * x)

    def zero(t):  # t = lambda z: z - y + 10
        if t(x) > 0:  # t(x) = x - y + 10，其中 x 是外部变量 y 的当前值，因此表达式变为 y - y + 10，简化后总是等于 10
            return y
        return 0

    return zero


y = 1
while y < 10:
    if f(y)(lambda z: z - y + 10):  # 即zero(lambda z: z - y + 10)
        max = y
    y = y + 1

