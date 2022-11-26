n=int(input())
arr=[int(x) for x in input().split()]

m={}
for i in arr:
    m[i]=m.get(i,0)+1

#print(m)
values=list(m.values())
#print(values)
values.sort()
cnt=0
max1=float("-inf")

for i ,v in enumerate(values):
    print(values,"values")
    max1=max(values)
    j=values.index(max1)
    print(max1,j,"Max and j")
    if(max1 >len(values)):
        z=[1 for x in values if x==0]
        cnt+=len(values)-1-len(z)
        for k in range(len(values)):                
            if(values[k]!=max1 and values[k]!=0):
                values[k]=values[k]-1
        values[j]=max1-len(values)+1
        print(cnt,"cnt if")
    else:
        cnt+=max1
        k=len(values)-1
        while(max1!=0):
            print(max1,k,"max1 k")
            k=k-1
            if(values[k]!=0):
                values[k]-=1
                max1-=1
        values[j]=0
        print(cnt,"cnt else")

print(cnt)


