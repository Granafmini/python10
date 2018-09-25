print("to check whether a number is armstrong or not")
n=int(input("N="))
t=n
s=0
a=0
while n>0:
    re=n%10
    a=re**3
    s=s+a
    n=n//10

if(t==s):
    print("armstrong")
else:
    print("not armstrong")
