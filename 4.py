n = int(input("enter the number :"))
if n&(n -1)==0:
    if n==1:
        print("it is a power of 4")
        exit()
    elif n%10==4 or n%10==6 :
        print("it is a power of 4")
    else:
        print("it is not a power of 4")
else:
    print("it is not a power of 4")