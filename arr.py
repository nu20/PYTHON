def arraytotal(a) :
    length = len(a)
    if length == 1:
        return a[0]
    return a[0] + arraytotal(a[1:])
a = [1 ,3 ,4 ,22 ,7]
print("arraytotal:" , arraytotal(a))