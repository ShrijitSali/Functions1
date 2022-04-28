def sum_numbers(*args:float) -> float:
    """
        star args take multiple inputs to give output  which is sum of given args
    """
    sum=0
    for a in args:
        sum+=a

    return sum

print(sum_numbers(1,2,3))