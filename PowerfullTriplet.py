t=int(input())
for i in range(t):
    n=int(input())
    arr=[int(x) for x in input().split()]
    arr=sorted(arr)
    x=arr[0]
    y=arr[-1]
    z=arr[-2]
    ans=abs(x-y)*z
    print(ans)



