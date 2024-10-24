def is_perfect(n: int) -> bool:
    if n < 1:
        return False
    divisors = [1]
    for i in range(2, n):
        if n % i == 0:
            divisors.append(i)
    return sum(divisors) == n



print(is_perfect(28))

