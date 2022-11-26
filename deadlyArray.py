# t=int(input())

# for i in range(t):
m={}
d=int(input())
prime=[]
c=2
while(d>1):
    if(d%c==0):
        prime.append(c)
        d=d/c
    else:
        c+=1

for i in prime:
    m[i]=m.get(i,0)+1

arr=list(m.values())
arr.sort()
ans=max(arr)
print(ans)


        

