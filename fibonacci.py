import math
# 1,1,2,3,5,8,13,21,34,55,.....................
# f(1) = 1
# f(2) = 1
# f(3) = 2
# f(4) = 3
# f(5) = 5

def fibonacci_iter(n):
    f1, f2 = 0, 1
    i = 0
    while i < n:
        f1, f2 = f2, f1 + f2
        i = i + 1
    return f1

def fibonacci_rec(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)

def fibonacci_direct(n):
    return int((1/math.sqrt(5)) * (math.pow((1 + math.sqrt(5))/2 ,n) - math.pow((1 - math.sqrt(5))/2 ,n)))

def fibonacci_gen():
    f1, f2 = 0, 1
    while 1:
        f1, f2 = f2, f1 + f2
        yield f1

r1 = fibonacci_iter(4)
print(str(r1) + '\n')
r2 = fibonacci_rec(5)
print(str(r2) + '\n')
r3 = fibonacci_direct(7)
print(str(r3) + '\n')
r4 = fibonacci_gen()
print(r4.__next__())
print(r4.__next__())
print(r4.__next__())
print(r4.__next__())
print(r4.__next__())
print(r4.__next__())
