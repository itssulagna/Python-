

vowels=0
digit=0
consonents=0
s=input("enter string")
ch=s.split()
for word in  ch:
    if word in "aeiou":
        vowels=vowels+1
    elif (word>="a" and word<="z") and word not in "aeiou":
        consonents=consonents+1
    elif word in "123456789":
        digit=digit+1
print("Vowels=", vowels)
print("consonents=", consonents)
print("digit=", digit)