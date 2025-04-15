n = int(input("enter the number"))
def checkifpower(n):
    if (n<=0) :
        return False
    if (n==1) :
        return True
    if (n%2== 0):
        return checkifpower(n/2)
    else :
        return False
print(checkifpower(n))