# Prime number or not 
n = int(input("Enter a no: "))


div = 0
for i in range(1, n+1):
    if n % i == 0:
        div += 1
        
if div == 2:
    print("Yes")
else:
    print("No")
