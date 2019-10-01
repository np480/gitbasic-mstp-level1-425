def addition(a,b):
    c=a+b
    
    def isprime(n):
    factor=0
    for i in range(1,n+1):
        if n%i==0:
            factor+=1
        if factor==2: