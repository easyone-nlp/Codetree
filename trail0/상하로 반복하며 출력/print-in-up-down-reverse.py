N = int(input())

mat = [
    [i for i in range(1,N+1)]
    for _ in range(N)
]

new_mat = [
    [0 for _ in range(1,N+1)]
    for _ in range(N)
]
# print(mat)
for i in range(N):
    if i % 2 == 0:
        for j in range(N):
            new_mat[j][i] = mat[i][j]
    else:
        for j in range(N):
            new_mat[N-1-j][i] = mat[i][j]

for i in range(N):
    for j in range(N):
        print(new_mat[i][j], end="")
    print()