def ackermann(m, n):
    assert n >= 0 and m >= 0, "Error"
    if m == 0:
        return n + 1

    if n == 0:
        return ackermann(m - 1, 1)

    return ackermann(m - 1, ackermann(m, n-1))


# maximum around m = 3