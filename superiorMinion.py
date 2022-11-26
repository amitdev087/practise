s=input()
ans=1
cnt=1
for i in range(len(s)-1,-1,-1):
    if(s[i]==">"):
        cnt+=1
    elif(s[i]=="<"):
        
        cnt=1
    print(s[i],cnt)
    ans+=cnt

print(ans)




    