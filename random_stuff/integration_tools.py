def riemann_sum(func, n, a, b):
    """
    :param func: must be callable via func(x) and has to return an integer
    :param n: number of subdivisions of the interval [a, b]
    :param a: lower-bound limit of integral
    :param b: upper-bound limit of integral
    :return: approximation of integral using riemann sum method (Note: Midpoint Rule)
    """
    assert n > 0, "n must be greater than 0"
    delta_x = (b - a) / n
    x_0, x_1 = a, a + delta_x
    computed_integral = 0
    while x_1 <= b:
        midpoint = (x_1 + x_0) / 2
        computed_integral += func((midpoint))
        x_0, x_1 = x_1, x_1 + delta_x
    return delta_x * computed_integral


def riemann_sum_left(func, n, a, b):
    """
    :param func: must be callable via func(x) and has to return an integer
    :param n: number of subdivisions of the interval [a, b]
    :param a: lower-bound limit of integral
    :param b: upper-bound limit of integral
    :return: approximation of integral using riemann sum method (Note: Midpoint Rule)
    """
    assert n > 0, "n must be greater than 0"
    delta_x = (b - a) / n
    x = a
    computed_integral = 0
    while x < b:
        computed_integral += func(x)
        x += delta_x
    return delta_x * computed_integral


def trapezoidal_rule(func, n, a, b):
    """
    :param func: must be callable via func(x) and has to return an integer
    :param n: number of subdivisions of the interval [a, b]
    :param a: lower-bound limit of integral
    :param b: upper-bound limit of integral (inclusive)
    :return: approximation of integral using trapezoidal rule
    """
    assert n > 0, "n must be greater than 0"
    delta_x = (b - a) / n
    x = a
    computed_integral = 0
    while x <= b:
        computed_integral += (1 / 2) * func(x) if x in [a, b] else func(x)
        x += delta_x
    return delta_x * computed_integral


def simpsons_rule(func, n, a, b):
    """
    :param func: must be callable via func(x) and has to return an integer
    :param n: number of subdivisions of the interval [a, b] with n being an even integer
    :param a: lower-bound limit of integral
    :param b: upper-bound limit of integral
    :return: approximation of integral using simpsons rule
    """
    assert n > 0 and n % 2 == 0, "n must be greater than 0 and an even number"
    delta_x = (b - a) / n
    x, alternating = a, 0
    computed_integral = 0
    while x <= b:
        if x in [a, b]:
            computed_integral += func(x)
        else:
            computed_integral += 4 * func(x) if alternating else 2 * func(x)
        x += delta_x
        alternating = 0 if alternating else 1
    return delta_x * computed_integral * (1 / 3)


from math import sin, pi, sqrt, e, cos


def f(x):
    return sqrt(x)


def g(a):
    def f(x):
        return sqrt(a ** 2 - x ** 2)

    return f


def fresnel(x):
    return cos(x ** 2)


if __name__ == "__main__":
    x = sqrt(pi / 2)
    n = 2
    while abs(simpsons_rule(fresnel, n, 0, x) - simpsons_rule(fresnel, 100, 0, x)) >= (10**-7):
        n += 2
    print(n)
    print(simpsons_rule(fresnel, n-2, 0, x))
    print(simpsons_rule(fresnel, n, 0, x))
