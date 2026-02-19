def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)

def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 1 or n == 2:
        memo[n] = 1
    else:
        memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

def matrix_mult(a, b):
    n = len(a)
    p = len(b)
    m = len(b[0])
    c = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(p):
            for k in range(m):
                c[i][k] += a[i][j] * b[j][k]
    return c

def test(a, b):
    if b <= 0:
        return 0
    if a > b:
        return a * b
    return test(a, b-2) + test(a-1, b-3) + 6

print(fib(7))
print(fib_memo(50))

a = [[1,2],[3,4]]
b = [[5,6],[7,8]]
print(matrix_mult(a,b))

print(test(3,7))
