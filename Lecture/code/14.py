# Video: https://www.youtube.com/watch?v=Q-CewobDFZM&list=PL6BsET-8jgYWfS7Jqp64nI7uQLXLPWObR&ab_channel=JohnDeNero
# Textbook: Ch.2.4

# Trees
def tree(label, branches=[]):  # A tree has a root label and a list of branches
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def list_demos():
    s = [3, 3, 7, 9]
    u = s
    s[1] = 5
    s.append(11)

    t = [x+3 for x in s]
    for i in range(len(s)):
        s[i] = s[i] + 3

    [s[-(i+1)] for i in range(len(s))]
    for i in range(len(s)):
        s[i] = s[-(i+1)]

def sums(n, m):
    """Return lists that sum to n containing positive numbers up to m that
    have no adjacent repeats, for n > 0 and m > 0.

    >>> sums(5, 1)
    []
    >>> sums(5, 2)
    [[2, 1, 2]]
    >>> sums(5, 3)
    [[1, 3, 1], [2, 1, 2], [2, 3], [3, 2]]
    >>> sums(5, 5)
    [[1, 3, 1], [1, 4], [2, 1, 2], [2, 3], [3, 2], [4, 1], [5]]
    >>> sums(6, 3)
    [[1, 2, 1, 2], [1, 2, 3], [1, 3, 2], [2, 1, 2, 1], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    """
    result = []
    for k in range(1, min(m + 1, n)):  # is the first number of a list
        for rest in sums(n-k, m):
            if rest[0] != k:
                result.append([k] + rest)
    if n <= m:
        result.append([n])
    return result

def make_path(t, p):
    """Return a tree like t also containing path p."""

    assert p[0] == label(t), 'Impossible'
    if len(p) == 1:
        return t
    new_branches = []  # 用于存储新的子树
    found_p1 = False  # 用于记录是否在树 t 的子节点中找到了路径 p 的第二个元素
    for b in branches(t):
        if label(b) == p[1]:
            new_branches.append(make_path(b, p[1:]))
            found_p1 = True
        else:
            new_branches.append(b)  # 如果不匹配，直接添加该子树
    if not found_p1:
        new_branches.append(make_path(tree(p[1]), p[1:]))  # 如果在所有子节点中都没有找到路径 p 的第二个元素，说明需要在当前树中插入一个新的子树。这个新的子树以 p[1] 为根节点，并递归地插入剩余的路径 p[1:]。
    return tree(label(t), new_branches)


def sums_demo():
    result = [[1], [2], [3]]
    for k in range(1, 4):
        for s in result:
            if s[-1] != k:
                s.append(k)
                result.append(s)
    print(result)

def identity_demos():
    a = [10]
    b = a
    a == b
    a is b
    a.extend([20, 30])
    a == b
    a is b
    
    a = [10]
    b = [10]
    a == b
    a is not b
    a.append(20)
    a != b

    s = [3, 5, 7]
    t = [9, 11]
    s.append(t)
    s.extend(t)
    t[1] = 13
    print(s)

    s = [2, 7, [1, 8]]
    t = s[2]
    t.append([2])
    e = s + t
    t[2].append(8)
    print(e)

def tuple_demos():
    (3, 4, 5, 6)
    3, 4, 5, 6
    ()
    tuple()
    tuple([1, 2, 3])
    # tuple(2)
    (2,)
    (3, 4) + (5, 6)
    (3, 4, 5) * 2
    5 in (3, 4, 5)

    # {[1]: 2}
    {1: [2]}
    {(1, 2): 3}
    # {([1], 2): 3}
    {tuple([1, 2]): 3}



