
l=[[2],[3,4],[6,5,7],[4,1,8,3]]
#using recurrsion
def fun(i,j,l):
    if i==len(l)-1:
        return l[i][j]
    return l[i][j]+min(fun(i+1,j,l),fun(i+1,j+1,l))
print(fun(0,0,l))

#using 1D array
dp=l[-1]
i=len(l)-2
while i>=0:
    for j in range(len(l[i])):
        dp[j]=min(dp[j],dp[j+1])+l[i][j]
    i-=1
print(dp[0])