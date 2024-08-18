def is_divisible(n, *args):
    if not args:
        return True
    return all(n % x == 0 for x in args)