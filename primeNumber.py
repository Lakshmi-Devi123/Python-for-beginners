num=int(input("Enter the Number to check: "))
count=0
for i in range(2,num):
    if num%i==0:
        count=count+1
if count==0:
    print("Prime Number")
else:
    print("Not Prime")
