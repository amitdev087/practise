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

def Result(arr,x,y):
    for k in arr:
        val=sum(k)
        if(val>=x and val<=y):
            return 1
    return 0

for i in range(t):
    q,l,r=[int(c) for c in input().split()]
    for j in range(q):
        x,y=[int(x) for x in input().split()]
        data=[]
        arr=[]
        for k in range(l,r+1):
            data.append(k)
        arr=solution(data,arr,[],0)
        #print(arr)
        ans=Result(arr,x,y)
        print(ans)

        


        
