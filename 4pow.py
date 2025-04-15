n = int(input("enter the number"))
def checkifpower(n):
    if (n<=0) :
        return False
    if (n==1) :
        return True
    if (n%4== 0):
        return checkifpower(n/4)
    else :
        return False
print(checkifpower(n))