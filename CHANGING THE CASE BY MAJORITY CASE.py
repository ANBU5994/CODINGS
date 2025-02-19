def num(n):
    x=sum(1 for i in n if i.islower() )
    Y=sum(1 for i in n if i.isupper() )
    if x > Y:
        res=n.lower()
        print(res)
    else:
        print(n.upper())

num("AnbAz")