
# gcd of the two numbers

def gcd_calci(a,b):
    if a>b:
        a,b=b,a
    while b:
         a,b=b,a%b
    return a
a = int(input("Enter a: "))
b = int(input("Enter b: "))

print(f"The GCD of {a} and {b} is {gcd_calci(a,b)}")