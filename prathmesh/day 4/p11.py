def pattern(n):
    for i in range(1,n+1):
        flag=i%2
        for j in range(i):
            print(flag,end="")
            flag=1-flag
        print()

pattern(5)