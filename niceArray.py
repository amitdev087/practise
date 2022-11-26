n=int(input())
arr=[int(x) for x in input().split()]
m={}

def possition(arr,m):
    for i in range(len(arr)):
        temp=i
        # print(temp,"temp")
        del m[(arr[i])]
        # print(m,"m after deleting")
        res=(sum(arr) -arr[i])/2
        if(res in m):
            # print(res,"res")
            # print(m[res],"m[res]")
            # print(m,"m")
            return i

        m[float(arr[i])]=temp
        # print(m,"m after adding5")
    return -1

for i in range(len(arr)):
    if(arr[i] not in m):
        m[float(arr[i])]=i
# print(m)

print(possition(arr,m))






