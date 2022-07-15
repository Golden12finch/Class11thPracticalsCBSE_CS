from re import X


x=int(input("Write the value of x:"))
y=int(input("Write the value of y:"))
z=int(input("Write the value of z:"))
if(x>y>z):
    print("The largest number is:",x)
elif(x<y>z):
    print("The largest number is:",y)
else:
    print("The largest number is:",z)
        
