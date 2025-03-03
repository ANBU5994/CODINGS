def steel(h,c,t):
    if h>=60 and c>=0.8 and t>=5700:
        return("class A")
    elif h>=60 and c>=0.8 or t>=5700:
        return("class B")
    elif h>=60 and t>=5700 or c>=0.8:
        return("class C")
    elif h>=60 or c>=0.8 and t>=5700:
         return("class D")
    elif h>=60 or c>=0.8 or t>=5700:
         return ("class E")
    else:
        return ("Class F")
    

h=int(input("enter the hardness:"))
c=float(input("enter the carbon content :"))
t=int(input("enter the tension "))
res=steel(h,c,t)
print(res)
        
    
    