def sum_i_squared_plus_1(n):
    running_sum = 0
    for i in range(n + 1):
        running_sum += i ** 2 + 1
    return running_sum


def sumintegers(n):
    return n*(n+1) / 2

print(sumintegers(100))
print(sumintegers(1000))
