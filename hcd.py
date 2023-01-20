def hcf(a,b):
    if(b==0):
        return a
    else:
        return hcf(b,a%b)
print("Broi chlenove na redicata= ")
n=int(input())
a=int(input())
b=int(input())
for i in range(n-2):
        c=int(input())
k=hcf(hcf(a,b),c)
print("the gcd of a and b is:",end="")
print(k)
