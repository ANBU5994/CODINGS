''' %3 fizz , 5% ,%3 and 5% FIZZ , np --> number alone '''

def num(n):
    if (n %3 ==0) :
        print("fizz")
    elif(n%5==0):
        print("Fizz")
    elif (n %3==0 )and (n%5==0):
        print("Fizz")
    else:
        print(n)
(num(10))