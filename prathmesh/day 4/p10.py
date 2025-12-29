def pattern(n):
    for i in range(1,2*n):
        if i<=n:
            for j in range(i):
                print("*",end="")
        else:
            for j in range(2*n-i):
                print("*",end="")
        print()

pattern(5)