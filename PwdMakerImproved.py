x=input("Press Y to generate a random secure password:")
if(x=="y"):
    NUM=int(input("Write any number:"))
    NAME=input("Write any name:")
    if(NUM>49):
        NUM=NUM*55
        print(NUM,NAME,sep="")
    else:
        NUM=NUM*131
        print(NUM,NAME,sep="")
else:
    print("Wrong input")            
