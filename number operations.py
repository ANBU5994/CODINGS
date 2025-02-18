
'''
Given a number N your Task is to make N a single digit number by performing these operations

1) If N is odd, make it floor (N/2)

2) If N is even, make it floor((N-2)/2)

3) If N is already a single digit, print as it is

Example:

Input 1: N-25

Output 1: 12

Input 2: N-10

Output: 4

Input 3: N-5

Output: 5

'''


def num(n):
    n=abs(n)
    if  n > 0 and n<=9  :
        print(n)
    elif  n % 2 == 1:
        print((n-2)/2)
    elif n % 2 == 0:
        print(n/2)

print((num(-5)))