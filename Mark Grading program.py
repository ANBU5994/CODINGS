# 90 or 90 aove a, 80 and 90 b, 70and 80 c grade 60 and 70 d grade else fail
def num(n):
    if n>=90:
        print("A grade ")
    elif n>=80 or n< 90:
        print("B grade")
    elif n>= 70 and n <60:
        print("c grade")
    elif n>=60 and n <50:
        print("d grade")
    else :
        print ("fail")

num(80)