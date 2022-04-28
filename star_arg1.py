def test_star(*args):
    print(args) #here we get tuple
    for x in args:
        print(x) # unpacked arguments

test_star(0,1,2,3,4,5)