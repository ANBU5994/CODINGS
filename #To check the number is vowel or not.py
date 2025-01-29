# To check the number is vowel or not 

def check_vowel(n):
    n=n.lower()
    if n in ('aeiou'):
        print("the string contains vowel")
    else :
        print("the string Contains Consonant ")
n=input("enter the string : ")
check_vowel(n)