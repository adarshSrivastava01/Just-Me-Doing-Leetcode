mat = [[1,2,3], [4,5,6], [7,8,9]]

def diagonalSum(mat):
    sum = 0
    n = len(mat)
    print("-------------",mat[n//2][n//2],"--------------")
    for i in range(n):
        print(i, "------", mat[i][i], "-------", mat[i][n-i-1], "--------", mat[n//2][n//2])
        sum = sum + mat[i][n - i - 1] + mat[i][i]
    sum = sum - mat[n//2][n//2]
    return sum

print(diagonalSum(mat))