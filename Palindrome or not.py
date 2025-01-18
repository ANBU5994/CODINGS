# Input a string
string = input("Enter a string: ")

# Reverse the string and compare
if string == string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
