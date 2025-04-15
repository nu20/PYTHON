def reversenumber(num) :
    if(num > 0) :
        last = num%10
        if (num // 10 > 0) :
            currentnumber = int(''.join(reversed(str(num // 10))))
            return last * pow(10, len(str(currentnumber))) + currentnumber
        return num
input = int(input("enter the number"))
print(reversenumber(input))