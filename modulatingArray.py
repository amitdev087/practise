arr = [int(x) for x in input().split()]
k, q = input().split()
queries = [[int(x) for x in input().split()] for _ in range(int(q))]

def modulating_array(arr,q,queries,k):
    for i in range(len(arr)):
        arr[i]=arr[i]-k
    num =max(arr)
    modArray=[]
    for i in range(1,num+1):
        temp=[x%i for x in arr]
        modArray.append(temp)
    print(modArray)
    resArray=[]
    for ele in queries:
        cnt=0
        if(ele[0]==ele[1] or  arr[ele[0]-1] == arr[ele[1]-1]):
            resArray.append(-1)
        else:
            for item in modArray:
                if item[ele[0]-1] == item[ele[1]-1]:
                    cnt += 1
                    resArray.append(cnt)
    return resArray

result=modulating_array(arr,int(q),queries,int(k))
print(result)


