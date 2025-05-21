import random

def miller(n,k):
    d=n-1
    s=0
    while d%2==0:
        d//=2
        s+=1
    def comp(a):
        x=pow(a,d,n)
        if x==1 or x==n-1:
            return False
        for _ in range(s-1):
            x=pow(x,2,n)
            if x==n-1:
                return False
        return True
    for _ in range(k):
        a=random.randint(2,n-2)
        if comp(a):
            return False
    return True

n=int(input("Enter a number to check prime: "))
k=int(input("Enter testing rounds: "))
if miller(n,k):
    print(n,"is prime")
else:
    print(n,"is not prime")
