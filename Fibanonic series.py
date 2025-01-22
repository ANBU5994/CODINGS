n=int(input("enter the number"))
a,b=0,1

for i in range(n):
    print(a,end=" ")
    a,b=b,a+b
# the logic is initially store the 0 and 1 as the a,b then a+b stands for it add the no of iterations in n with the b 
#the sum of the previous term get the value