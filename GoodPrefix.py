n=int(input())
arr=[int(x) for x in input().split()]

even=[]
odd=[]
for i in arr:
    if(i%2==0):
        even.append(2)
    else:
        odd.append(i)

oddcount=0
if(len(odd)%2==0):
    oddcount=1
else:
    oddcount=2

ans=len(even)+oddcount

print(ans)
