def totalflips (number1 , number2):
    flips = 0
    while number1 > 0 or number2 > 0 :
        t1 = number1 & 1
        t2 = number2 & 1
        if t1 != t2 :
            flips += 1
        
        number1>>=1
        number2>>=1
    return (flips)
num1 = int(input("enter your number"))
num2 = int(input("enter your number"))
print(totalflips(num1 ,num2))