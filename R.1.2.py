def genap(k):
    if k == 0 :
        return True
    elif k == 1:
        return False
    else:
        return genap(k-2)


print(genap(601))
print(genap(602))
