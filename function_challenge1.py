sum=0
def sum_eo(n,t):
    sum=0
    if t=="e":
        for x in range(0,n,2):

            sum+=x

        return sum
    elif t=="o":
        for x in range(1,n,2):
            sum+=x
        return sum
    else:
        return -1

x=sum_eo(10,"e")
print(x)
    # y=0
    # if t=="e":
    #
    #
    #     for x in range(0,n,2):
    #         y=y+x
    #     return y
            # if x%2==0:
            #     sum+=x
            # else:
            #     continue
            # return sum
    # elif t=="o":
    #     for x in range(n):
    #         if x%2!=0:
    #             sum+=x
    #         else:
    #             continue
    #     return sum
    # else:
    #     return -1

x=sum_eo(10,'e')
print(x)