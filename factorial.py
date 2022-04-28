def factorial(x:int) -> int:
    """
    :x is integer input
    """
    n=1
    facto=1
    if x==0:
        return 1
    elif x>0:
        while n<=x:
            facto*=n
            n+=1
        '''
            also can use :
            for x in range(1,x):
                facto*=n
        '''
    return facto

for f in range(0,36):
    print(f, factorial(f))