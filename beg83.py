n1,n11,n31=map(str,input().split())
if n11=="%":
    res=int(n1)%int(n31)
elif n11=="/":
    res=int(n1)//int(n31)
print(res)
