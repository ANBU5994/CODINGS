# Check if a Character is a Vowel or Consonant:
# Given a character,determine if it is a vowel (a, e, i, o, u) or a consonant using conditional statements.

n=input("enter the string ")
for i in n:
    if i in ("a","e","i","o","u"):
        print("vowels")
    else:
        print("constant")
