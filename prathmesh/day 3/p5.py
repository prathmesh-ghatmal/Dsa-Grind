def pattern(n):
    for i in range(n,0,-1):
        for j in range(i):
            print("*",end="")
        print()

pattern(5)