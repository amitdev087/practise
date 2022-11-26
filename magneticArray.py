n,b=[int(x) for x in input().split()]
arr=[int(x) for x in input().split()]

m={}

cal=0
maxCount=float("-inf")
for i in range(1,len(arr)):
    strength=abs(arr[i]-arr[i-1])
    m[i]=strength
# 7print(m,"m")
for i in range(1,len(arr)):
    cnt=0
    for j in range(i,len(arr)):
        if(cal<=b):
            cal+=m[j]
            # print(cal,"cal")
            cnt+=1
            # print(cnt,"cnt in cal")
        else:
            # print(maxCount,cnt,"final5")
            if(maxCount<cnt):
                maxCount=cnt
            break

print(maxCount)





