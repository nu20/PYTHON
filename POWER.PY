ans = 0
a = 0
num = int(input("enter the number"))
while ans<num :
    ans = 1<<a 
    if ans==num :
        print("it is a power of two ")
        break
    a+=1
else:
    print("it is not a power of two")