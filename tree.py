def ind(n , num) :
    if (n<1 or n>num) :
        return
    print(n)
    ind(n - 1 , num)
    print(n)
n = int(input("enter any number n"))
ind(n , n)