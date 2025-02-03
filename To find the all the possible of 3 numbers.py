
# to check all the possible values of 3 numbers 
def sum (a,b,c):
    if a==b and a==c and c==a :
        print("all are equal")
    elif a==b  :
        print("a and b are equal")
    elif a==c :
        print ("a and c are equal")
    elif b==c :
        print("b and c are equal ")
    elif a>b and a>c :
        print ("a is greater")
    elif c>a and c>b:
        print ("c is greater")
    else :
        print(" b is greater")

a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
c=int(input("enter the value of c"))
sum(a,b,c)   