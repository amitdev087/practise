t=int(input())
def solution(nums,ans,cur,index):
    if(index>len(nums)):
        return
    ans.append(cur[:])
    for i in range(index,len(nums)):
        if(nums[i] not in cur):
            cur.append(nums[i])
            solution(nums,ans,cur,i)
            cur.pop()
    return ans

for i in range(t):
    n,x,y =[int(x) for x in input().split()]
    data=[]
    for  j in range(1,n+1):
        data.append(j)
    arr=[]
    arr=solution(data,arr,[],0)
    #print(arr)
    m={}
    for j in range(1,len(arr)):
        k=len(arr[j])
        m[k]=m.get(k,0)+1
    #print(m)
    total=(2**n)-1
    ans=total-m[x]-m[y]
    print(ans)


