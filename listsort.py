lst=list(map(int,input("Enter the Number: ").split()))
maxval=lst[0]
for i in range(len(lst)):
    if lst[i]>maxval:
        maxval=lst[i]
        
    