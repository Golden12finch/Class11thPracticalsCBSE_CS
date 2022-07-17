print("Welcome to the python calculator")
ans=int
num1=int(input("Write the first number:"))
num2=int(input("Write the second number:"))
operation=input("What do you want to do?:")
if(operation=="+"):
    ans=num1+num2
    print(ans)
elif(operation=="-"):
    ans=num1+num2
    print(ans)    
elif(operation=="/"):
    ans=num1/num2
    print(ans)
elif(operation=="*"):
    ans=num1*num2
    print(ans)
elif(operation=="%"):
    ans=num1%num2
    print(ans)
else:
    print("invalid input exiting with code 69")            