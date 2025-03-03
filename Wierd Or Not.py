def num(n):
    if  n % 2== 1:
        return("odd")
    elif n%2==0 and n>= 2 and n<=5 :
        return("Not wierd")
    elif n%2==0 and n>= 6 and n<=20 :
        return("wierd")
    elif n%2==0 and n>=20 :
        return("Not wierd")
n=int(input("Enter the Number:"))
res=num(n)
print(res)   