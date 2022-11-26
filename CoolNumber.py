t=int(input())
for i in range(t):
    n=int(input())
    a=[int(x) for x  in input().split()]
    m={}
    for y in range(1,26):
        for x in range(1,21):
            ans=(x*((3*y )+2)) +y
            if(ans<=103):
                m[ans]=1
    cnt=0
    for i in a:
        if(i in m):
            cnt+=1
    print(cnt)

    
