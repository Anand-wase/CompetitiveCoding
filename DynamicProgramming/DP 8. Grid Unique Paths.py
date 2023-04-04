m=int(input()) #no of rows
n=int(input()) #no of columns


#Using Recurrsion
def fun(i,j,m,n):
    if i==m-1 and j==n-1:
        return 1 
    if i>=m or j>=n:
        return 0    
    return fun(i+1,j,m,n)+fun(i,j+1,m,n) 
print( fun(0,0,m,n))


#Using 2D array
dp=[[0 for i in range(n)]for j in range(m)]
for i in range(m):
    dp[i][0]=1
for j in range(n):
    dp[0][j]=1
for i in range(1,m):
    for j in range(1,n):
        dp[i][j]=dp[i-1][j]+dp[i][j-1]
print(dp[m-1][n-1])


#Using 1D array
dp=[1 for i in range(n)]
for i in range(1,m):
    for j in range(1,n):
        dp[j]=dp[j]+dp[j-1]
print(dp[n-1])