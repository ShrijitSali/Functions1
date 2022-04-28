def fizz_buzz(x: int) -> str:
    """

    :param x: input integer
    :return: string value: fizz, buzz or fizzbuzz
    """
    if x % 3 == 0 and x % 5 == 0:
        """
        check if number is divisible by both 3 and 5
        """
        return "fizz buzz"
    elif x % 3 == 0:
        """check if divisible by 3"""
        return "fizz"
    elif x % 5 == 0:
        """ div by 5"""
        return "buzz"
    else:
        return str(x)


for i in range(1, 101):
    x = fizz_buzz(i)
    print(x)
