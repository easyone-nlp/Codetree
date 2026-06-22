N, M = map(int, input().split())
mat1 = [list(map(int, input().split())) for _ in range(N)]
mat2 = [list(map(int, input().split())) for _ in range(N)]

# print(mat2)

for i in range(N):
    for j in range(M):
        print(0 if mat1[i][j] == mat2[i][j] else 1, end= " ")
    print()
