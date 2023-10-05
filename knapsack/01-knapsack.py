
v = [15, 17, 14, 19, 11]
w = [4, 5, 3, 6, 2]

W = 11

x, y = len(v)+1, W+1


dp = [[0] * y for _ in range(x)]
so = [[[]] * y for _ in range(x)]

for i in range(1, x):
    for j in range(1, y):
        dp[i][j] = dp[i-1][j]
        so[i][j] = so[i-1][j]
        if j >= w[i-1]:
            dp[i][j] = max(dp[i-1][j], v[i-1]+dp[i-1][j-w[i-1]])

            if v[i-1]+dp[i-1][j-w[i-1]] >= dp[i-1][j]:
                so[i][j] = so[i-1][j-w[i-1]]+[i-1]

print(dp[-1][-1])
print(so[-1][-1])
