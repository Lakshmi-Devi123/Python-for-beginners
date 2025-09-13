a=int(input("Enter the Number: "))
b=int(input("Enter the Number: "))
c=int(input("Enter the Number: "))
if a>b and a>c:
    print(f"a is the biggest of three",a)
elif b>a and b>c:
    print(f"b is the biggest of three",b)
else:
    print(f"c is the biggest of three",c)
