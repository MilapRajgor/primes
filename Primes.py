

def printPrimes(n):
    myList=list(range(2,n+1))

    for j in myList:
        print(j)
    # REMOVES ALL Composite 
        for i in range(j,(n//j)+1):
            if i*j in myList:
                myList.remove(i*j)


n=int(input("Enter an Upper bound:"))
printPrimes(n)