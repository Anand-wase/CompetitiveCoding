m=3
n=3
l=[[0,0,0],[0,1,0],[0,0,0]]


#Using Recurssion
def f(i,j,m,n,l):
    if i==m-1 and j==n-1:
        return 1
    if i>=m or j>=n:
        return 0
    if j+1<n and l[i][j+1]!=1:
        r=f(i,j+1,m,n,l)
    else:
        r=0
    if i+1<m and l[i+1][j]!=1:
        d=f(i+1,j,m,n,l)
    else:
        d=0
    return r+d
print(f(0,0,m,n,l))


#Using DP 2d array
if l[0][0]==1:
    print(0)
else:
    dp=[[0 for i in range(n)] for j in range(m)]
    dp[0][0]=1 
    for j in range(1,n):
        if l[0][j]==1:
            dp[0][j]=0
        else:
            dp[0][j]=dp[0][j-1]
    for i in range(1,m):
        if l[i][0]==1:
            dp[i][0]=0
        else:
            dp[i][0]=dp[i-1][0]
    for i in range(1,m):
        for j in range(1,n):
            if l[i][j]==1:
                dp[i][j]=0
            else:
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
    print(dp[m-1][n-1])


#Using 1D array
if l[0][0]==1:
    print(0)
else:
    dp1=[0 for i in range(n)]
    for i in range(m):
        for j in range(n):
            if i==0 and j==0:
                dp1[0]=1
            elif l[i][j]==1:
                dp1[j]=0
            elif i==0:
                dp1[j]=dp1[j-1]
            elif i>0 and j>0:
                dp1[j]+=dp1[j-1]
    print(dp1[n-1])