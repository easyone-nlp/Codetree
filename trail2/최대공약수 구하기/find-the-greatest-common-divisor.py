n, m = map(int, input().split())

def gcd(n, m):
    num_list = []
    if n > m:
        for num in range(1, m+1):
            if n % num == 0 and m % num == 0:
                num_list.append(num)
    else:
        for num in range(1, n+1):
            if n % num == 0 and m % num == 0:
                num_list.append(num)
    print(num_list[-1])

gcd(n, m)