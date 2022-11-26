n=int(input())
arr=[int(x) for x in input().split()]
maxSum=float("-inf")

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

list1=[]
list1=solution(arr,list1,[],0)
print(list1)

for i in list1:
    curSum=sum(i)
    if(curSum%2==0):
        if(curSum>maxSum):
            maxSum=curSum

print(maxSum)