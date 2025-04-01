a = int(input("enter the greater number"))
b = int(input("enter the smaller number"))
if  b==0 :
    print("not possible")
    exit()
q = 0
while a>=b :
    a=a-b
    q+=1
print(q)