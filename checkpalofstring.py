s=input("Enter the String: ")
revstr=""
for i in s:
    revstr=i+revstr
print(revstr)
if revstr==s:
    print("Palindrome")
else:
    print("Not Palindrome")