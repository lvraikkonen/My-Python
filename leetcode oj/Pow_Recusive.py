## Pow(x, n)

# simple recusive
def pow_simple(x, n):
    if n < 0:
        return 1.0 / pow_simple(x, -n)
    elif n == 0:
        return 1.0
    else:
        return x * pow_simple(x, n-1)


# improved recusive solution
def pow_recusive(x, n):
    if n < 0:
        return 1.0 / pow_recusive(x, -n)
    elif n == 0:
        return 1.0
    else:
        if n % 2 == 0:
            return pow_recusive(x, n//2) ** 2
        else:
            return x * pow_recusive(x, n//2) ** 2
