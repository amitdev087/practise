arr = [int(x) for x in input().split()]
k, q = input().split()
queries = [[int(x) for x in input().split()] for _ in range(int(q))]

def modulating_array(arr,q,queries,k):
    max_number = 0
    for i in range(len(arr)):
        arr[i] = arr[i] - k
        max_number = max(arr[i],max_number)
    
    modulated_arr = []
    for i in range(1,max_number+1):
        temparr = [x%i for x in arr]
        modulated_arr.append(temparr)
     
    resarray = []
    print(modulated_arr)
    for ele in queries:
        print(ele[0],ele[1])
        count = 0
        if ele[0] == ele[1] or arr[ele[0]-1] == arr[ele[1]-1]:
            resarray.append(-1)
        else:
            for item in modulated_arr:
                if item[ele[0]-1] == item[ele[1]-1]:
                    count += 1
            resarray.append(count)
    return resarray
result = modulating_array(arr,int(q),queries,int(k))
print(result,sep='/n')