print("display prime numbers between two intervals")
s=int(input("s="))
e=int(input("e="))
flag=0
for x in range(s+1,e):
    flag=0
    for y in range(1,x+1):
        if(x%y==0):
            flag=flag+1
    if(flag==2):
         print(x)
