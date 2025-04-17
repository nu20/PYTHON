n = int(input("enter the number of parenthesis"))
s = [""]*2*n
print("\n")

def par(g ,r ,s, k, n):
    if (k==2*n):
        for ss in s :
            print(ss , end='')
        print("\n")
        return
    if (g>r) :
        s[k] = "}"
        par(g,r+1,s,k+1,n)
    if (g<n):
        s[k] = "{"
        par(g+1,r,s,k+1,n)
par(0,0,s,0,n)

     