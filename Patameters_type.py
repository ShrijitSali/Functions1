
# always follow rule to pass args

def func(p1,p2,*args,k,**kwargs):
    print(f"Positional or keyword :... {p1},{p2}")
    print(f"var-Positional *args :... {args}")
    print(f"keyword :... {k}")
    print(f"var keyword :... {kwargs}")

func(1,2,3,4,5,9,k=6, key1=7,key2=8)

""" 
o/p:
Positional or keyword :... 1,2
var-Positional *args :... (3, 4, 5, 9)
keyword :... 6
var keyword :... {'key1': 7, 'key2':
"""