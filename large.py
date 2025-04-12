def largearray(a) :
    length = len(a)
    if length == 1 :
        return a[0]
    return max(a[0] , largearray(a[1 :]))
a = [18977777777777777777777777777777777777777777777777 ,9978999999999999999999999 ,6666666665 ,888888888888 , 987456763457347445 ,100000000000000000000]
print("largest element :" , largearray(a))