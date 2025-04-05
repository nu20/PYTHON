def foc (n) :
    if(n==1 or n==0) :
        return 1
    return n*foc(n - 1) 
n = int(input("enter the number"))
print(foc(n))