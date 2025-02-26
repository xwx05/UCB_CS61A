# Q1: Big Fib
def gen_fib():
    n, add = 0, 1
    while True:
        yield n
        n, add = n + add, n

print(next(filter(lambda n: n > 2024, gen_fib())))


# Q2: Something Different
def differences(t):
    """Yield the differences between adjacent values from iterator t.

    >>> list(differences(iter([5, 2, -100, 103])))
    [-3, -102, 203]
    >>> next(differences(iter([39, 100])))
    61
    """
    prev = next(t)
    for current in t:
        yield current - prev
        prev = current


# Q3: Partitions
def partition_gen(n, m):
    """Yield the partitions of n using parts up to size m.

    >>> for partition in sorted(partition_gen(6, 4)):
    ...     print(partition)
    1 + 1 + 1 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 2
    1 + 1 + 1 + 3
    1 + 1 + 2 + 2
    1 + 1 + 4
    1 + 2 + 3
    2 + 2 + 2
    2 + 4
    3 + 3
    """
    assert n > 0 and m > 0
    if n == m:  # 直接生成一个只包含 n 的partition
        yield str(n)
    if n - m > 0:  # 考虑至少使用一个m的情况，对n-m部分递归调用
        for p in partition_gen(n - m, m):
            yield p + ' + ' + str(m)
    if m > 1:  # 考虑不使用m的情况，对m-1部分递归调用
        yield from partition_gen(n, m-1)  # yield from 等价于下面的代码
        # for p in partition_gen(n, m-1):
        #     yield p
