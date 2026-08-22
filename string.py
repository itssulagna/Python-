# # # Take a string as input and count the number of vowels in it.

v="aeiou"
s="hello"
cnt=0
for word in s:
    if word in v:
        cnt+=1      
print(cnt)

# # # Take a string and print it in reverse without using a built-in reverse function.
s1="wtever"
s3=""
for i in range(len(s1)-1,-1,-1):
    s3+=s1[i]
print(s3)

# # # Take a string and check whether it is a palindrome.
s4="hello"
s5=""
for i in range(len(s4)-1,-1,-1):
    s5+=s4[i]
if s4==s5:
    print("is palindrome")
else:
    print("not palindrome")

# # Take a sentence and find the longest word in it.
s8="My name is sulagna"
s9=s8.split()
print(s9)
maxx=s9[0]
for word in s9:
    if len(maxx) < len(word):
        maxx=word
print(maxx)






    
