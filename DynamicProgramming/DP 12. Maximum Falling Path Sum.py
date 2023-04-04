m=[[2,1,3],[6,5,4],[7,8,9]]
n=len(m)


#Using Recurrsion
def fun(i,j,m,n):
    if i==n-1:
        return m[i][j]
    if j<0 or j>=len(m[0]):
        return 0
    return m[i][j]+max(fun(i+1,j-1,m,n),fun(i+1,j,m,n),fun(i+1,j+1,m,n))
print(fun(0,0,m,n))


#Using DP
for i in range(len(m)-2,-1,-1):
    for j in range(len(m[0])):
        if j==0:
            m[i][j]+=max(m[i+1][j],m[i+1][j+1])
        elif j==len(m[0])-1:
            m[i][j]+=max(m[i+1][j],m[i+1][j-1])
        else:
            m[i][j]+=max(m[i+1][j],m[i+1][j+1],m[i+1][j-1])
print(max(m[0]))
