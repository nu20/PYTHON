def ways(stars) :
    if stars <0 :
        return 0
    if stars == 0:
        return 1
    twosteps = 0
    onestep = 0
    if (stars>=2):
       twosteps = ways(stars - 2)
    onestep = ways(stars - 1)
    return twosteps + onestep
stars = int(input("enter the number of stairs"))
print("number of ways to climb : " , ways(stars))