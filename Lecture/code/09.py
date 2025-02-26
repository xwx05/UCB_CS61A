# Video: https://www.youtube.com/watch?v=VYYkJ1OLXBw&list=PL6BsET-8jgYUUWPap4etQjZVWlWUeFxn0&ab_channel=JohnDeNero
# Textbook: Ch.1.7

def streak(n):
    """Return whether positive n is a dice integer in which all the digits are the same.

    >>> streak(22222)
    True
    >>> streak(4)
    True
    >>> streak(22322)  # 2 and 3 are different digits.
    False
    >>> streak(99999)  # 9 is not allowed in a dice integer.
    False
    >>> streak(505)
    False
    >>> streak(707)
    False
    >>> streak(7070)
    False
    >>> streak(33333333333333)
    True
    """
    return (n >= 1 and n <= 6) or (n >= 10 and n % 10 == n // 10 % 10 and streak(n // 10))  # all pairs of adjacent digits are equal


def smallest_factor(n):
    """Return the smallest divisor of n above 1.

    >>> smallest_factor(10)
    2
    >>> smallest_factor(45)
    3
    >>> smallest_factor(49)
    7
    """

    def smallest_divisor(k):
        "Return the smallest divisor of n above or equal to k."
        if n % k == 0:
            return k
        else:
            return smallest_divisor(k + 1)

    return smallest_divisor(2)


def unique_prime_factors(n):
    """Return the number of unique prime factors of n.

    >>> unique_prime_factors(51)  # 3 * 17
    2
    >>> unique_prime_factors(9)   # 3 * 3
    1
    >>> unique_prime_factors(576) # 2 * 2 * 2 * 2 * 2 * 2 * 3 * 3
    2
    """
    k = smallest_factor(n)

    def no_k(n):
        "Return the number of unique prime factors of n other than k."
        if n == 1:  # 说明已经因数分解完毕
            return 0
        elif n % k != 0:  # 说明k不是n的因数
            return unique_prime_factors(n)
        else:
            return no_k(n // k)

    return 1 + no_k(n)  # 1 表示当前找到的质因数 k，no_k(n) 表示其他质因数的个数


def sevens_iter(n, k):
    """Return the (clockwise) position of who says n among k players.

    >>> sevens_iter(2, 5)
    2
    >>> sevens_iter(6, 5)
    1
    >>> sevens_iter(7, 5)
    2
    >>> sevens_iter(8, 5)
    1
    >>> sevens_iter(9, 5)
    5
    >>> sevens_iter(18, 5)
    2
    """
    i, who, direction = 1, 1, 1
    while i < n:
        if i % 7 == 0 or has_seven(i):
            direction = -direction
        who = who + direction
        if who > k:
            who = 1
        if who < 1:
            who = k
        i = i + 1
    return who


def sevens(n, k):
    """Return the (clockwise) position of who says n among k players.

    >>> sevens(2, 5)
    2
    >>> sevens(6, 5)
    1
    >>> sevens(7, 5)
    2
    >>> sevens(8, 5)
    1
    >>> sevens(9, 5)
    5
    >>> sevens(18, 5)
    2
    """

    def f(i, who, direction):
        if i == n:
            return who
        if i % 7 == 0 or has_seven(i):
            direction = -direction
        who = who + direction
        if who > k:
            who = 1
        if who < 1:
            who = k
        return f(i + 1, who, direction)

    return f(1, 1, 1)


def has_seven(n):
    if n == 0:
        return False
    elif n % 10 == 7:
        return True
    else:
        return has_seven(n // 10)


def count_partitions(n, m):
    """
    The number of partitions of a positive integer n, using parts up to size m, is the number
    of ways in which n can be expressed as the sum of positive integer parts up to m in non-decreasing order.
    >>> count_partitions(6,4)
    9
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count_partitions(n-m, m)  # use at least one m, 只要在剩下的n-m中递归调用
        without_m = count_partitions(n, m-1)  # Don't use any m
    return with_m + without_m


def count_park(n):
    """Count the ways to park cars and motorcycles in n adjacent spots.
    >>> count_park(1)  # '.' or '%'
    2
    >>> count_park(2)  # '..', '.%', '%.', '%%', or '<>'
    5
    >>> count_park(4)  # some examples: '<><>', '.%%.', '%<>%', '%.<>'
    29
    """
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return 2 * count_park(n - 1) + count_park(n - 2)  # car, motorcycle, or empty spot
