print("disply odd numbers between two intervalas")
s=int(input("s="))
e=int(input("e="))
if(s<=100000)&(e<=10000):
    for x in range(s,e+1):
     if(x%2!=0):
        print(x)

else:
      print("input is invalid")
