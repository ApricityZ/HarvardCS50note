def meow(n: int) -> str:
    """
    Meow n times.

    :param n: Number of times of meow
    :type n: int
    :raise TyprErrpr: If n is not an int
    :return: A string of n meows, one per line
    :rtype: Str
    """
    return "meow\n" * n

nember: int = int(input("Number: "))
meows: str = meow(nember)
print(meows, end="")