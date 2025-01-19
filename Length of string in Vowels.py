# Length of string in Vowels
s=input("Enter string:")
vowels=0
s=s.lower()
for i in s:
    if i in "aeiou":
        vowels+=1
print(f"Vowels:{vowels}")
