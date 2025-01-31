#to print the various types of patterns
#left lower triangle 
n=5
for i in range(n,0,-1):
    print("* "*i,end="\n")

#to print 5*5 matrix by the pattern \
n=5
for i in range(n*n):
    print("*",end=" ")
    if ((i+1)%5==0):
        print()
    