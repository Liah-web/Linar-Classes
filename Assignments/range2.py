
def sum(n):
    s=0
    for i in range (1,n+1):
        for j in range (1, i +1):
            s+=j
    print(s)

sum(13)