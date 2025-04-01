def swap1(a,b) :
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print ("After swapping : a = ", a , "b =" , b)

swap1(6,5)

def swap2(a,b) :
    a = (a&b) + (a | b )
    b = a + (~b) + 1
    a = a + (~b) + 1
    print ("After swapping : a = ", a , "b =" , b)

swap2(1,2)