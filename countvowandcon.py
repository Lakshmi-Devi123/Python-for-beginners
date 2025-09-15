s=input("Enter the String: ")
countcon=0
countvow=0
vowel="AEIOUaeiou"
for i in s:
    if i.isalpha():
        if i in vowel:
            countvow=countvow+1
        else:
            countcon=countcon+1

print(countvow,countcon)    